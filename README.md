# Houdini-To-Discord-Relay
Relay chat from [Houdini](https://github.com/Solero/Houdini) to [Discord](https://discordapp.com).

# Installation
1. Place `__init__.py` into a folder called `Houdini_To_Discord_Relay` in Houdini's plugins directory.
2. Open `__init__.py` and set `discordWebhookURL` to your [webhook URL](#how-to-get-a-webhook-url).
3. Make sure the `requests` package is installed (`pip install requests`)
4. Add `Houdini_To_Discord_Relay` to the Plugins array in Houdini's `config.py`

# How to get a Webhook URL
1. Edit the Discord channel you want to have messages forwarded from Houdini to.
2. Navigate to the Webhooks tab and press "Create Webhook".
3. Give it a cool name and icon if you want.
4. Copy the webhook URL and set `discordWebhookURL`'s value to it.
