import sys
import dbus
import math
import subprocess
from traceback import print_exc
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'aix'

LOGGER = getLogger(__name__)

class KonversationControlDesktopSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(KonversationControlDesktopSkill, self).__init__(name="KonversationControlDesktopSkill")
        
    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))
        
        konversationcontrol_showwin_intent = IntentBuilder("KonversationShowKeywordIntent").\
            require("InternalKonversationShowKeyword").build()
        self.register_intent(konversationcontrol_showwin_intent, self.handle_konversationcontrol_showwin_intent)
        
        konversationcontrol_quitwin_intent = IntentBuilder("KonversationQuitKeywordIntent").\
            require("InternalKonversationQuitKeyword").build()
        self.register_intent(konversationcontrol_quitwin_intent, self.handle_konversationcontrol_quitwin_intent)
        
        konversationcontrol_openservlist_intent = IntentBuilder("KonversationOpenServListIntent").\
            require("InternalKonversationOpenServListKeyword").build()
        self.register_intent(konversationcontrol_openservlist_intent, self.handle_konversationcontrol_openservlist_intent)
        
        konversationcontrol_openidentity_intent = IntentBuilder("KonversationOpenIdentityIntent").\
            require("InternalKonversationOpenIdentityKeyword").build()
        self.register_intent(konversationcontrol_openidentity_intent, self.handle_konversationcontrol_openidentity_intent)

    def handle_konversationcontrol_showwin_intent(self, message):
                bus = dbus.SessionBus()
                remote_object = bus.get_object("org.kde.konversation","/konversation/MainWindow_1")
                remote_object.showNormal(dbus_interface = "org.qtproject.Qt.QWidget")
                remote_object.activateAndRaiseWindow(dbus_interface = "org.kde.konversation.MainWindow")
                
    def handle_konversationcontrol_quitwin_intent(self, message):
                bus = dbus.SessionBus()
                remote_object = bus.get_object("org.kde.konversation","/konversation/MainWindow_1")
                remote_object.quitProgram(dbus_interface = "org.kde.konversation.MainWindow")
                
    def handle_konversationcontrol_openservlist_intent(self, message):
                bus = dbus.SessionBus()
                remote_object = bus.get_object("org.kde.konversation","/konversation/MainWindow_1")
                remote_object.openServerList(dbus_interface = "org.kde.konversation.MainWindow")
                remote_object.activateAndRaiseWindow(dbus_interface = "org.kde.konversation.MainWindow")

    def handle_konversationcontrol_openidentity_intent(self, message):
                bus = dbus.SessionBus()
                remote_object = bus.get_object("org.kde.konversation","/konversation/MainWindow_1")
                remote_object.openIdentitiesDialog(dbus_interface = "org.kde.konversation.MainWindow")
                remote_object.activateAndRaiseWindow(dbus_interface = "org.kde.konversation.MainWindow")
                
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return KonversationControlDesktopSkill()
