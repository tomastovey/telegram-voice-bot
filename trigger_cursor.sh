#!/bin/bash

COMMAND=$(cat ~/Documents/telegram-voice-bot/commands.txt)
ENCODED_COMMAND=$(python3 -c "import urllib.parse; print(urllib.parse.quote('''$COMMAND'''))")

open "https://actions.zapier.com/mcp/sk-ak-hxUa7DCZtJ8ryTrBJn5iHFBx9Z/sse?input=$ENCODED_COMMAND"

