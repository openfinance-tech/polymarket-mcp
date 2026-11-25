# Trade Polymarket with Cursor

> **Short answer:** Cursor connects to remote MCP servers, so its agent can research and trade Polymarket through OpenFinance with one click and no wallet private key in your config.

**MCP URL:** `https://api.openfinance.tech/agent/mcp` · Streamable HTTP · OAuth or `x-api-key` · by [OpenFinance](https://openfinance.tech), not affiliated with Polymarket

## Set up Cursor

First create your account at [openfinance.tech](https://openfinance.tech); your wallets are created for you.

<a href="https://cursor.com/en/install-mcp?name=openfinance-tech&config=eyJ1cmwiOiJodHRwczovL2FwaS5vcGVuZmluYW5jZS50ZWNoL2FnZW50L21jcCJ9"><img alt="Add to Cursor" src="https://cursor.com/deeplink/mcp-install-dark.svg" height="32" /></a>

Or copy [`examples/cursor/mcp.json`](../examples/cursor/mcp.json) to `~/.cursor/mcp.json`. Cursor shows **Needs login**; click it to sign in.

## Fund your Polymarket wallet

Orders spend pUSD in your Polymarket **deposit wallet**, which OpenFinance creates for you. Ask *"What's my Polymarket deposit wallet and balance?"*, then fund it with pUSD on Polygon, from your other OpenFinance wallets, or by debit card. [Funding details →](../README.md#fund-your-polymarket-wallet)

## Prompts to try in Cursor

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

- Your agent shows a summary of every order and waits for your go-ahead, such as replying "confirm". Keep Cursor's tool-approval prompts on too.
- Funds only move between your own wallets. Sending to anyone else needs your sign-in on openfinance.tech and a code from your authenticator app.
- There are no server-side trade limits, so fund only what you're willing to risk. Your agent can build a paper-trading system for you to use first.

## More

- [All 32 Polymarket actions](../README.md#what-your-agent-can-do) · [Troubleshooting](../README.md#troubleshooting) · [FAQ](../README.md#faq)
- [Guides for other apps and agents](./README.md)
- For agents: [AGENTS.md](../AGENTS.md)

<sub>Prediction markets carry a real risk of loss. Nothing here is financial advice. Polymarket isn't available in some countries.</sub>
