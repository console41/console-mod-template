# -*- coding: utf-8 -*-
from ...config.configUtils import *
from ...library.consoleMod.config.configUtils import SERVER_SYSTEM_NAME, CLIENT_SYSTEM_NAME
from ...constant.clientConstant import *
from ...library.consoleMod.clientApi import Listen

clientSystem = clientApi.GetSystem(MOD_NAME, CLIENT_SYSTEM_NAME)

NotifyToServer = clientSystem.NotifyToServer
CreateEngineSfx = clientSystem.CreateEngineSfx
CreateEngineSfxFromEditor = clientSystem.CreateEngineSfxFromEditor
CreateEngineParticle = clientSystem.CreateEngineParticle
CreateEngineEffectBind = clientSystem.CreateEngineEffectBind
DestroyEntity = clientSystem.DestroyEntity
CreateClientEntityByTypeStr = clientSystem.CreateClientEntityByTypeStr
DestroyClientEntity = clientSystem.DestroyClientEntity
BroadcastEvent = clientSystem.BroadcastEvent
