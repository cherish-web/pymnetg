# _*_ coding: utf-8 _*_
# @Time : 2021/4/27 下午 06:52 
# @Author : cherish_peng
# @Email : 1058386071@qq.com 
# @File : __init__.py
# @Software : PyCharm
from .mnetg import Mnetg
from .mnetg_device import Device as Dev
from .base_worker import BaseWorker
from .mnnetg_enum import ChanEnum


class MnetgWorker(BaseWorker):
    def __init__(self, st_no, net_no, chan: ChanEnum, mode=0):
        self.mnetg = Mnetg(st_no, net_no)
        self.chan = chan.value
        self.mode = mode
        self.is_open = False

    def connect(self):
        result = self.mnetg.md_open(self.chan, self.mode)
        if result == 0:
            self.is_open = True
            return True
        return False

    def disconnect(self):
        result = self.mnetg.md_close()
        if result == 0:
            self.is_open = False
            return True
        return False

    def is_connected(self):
        return self.is_open

    def _get_device_type(self, device):
        start_addr = int(device[len(device) - 4:], 16)
        device_type = device[:len(device)-4]
        if hasattr(Dev, device_type):
            device_type = getattr(Dev, device_type)
        else:
            raise Exception(f"device_type({device_type}) is error")
        return device_type, start_addr

    def read(self, device, length):
        """
        读数据
        :param device: 软元件(D0000)
        :param length: 读取长度
        :return: dic
        """
        device_type, start_addr = self._get_device_type(device)
        code, data = self.mnetg.md_receive_ex(device_type, start_addr,
                                              length)
        if code == 0:
            res = {'res': data, 'code': code, 'desc': ''}
        else:
            res = {'res': None, 'code': code, 'desc': 'It cannot communicate'}
        return res

    def write(self, device, data):
        """
        写数据
        :param device: 软元件(D0000)
        :param data: list
        :return: dic
        """
        device_type, start_addr = self._get_device_type(device)
        code = self.mnetg.md_send_ex(device_type, start_addr, len(data), data)
        if code == 0:
            res = {'res': True, 'code': code, 'desc': ''}
        else:
            res = {'res': False, 'code': code, 'desc': 'It cannot communicate'}
        return res
