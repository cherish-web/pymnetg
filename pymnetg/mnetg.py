# _*_ coding: utf-8 _*_
# @Time : 2021/4/27 下午 06:47 
# @Author : cherish_peng
# @Email : 1058386071@qq.com 
# @File : mnetg.py
# @Software : PyCharm
from ctypes import *
import math
from .mnetg_device import DeviceInfo
from .mnnetg_enum import DevTypeEnum


class Mnetg:
    def __init__(self, st_no, net_no):
        self.net_no = net_no
        self.st_no = st_no
        self.path = c_int(0)
        try:
            self.dll = windll.LoadLibrary("MDFUNC32.DLL")
        except FileNotFoundError:
            raise Exception("Mnetg driver not installed!")

    @staticmethod
    def get_ctypes_by_length_bin(length: int):
        _buf_n = c_short * math.ceil(length / 16)
        _buf = _buf_n()
        return _buf

    @staticmethod
    def get_ctypes_by_length(length: int):
        _buf_n = c_short * length
        _buf = _buf_n()
        return _buf

    @staticmethod
    def get_ctypes_by_list(buf: list):
        _buf_n = c_short * len(buf)
        _buf = _buf_n()
        for i in range(len(buf)):
            _buf[i] = buf[i]
        return _buf

    @staticmethod
    def get_ctypes_by_list_bin(buf: list):
        _buf_n = c_short * math.ceil(len(buf) / 16)
        _buf = _buf_n()
        for i in range(math.ceil(len(buf) / 16)):
            for j in range(16):
                if i * 16 + j < len(buf):
                    _buf[i] |= buf[i * 16 + j] << j
        return _buf

    @staticmethod
    def get_list_by_ctypes(buf: Array):
        return [_buf for _buf in buf]

    @staticmethod
    def get_list_by_ctypes_bin(buf: Array, start_index: int, length: int):
        _buf = []
        for _bits in buf:
            for i in range(16):
                if i < start_index:
                    continue
                else:
                    start_index = 0
                if len(_buf) < length:
                    _buf.append((_bits >> i) & 1)
                else:
                    break
        return _buf

    def md_open(self, chan: int, mode: int):
        '''
        Open MNETG
        :param chan: channel No
        :param mode: MNET open mode
        :return: code
        '''
        return self.dll.mdOpen(chan, mode, byref(self.path))

    def md_close(self):
        '''
        Close MNETG
        :return: code
        '''
        return self.dll.mdClose(self.path)

    def md_send(self, devi: DeviceInfo, dev_no: int, size_renamed: int, buf: list):
        '''
        Write MNETG
        :param devi: device
        :param dev_no: start address
        :param size_renamed: length
        :param buf: data
        :return: code
        '''
        if devi.dev_type == DevTypeEnum.Bit:
            if size_renamed <= 8 - dev_no % 8:
                return self._md_batch_refresh_bit(devi, dev_no, buf[:size_renamed])
            else:
                if dev_no % 8:
                    f_len = 8 - dev_no % 8
                    code = self._md_batch_refresh_bit(devi, dev_no, buf[:f_len])
                else:
                    f_len = 0
                b_len = (dev_no + size_renamed + 1) % 8
                if b_len > 1:
                    code = self._md_batch_refresh_bit(devi, dev_no + size_renamed + 1 - b_len,
                                                      buf[size_renamed - b_len + 1:])
                    m_len = size_renamed - b_len - f_len + 1
                    if m_len > 0:
                        _buf = self.get_ctypes_by_list_bin(
                            buf[f_len:m_len + f_len])
                        _size_renamed = c_short(m_len // 8)
                        code = self.dll.mdSendEx(self.path, self.st_no | (self.net_no*0x100), devi.dev_code.value,
                                                 dev_no + f_len, byref(_size_renamed), byref(_buf))
                else:
                    _size_renamed = c_short((size_renamed - f_len) // 8)
                    _buf = self.get_ctypes_by_list_bin(
                        buf[f_len:])
                    code = self.dll.mdSend(self.path, self.st_no | (self.net_no*0x100), devi.dev_code.value,
                                           dev_no + f_len, byref(_size_renamed), byref(_buf))
        else:
            _size_renamed = c_short(size_renamed * 2 ** devi.dev_type.value)
            _buf = self.get_ctypes_by_list(buf)
            code = self.dll.mdSend(self.path, self.st_no | (self.net_no*0x100),
                                   devi.dev_code.value, dev_no, byref(_size_renamed), byref(_buf))
        return code

    def md_receive(self, devi: DeviceInfo, dev_no: int, size_renamed: int):
        '''
        Read MNETG
        :param devi: device
        :param dev_no: start address
        :param size_renamed: length
        :return: code,data
        '''
        if devi.dev_type == DevTypeEnum.Bit:
            _size_renamed = c_short(math.ceil(size_renamed/8))
            _buf = self.get_ctypes_by_length_bin(dev_no % 16 + size_renamed)
            code = self.dll.mdReceive(self.path, self.st_no | (self.net_no * 0x100), devi.dev_code.value,
                                      dev_no - dev_no % 16, byref(_size_renamed), byref(_buf))
            result = self.get_list_by_ctypes_bin(_buf, dev_no % 16, _size_renamed.value)
        else:
            _size_renamed = c_short(size_renamed * 2 ** devi.dev_type.value)
            _buf = self.get_ctypes_by_length(size_renamed)
            code = self.dll.mdReceive(self.path, self.st_no | (self.net_no*0x100), devi.dev_code.value,
                                      dev_no, byref(_size_renamed), byref(_buf))
            result = self.get_list_by_ctypes(_buf)
        return code, result

    def md_dev_set(self, devi: DeviceInfo, dev_no: int):
        '''
        Bit Set
        :param devi: device
        :param dev_no: start address
        :return: code
        '''
        code = self.dll.mdDevSet(self.path, self.st_no | (self.net_no*0x100), devi.dev_code.value, dev_no)
        return code

    def md_dev_rst(self, devi: DeviceInfo, dev_no: int):
        '''
        Bit Rset
        :param devi: device
        :param dev_no: start address
        :return: code
        '''
        code = self.dll.mdDevRst(self.path, self.st_no | (self.net_no*0x100), devi.dev_code.value, dev_no)
        return code

    def md_rand_w(self, dev: list, buf: list, buf_siz):
        _dev = self.get_ctypes_by_list(dev)
        _buf = self.get_ctypes_by_list(buf)
        code = self.dll.mdRandW(self.path, self.st_no | (self.net_no*0x100), _dev, _buf, buf_siz)
        return code, _buf.value

    def md_rand_r(self, dev: list, buf_siz):
        '''
        Rand Read
        :param dev: device list
        :param buf_siz: length
        :return: code,data
        '''
        _dev = self.get_ctypes_by_list(dev)
        _buf = self.get_ctypes_by_length(buf_siz)
        code = self.dll.mdRandR(self.path, self.st_no | (self.net_no*0x100), _dev, _buf, buf_siz)
        buf = self.get_list_by_ctypes(_buf)
        return code, buf

    def md_control(self, buf: int):
        code = self.dll.mdRandR(self.path, self.st_no | (self.net_no*0x100), buf)
        return code

    def md_type_read(self, buf: int):
        _buf = c_short(buf)
        code = self.dll.mdRandR(self.path, self.st_no | (self.net_no*0x100), _buf)
        return code, _buf.value

    def md_bd_led_read(self):
        pass

    def md_bd_mod_read(self):
        pass

    def md_bd_mod_set(self):
        pass

    def md_bd_rst(self):
        pass

    def md_bd_sw_read(self):
        pass

    def md_bd_ver_read(self):
        pass

    def md_init(self):
        pass

    def _md_batch_refresh_bit(self, devi: DeviceInfo, dev_no: int, buf: list):
        '''
        batch refresh bit
        :param devi: device
        :param dev_no: start address
        :param buf: data
        :return: code
        '''
        for i, _bit in zip(range(dev_no, dev_no + len(buf), 1), buf):
            if _bit:
                code = self.md_dev_set_ex(devi, i)
            else:
                code = self.md_dev_rst_ex(devi, i)
            if code != 0:
                return code
        return 0

    def md_wait_bd_event(self, event_no: int, timeout: int, signal_ed_no: int, details: int):
        _event_no = c_short(event_no)
        _signal_ed_no = c_short(signal_ed_no)
        _details = c_short(details)
        code = self.dll.mdWaitBdEvent(self.path, byref(_event_no), timeout, byref(_signal_ed_no), byref(_details))
        return code, _event_no.value, _signal_ed_no.value, _details.value

    def md_send_ex(self, devi: DeviceInfo, dev_no: int, size_renamed: int, buf: list):
        '''
        Write MNETG
        :param devi: device
        :param dev_no: start address
        :param size_renamed: length
        :param buf: data
        :return: code
        '''
        if devi.dev_type == DevTypeEnum.Bit:
            if size_renamed <= 8-dev_no % 8:
                return self._md_batch_refresh_bit(devi, dev_no, buf[:size_renamed])
            else:
                if dev_no % 8:
                    f_len = 8-dev_no % 8
                    code = self._md_batch_refresh_bit(devi, dev_no, buf[:f_len])
                else:
                    f_len = 0
                b_len = (dev_no+size_renamed+1) % 8
                if b_len > 1:
                    code = self._md_batch_refresh_bit(devi, dev_no + size_renamed + 1 - b_len,
                                                      buf[size_renamed - b_len + 1:])
                    m_len = size_renamed - b_len - f_len + 1
                    if m_len > 0:
                        _buf = self.get_ctypes_by_list_bin(
                            buf[f_len:m_len + f_len])
                        _size_renamed = c_short(m_len//8)
                        code = self.dll.mdSendEx(self.path, self.net_no, self.st_no, devi.dev_code.value,
                                                 dev_no + f_len, byref(_size_renamed), byref(_buf))
                else:
                    _size_renamed = c_short((size_renamed-f_len)//8)
                    _buf = self.get_ctypes_by_list_bin(buf[f_len:])
                    code = self.dll.mdSendEx(self.path, self.net_no, self.st_no, devi.dev_code.value,
                                             dev_no + f_len, byref(_size_renamed), byref(_buf))

        else:
            _size_renamed = c_short(size_renamed * 2 ** devi.dev_type.value)
            _buf = self.get_ctypes_by_list(buf)
            code = self.dll.mdSendEx(self.path, self.net_no, self.st_no, devi.dev_code.value,
                                     dev_no, byref(_size_renamed), byref(_buf))
        return code

    def md_receive_ex(self, devi: DeviceInfo, dev_no: int, size_renamed: int):
        '''
        Read MNETG
        :param devi: device
        :param dev_no: start address
        :param size_renamed: length
        :return: code,data
        '''
        if devi.dev_type == DevTypeEnum.Bit:
            _size_renamed = c_short(math.ceil(size_renamed/8))
            _buf = self.get_ctypes_by_length_bin(size_renamed + dev_no % 16)
            code = self.dll.mdReceiveEx(self.path, self.net_no, self.st_no, devi.dev_code.value,
                                        dev_no - dev_no % 16, byref(_size_renamed), byref(_buf))
            result = self.get_list_by_ctypes_bin(_buf, dev_no % 16, _size_renamed.value)
        else:
            _size_renamed = c_short(size_renamed * 2 ** devi.dev_type.value)
            _buf = self.get_ctypes_by_length(size_renamed)
            code = self.dll.mdReceiveEx(self.path, self.net_no, self.st_no, devi.dev_code.value,
                                        dev_no, byref(_size_renamed), byref(_buf))
            result = self.get_list_by_ctypes(_buf)
        return code, result

    def md_dev_set_ex(self, devi: DeviceInfo, dev_no: int):
        '''
        Bit Set
        :param devi: device
        :param dev_no: start address
        :return: code
        '''
        code = self.dll.mdDevSetEx(self.path, self.net_no, self.st_no, devi.dev_code.value, dev_no)
        return code

    def md_dev_rst_ex(self, devi: DeviceInfo, dev_no: int):
        '''
        Bit Rset
        :param devi: device
        :param dev_no: start address
        :return: code
        '''
        code = self.dll.mdDevRstEx(self.path, self.net_no, self.st_no, devi.dev_code.value, dev_no)
        return code

    def md_rand_w_ex(self, dev: list, buf_siz: int):
        _dev = self.get_ctypes_by_list(dev)

        _buf = self.get_ctypes_by_length(buf_siz)
        code = self.dll.mdRandWEx(self.path, self.net_no, self.st_no, _dev, _buf, buf_siz)
        buf = self.get_list_by_ctypes(_buf)
        return code, buf

    def md_rand_r_ex(self, dev: list, buf: list, buf_siz: int):
        _dev = self.get_ctypes_by_list(dev)
        _buf = self.get_ctypes_by_list(buf)
        code = self.dll.mdRandREx(self.path, self.net_no, self.st_no, _dev, _buf, buf_siz)
        return code, _buf.value

    def md_rem_buf_write_ex(self, addr_ex: int, buf_size: int, buf: list):
        _buf_size = c_int(buf_size)
        _buf = self.get_ctypes_by_list(buf)
        code = self.dll.mdRemBufWriteEx(self.path, self.net_no, self.st_no, addr_ex, byref(_buf_size), byref(_buf))
        return code

    def md_rem_buf_read_ex(self, addr_ex: int, buf_size: int):
        _buf_size = c_int(buf_size)
        _buf = self.get_ctypes_by_length(buf_size)
        code = self.dll.mdRemBufReadEx(self.path, self.net_no, self.st_no, addr_ex, byref(_buf_size), byref(_buf))
        return code, self.get_list_by_ctypes(_buf)



