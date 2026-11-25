#!/bin/sh
# Checks the OpenFinance MCP server is reachable. Without credentials it answers
# 401 and points your client to sign-in, which is expected.
curl -si https://api.openfinance.tech/agent/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | grep -i -E '^HTTP|^www-authenticate'
