import requests

import zope.interface, logging
from twisted.internet import reactor

from Houdini.Plugins import Plugin
from Houdini.Handlers import Handlers
from Houdini.Events import Events

class Houdini_To_Discord_Relay(object):
    zope.interface.implements(Plugin)

    author = "PikaDude"
    version = 1.0
    description = "Relay chat from Club Penguin to Discord."

    discordWebhookURL = 'Fill me!'

    def __init__(self, server):
        self.logger = logging.getLogger("Houdini")
        self.server = server

        Handlers.Message += self.handleMessage
        Handlers.Login += self.handleLogin
        Events.Disconnected += self.handleDisconnection

    def ready(self):
        self.logger.info("Houdini to Discord has loaded.")

    def handleMessage(self, player, data):
        requests.post(url = self.discordWebhookURL, data = { "content": "**" + player.user.Username + "**: " + data.Message })

    def handleLogin(self, player, data):
        requests.post(url = self.discordWebhookURL, data = { "content": "***" + data.Username + "** joined the server*" })

    def handleDisconnection(self, player):
        requests.post(url = self.discordWebhookURL, data = { "content": "***" + player.user.Username + "** left the server*" })
