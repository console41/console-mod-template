# -*- coding: utf-8 -*-
from ...config.configUtils import *
from ...library.consoleMod.config.configUtils import CLIENT_SYSTEM_NAME, SERVER_SYSTEM_NAME
from ...constant.serverConstant import *
from ...library.consoleMod.serverApi import Listen

serverSystem = serverApi.GetSystem(MOD_NAME, SERVER_SYSTEM_NAME)

NotifyToClient = serverSystem.NotifyToClient
NotifyToMultiClients = serverSystem.NotifyToMultiClients
BroadcastToAllClient = serverSystem.BroadcastToAllClient
BroadcastEvent = serverSystem.BroadcastEvent
CreateEngineEntityByNBT = serverSystem.CreateEngineEntityByNBT
CreateEngineItemEntity = serverSystem.CreateEngineItemEntity
CreateEngineEntityByTypeStr = serverSystem.CreateEngineEntityByTypeStr
DestroyEntity = serverSystem.DestroyEntity
