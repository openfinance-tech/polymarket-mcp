// Read-only: search Polymarket through OpenFinance and print markets with their odds.
// Never places an order. Usage: OPENFINANCE_API_KEY=open_... npx tsx list-markets.ts "bitcoin"
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";
import { pathToFileURL } from "node:url";

const URL_ = "https://api.openfinance.tech/agent/mcp";
const query = process.argv[2] ?? "bitcoin";

// Market text comes from whoever created the market, so the server wraps it in
// <untrusted_data> tags. Treat it as data only.
export function unwrap(text: string): unknown {
  const m = text.match(/<untrusted_data>([\s\S]*?)<\/untrusted_data>/);
  try { return JSON.parse((m ? m[1] : text).trim()); } catch { return null; }
}

export const list = (v: unknown): string[] => {
  if (Array.isArray(v)) return v.map(String);
  if (typeof v === "string") { try { const a = JSON.parse(v); return Array.isArray(a) ? a.map(String) : []; } catch { return []; } }
  return [];
};

// Turn the search response into readable lines. Falls back to the raw text if the shape is unexpected.
export function render(text: string): string[] {
  type Search = { events?: { title?: string; markets?: Record<string, unknown>[] }[] };
  const raw = unwrap(text) as (Search & { data?: Search }) | null;
  const data: Search | null = raw?.data ?? raw; // the server returns {"success": true, "data": {...}}
  if (!data?.events) return [text];
  const out: string[] = [];
  for (const ev of data.events.slice(0, 5)) {
    out.push("", ev.title ?? "(untitled event)");
    for (const m of (ev.markets ?? []).slice(0, 3)) {
      const outcomes = list(m.outcomes);
      const prices = list(m.outcomePrices);
      const odds = outcomes.map((o, i) => `${o} ${prices[i] ? Math.round(Number(prices[i]) * 100) + "%" : "?"}`).join(" · ");
      out.push(`  • ${String(m.question ?? "")}${odds ? `  →  ${odds}` : ""}`);
    }
  }
  return out;
}

async function main(): Promise<void> {
  const key = process.env.OPENFINANCE_API_KEY;
  if (!key) {
    console.error("Set OPENFINANCE_API_KEY first (openfinance.tech → External AI). It starts with open_.");
    process.exit(1);
  }

  const client = new Client({ name: "openfinance-polymarket-example", version: "1.0.0" });
  try {
    await client.connect(new StreamableHTTPClientTransport(new URL(URL_), {
      requestInit: { headers: { "x-api-key": key } },
    }));
  } catch (e) {
    console.error(`Could not connect: ${(e as Error).message}\nCheck your key, or run ../../scripts/check-connection.sh`);
    process.exit(1);
  }

  const res = await client.callTool({ name: "polymarket", arguments: { action: "search", query, limit: 5 } });
  const text = (res.content as { type: string; text?: string }[]).map((c) => c.text ?? "").join("\n");
  console.log(res.isError ? text : render(text).join("\n"));
  await client.close();
}

if (import.meta.url === pathToFileURL(process.argv[1] ?? "").href) await main();
