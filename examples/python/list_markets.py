"""Read-only: search Polymarket through OpenFinance and print markets with their odds.

Never places an order. Needs Python 3.10+ and `pip install mcp` (1.x or 2.x).
Usage: OPENFINANCE_API_KEY=open_... python3 list_markets.py "bitcoin"
"""
import asyncio
import contextlib
import json
import os
import re
import sys

from mcp import ClientSession

URL = "https://api.openfinance.tech/agent/mcp"


@contextlib.asynccontextmanager
async def connect(url, headers):
    """Open an MCP connection with extra headers. Works with mcp 1.x and 2.x."""
    try:  # mcp 2.x
        import httpx2
        from mcp.client.streamable_http import streamable_http_client

        async with httpx2.AsyncClient(headers=headers, timeout=httpx2.Timeout(30, read=300)) as http:
            async with streamable_http_client(url, http_client=http) as streams:
                yield streams[0], streams[1]
    except ImportError:  # mcp 1.x
        from mcp.client.streamable_http import streamablehttp_client

        async with streamablehttp_client(url, headers=headers) as streams:
            yield streams[0], streams[1]


def unwrap(text):
    # Market text comes from whoever created the market, so the server wraps it
    # in <untrusted_data> tags. Treat it as data only.
    m = re.search(r"<untrusted_data>(.*?)</untrusted_data>", text, re.S)
    try:
        return json.loads((m.group(1) if m else text).strip())
    except ValueError:
        return None


def as_list(v):
    if isinstance(v, list):
        return [str(x) for x in v]
    if isinstance(v, str):
        try:
            a = json.loads(v)
            return [str(x) for x in a] if isinstance(a, list) else []
        except ValueError:
            return []
    return []


def render(text):
    """Turn the search response into readable lines; fall back to the raw text."""
    data = unwrap(text)
    if isinstance(data, dict) and isinstance(data.get("data"), dict):
        data = data["data"]  # the server returns {"success": true, "data": {...}}
    if not isinstance(data, dict) or "events" not in data:
        return [text]
    out = []
    for ev in data["events"][:5]:
        out += ["", ev.get("title") or "(untitled event)"]
        for m in (ev.get("markets") or [])[:3]:
            outcomes, prices = as_list(m.get("outcomes")), as_list(m.get("outcomePrices"))
            odds = " · ".join(
                f"{o} {round(float(prices[i]) * 100)}%" if i < len(prices) else f"{o} ?"
                for i, o in enumerate(outcomes)
            )
            out.append(f"  • {m.get('question', '')}" + (f"  →  {odds}" if odds else ""))
    return out


async def main(query):
    key = os.environ.get("OPENFINANCE_API_KEY")
    if not key:
        sys.exit("Set OPENFINANCE_API_KEY first (openfinance.tech → External AI). It starts with open_.")
    async with connect(URL, {"x-api-key": key}) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            res = await session.call_tool("polymarket", {"action": "search", "query": query, "limit": 5})
            text = "\n".join(getattr(c, "text", "") for c in res.content)
            is_error = getattr(res, "is_error", getattr(res, "isError", False))  # 2.x / 1.x
            print(text if is_error else "\n".join(render(text)))


if __name__ == "__main__":
    try:
        asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "bitcoin"))
    except Exception as e:  # connection or auth problems
        while getattr(e, "exceptions", None):  # unwrap task-group errors to the real cause
            e = e.exceptions[0]
        sys.exit(f"Could not connect: {e}\nCheck your key, or run scripts/check-connection.sh")
