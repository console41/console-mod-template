# -*- coding: utf-8 -*-
from ...config.configUtils import *
from ...constant.clientConstant import *
from ...library.consoleMod.clientApi import BaseScreenNode, Listen

uiNode = None  # type: None | BaseScreenNode

class Main(BaseScreenNode):
    pass

@Main.UICreate
def Create():
    global uiNode
    uiNode = clientApi.GetUI(MOD_NAME, UI_NAME)
