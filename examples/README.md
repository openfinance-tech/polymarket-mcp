# Examples

Ready-to-copy configs for the OpenFinance MCP server (`https://api.openfinance.tech/agent/mcp`). OAuth sign-in needs no key at all; these files show the API-key option where a client needs one. Keep your key in the `OPENFINANCE_API_KEY` environment variable and never commit it.

| File | Client | Where it goes |
|---|---|---|
| [`claude-code/.mcp.json`](./claude-code/.mcp.json) | Claude Code | Your project root (Claude Code expands `${OPENFINANCE_API_KEY}`) |
| [`cursor/mcp.json`](./cursor/mcp.json) | Cursor (OAuth) | `~/.cursor/mcp.json` or `.cursor/mcp.json` |
| [`vscode/mcp.json`](./vscode/mcp.json) | VS Code (Copilot agent mode) | `.vscode/mcp.json` (VS Code asks for the key once and stores it securely) |
| [`codex/config.toml`](./codex/config.toml) | Codex CLI and IDE extension | `~/.codex/config.toml` |
| [`openclaw/openclaw.json`](./openclaw/openclaw.json) | OpenClaw | `~/.openclaw/openclaw.json` (keep `"transport": "streamable-http"`; the key comes from `OPENFINANCE_API_KEY`) |
| [`hermes/config.yaml`](./hermes/config.yaml) | Hermes Agent | `~/.hermes/config.yaml`, then `/reload-mcp` |
| [`claude-desktop/claude_desktop_config.json`](./claude-desktop/claude_desktop_config.json) | Claude Desktop with an API key | Settings → Developer → Edit Config. Replace `open_...` with your key, and don't share the file. With OAuth, use Settings → Connectors instead. |

Scripts (read-only, they never place orders):

| Folder | Run |
|---|---|
| [`typescript/`](./typescript) | `npm install && npx tsx list-markets.ts "bitcoin"` |
| [`python/`](./python) | `pip install mcp && python3 list_markets.py "bitcoin"` |
