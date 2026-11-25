# Trade Polymarket with ChatGPT

> **Short answer:** ChatGPT reaches Polymarket through a custom MCP connector. Add OpenFinance once and ChatGPT can search Polymarket, read live odds and order books, and place, cancel and redeem bets after you confirm.

**MCP URL:** `https://api.openfinance.tech/agent/mcp` · Streamable HTTP · OAuth or `x-api-key` · by [OpenFinance](https://openfinance.tech), not affiliated with Polymarket

## Set up ChatGPT

First create your account at [openfinance.tech](https://openfinance.tech); your wallets are created for you.

1. Open **Settings → Apps & Connectors**. If you don't see **Create**, turn on **Developer mode** under **Advanced settings**.
2. Click **Create**. Name: `OpenFinance`. URL: `https://api.openfinance.tech/agent/mcp`. Authentication: **OAuth**.
3. Sign in to OpenFinance and approve. In a new chat, pick **OpenFinance** from the tools menu.

Custom connectors need a ChatGPT plan that supports them (Plus, Pro, Business, Enterprise or Edu).

## Fund your Polymarket wallet

Orders spend pUSD in your Polymarket **deposit wallet**, which OpenFinance creates for you. Ask *"What's my Polymarket deposit wallet and balance?"*, then fund it with pUSD on Polygon, from your other OpenFinance wallets, or by debit card. [Funding details →](../README.md#fund-your-polymarket-wallet)

## Prompts to try in ChatGPT

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

- Your agent shows a summary of every order and waits for your go-ahead, such as replying "confirm". Keep ChatGPT's tool-approval prompts on too.
- Funds only move between your own wallets. Sending to anyone else needs your sign-in on openfinance.tech and a code from your authenticator app.
- There are no server-side trade limits, so fund only what you're willing to risk. Your agent can build a paper-trading system for you to use first.

## More

- [All 32 Polymarket actions](../README.md#what-your-agent-can-do) · [Troubleshooting](../README.md#troubleshooting) · [FAQ](../README.md#faq)
- [Guides for other apps and agents](./README.md)
- For agents: [AGENTS.md](../AGENTS.md)

<sub>Prediction markets carry a real risk of loss. Nothing here is financial advice. Polymarket isn't available in some countries.</sub>
