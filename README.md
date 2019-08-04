# Houdini To Discord Relay
Relay chat from [Houdini](https://github.com/Solero/Houdini) to [Discord](https://discordapp.com).

# Previews
![](https://i.am-a.ninja/Ds7aJWL.png)
![](https://i.am-a.ninja/auxmrmW.png)

# Installation
1. Run `git clone https://github.com/PikaDude/Houdini_To_Discord_Relay.git` in `Houdini/Plugins`
2. Move into the `Houdini_To_Discord_Relay` directory
3. Open `__init__.py` and set `discordWebhookURL` to your [webhook URL](#how-to-get-a-webhook-url)
4. Make sure the `requests` package is installed (`pip install requests`)
5. Add `Houdini_To_Discord_Relay` to the Plugins array in Houdini's `config.py`

# How to get a Webhook URL
1. Edit the Discord channel you want to have messages forwarded from Houdini to.  
![](https://i.am-a.ninja/9CtEVTX.png)
2. Navigate to the Webhooks tab and press "Create Webhook".  
![](https://i.am-a.ninja/4YrwfhA.png)
3. Give it a cool name and icon if you want.
4. Copy the webhook URL and set `discordWebhookURL`'s value to it.  
![](https://i.am-a.ninja/3rMy1Gi.png)
