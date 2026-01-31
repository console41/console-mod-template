# -*- coding: utf-8 -*-
from ...constant.clientConstant import *

screenNode = clientApi.GetScreenNodeCls()


class BaseScreenNode(screenNode):
    _createFunc = []  # UI创建时需调用的函数
    _updateFunc = []
    _destroyFunc = []

    def __init__(self, namespace, name, param):
        super(BaseScreenNode, self).__init__(namespace, name, param)

    @classmethod
    def UICreate(cls, func):
        # 检查当前类是否自己有_createFunc(不是继承自父类的)
        if not hasattr(cls, '_createFunc') or cls._createFunc is BaseScreenNode._createFunc:
            # 为当前子类动态创建一个空列表
            cls._createFunc = []
        cls._createFunc.append(func)
        return func

    @classmethod
    def UIUpdate(cls, func):
        if not hasattr(cls, '_updateFunc') or cls._updateFunc is BaseScreenNode._updateFunc:
            cls._updateFunc = []
        cls._updateFunc.append(func)
        return func

    @classmethod
    def UIDestroy(cls, func):
        if not hasattr(cls, '_destroyFunc') or cls._destroyFunc is BaseScreenNode._destroyFunc:
            cls._destroyFunc = []
        cls._destroyFunc.append(func)
        return func

    def Create(self):
        super(BaseScreenNode, self).Create()
        for func in self._createFunc:
            func()

    def Update(self):
        super(BaseScreenNode, self).Update()
        for func in self._updateFunc:
            func()

    def Destroy(self):
        super(BaseScreenNode, self).Destroy()
        for func in self._destroyFunc:
            func()
