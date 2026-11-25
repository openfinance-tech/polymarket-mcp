# Contributing

This repository shows how to research and trade Polymarket from AI apps through the hosted OpenFinance MCP server at `https://api.openfinance.tech/agent/mcp`. It holds per-app guides in [`docs/`](./docs), example configs and scripts in [`examples/`](./examples), and a connection check in [`scripts/`](./scripts).

## Good first contributions

- **A guide that didn't work in your app.** The app, its version, the config you used and what happened. Open an issue, or fix the page in `docs/`.
- **An app we don't cover yet.** Add a page to `docs/` and, if it uses a config file, an example in `examples/`.
- **An example that no longer matches the server's response.** Include the call and the response you got.

## Run the examples

They are read-only: they search Polymarket and print odds, and never place orders.

```bash
export OPENFINANCE_API_KEY="open_..."   # from openfinance.tech → External AI

# TypeScript
cd examples/typescript && npm install && npx tsx list-markets.ts "bitcoin"

# Python 3.10+
pip install mcp && python3 examples/python/list_markets.py "bitcoin"
```

## Rules for changes

1. Use the real endpoint. Don't add a second server or a local wallet key in any config.
2. Keep examples read-only. Orders belong in the sample session, behind a quote and the user's "confirm".
3. Funds only move between the user's own wallets. Don't describe server-side trade limits; there aren't any.
4. Never put a real API key, wallet address or account detail in an issue, example or screenshot.

## Security issues

Don't open a public issue for a security problem. Follow [SECURITY.md](./SECURITY.md).
