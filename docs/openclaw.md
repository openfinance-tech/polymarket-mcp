# Trade Polymarket with OpenClaw

> **Short answer:** OpenClaw connects to OpenFinance as a remote MCP server (Streamable HTTP). Your agent can then search Polymarket, read live odds and order books, and place, cancel and redeem bets after you confirm.

**MCP URL:** `https://api.openfinance.tech/agent/mcp` · Streamable HTTP · OAuth or `x-api-key` · by [OpenFinance](https://openfinance.tech), not affiliated with Polymarket

## Set up OpenClaw

First create your account at [openfinance.tech](https://openfinance.tech); your wallets are created for you.

```bash
openclaw mcp add openfinance-tech \
  --url https://api.openfinance.tech/agent/mcp \
  --transport streamable-http
openclaw mcp doctor openfinance-tech --probe
```

OpenClaw treats remote servers as SSE unless you set `streamable-http`, so keep that flag. To use an API key, add it as a header in the Control UI's config editor with a `${OPENFINANCE_API_KEY}` reference, or copy [`examples/openclaw/openclaw.json`](../examples/openclaw/openclaw.json) into `~/.openclaw/openclaw.json` (servers sit under `mcp.servers`).

## Fund your Polymarket wallet

Orders spend pUSD in your Polymarket **deposit wallet**, which OpenFinance creates for you. Ask *"What's my Polymarket deposit wallet and balance?"*, then fund it with pUSD on Polygon, from your other OpenFinance wallets, or by debit card. [Funding details →](../README.md#fund-your-polymarket-wallet)

## Prompts to try in OpenClaw

```text
Using OpenFinance, what are the Polymarket odds on the next Fed rate decision?
```
```text
Who are the top 10 Polymarket sports traders this week, and what is the #1 wallet holding?
```
```text
Bet $10 on the favourite, then show my open Polymarket positions.
```

## Before you trade

- Your agent shows a summary of every order and waits for your go-ahead, such as replying "confirm". Keep OpenClaw's tool-approval prompts on too.
- Funds only move between your own wallets. Sending to anyone else needs your sign-in on openfinance.tech and a code from your authenticator app.
- There are no server-side trade limits, so fund only what you're willing to risk. Your agent can build a paper-trading system for you to use first.

## More

- [All 32 Polymarket actions](../README.md#what-your-agent-can-do) · [Troubleshooting](../README.md#troubleshooting) · [FAQ](../README.md#faq)
- [Guides for other apps and agents](./README.md)
- For agents: [AGENTS.md](../AGENTS.md)

<sub>Prediction markets carry a real risk of loss. Nothing here is financial advice. Polymarket isn't available in some countries.</sub>
