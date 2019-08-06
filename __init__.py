import zope.interface, logging, requests

from twisted.internet import reactor, task
from Houdini.Plugins import Plugin
from Houdini.Handlers import Handlers
from Houdini.Events import Events

class Houdini_To_Discord_Relay(object):
    zope.interface.implements(Plugin)

    author = "PikaDude"
    version = 1.2
    description = "Relay chat from Club Penguin to Discord."

    discordWebhookURL = 'Fill me!'

    messageQueue = []

    def __init__(self, server):
        self.logger = logging.getLogger("Houdini")
        self.server = server

        Handlers.Message += self.handleMessage
        Handlers.Login += self.handleLogin
        Events.Disconnected += self.handleDisconnection

        l = task.LoopingCall(self.runMessageQueue)
        l.start(0.5)

    def ready(self):
        self.logger.info("Houdini to Discord has loaded.")

    def handleMessage(self, player, data):
        self.messageQueue.append("[" + player.room.Name + "] **" + player.user.Username + "**: " + data.Message)

    def handleLogin(self, player, data):
        self.messageQueue.append("***" + data.Username + "** joined the server*")

    def handleDisconnection(self, player):
        self.messageQueue.append("***" + player.user.Username + "** left the server*")

    def runMessageQueue(self):
        if len(self.messageQueue) == 0: pass
        else:
            message = "\n".join(self.messageQueue)
            del self.messageQueue [:]
            requests.post(url = self.discordWebhookURL, data = { "content": message })
            pass