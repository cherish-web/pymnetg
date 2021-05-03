# _*_ coding: utf-8 _*_
# @Time : 2021/4/28 上午 11:05 
# @Author : cherish_peng
# @Email : 1058386071@qq.com 
# @File : mnetg_device.py
# @Software : PyCharm
from .mnnetg_enum import *


class DeviceInfo:
    def __init__(self, dev_name, dev_code: DevCodeEnum, dev_type: DevTypeEnum):
        self.dev_name = dev_name
        self.dev_code = dev_code
        self.dev_type = dev_type


class Device:
    X = DeviceInfo(DevCodeEnum.X.name, DevCodeEnum.X, DevTypeEnum.Bit)
    Y = DeviceInfo(DevCodeEnum.Y.name, DevCodeEnum.Y, DevTypeEnum.Bit)
    L = DeviceInfo(DevCodeEnum.L.name, DevCodeEnum.L, DevTypeEnum.Bit)
    M = DeviceInfo(DevCodeEnum.M.name, DevCodeEnum.M, DevTypeEnum.Bit)
    SM = DeviceInfo(DevCodeEnum.SM.name, DevCodeEnum.SM, DevTypeEnum.Bit)
    F = DeviceInfo(DevCodeEnum.F.name, DevCodeEnum.F, DevTypeEnum.Bit)
    TT = DeviceInfo(DevCodeEnum.TT.name, DevCodeEnum.TT, DevTypeEnum.Bit)
    TC = DeviceInfo(DevCodeEnum.TC.name, DevCodeEnum.TC, DevTypeEnum.Bit)
    TN = DeviceInfo(DevCodeEnum.TN.name, DevCodeEnum.TN, DevTypeEnum.Word)
    CT = DeviceInfo(DevCodeEnum.CT.name, DevCodeEnum.CT, DevTypeEnum.Bit)
    CC = DeviceInfo(DevCodeEnum.CC.name, DevCodeEnum.CC, DevTypeEnum.Bit)
    CN = DeviceInfo(DevCodeEnum.CN.name, DevCodeEnum.CN, DevTypeEnum.Word)
    STT = DeviceInfo(DevCodeEnum.STT.name, DevCodeEnum.STT, DevTypeEnum.Bit)
    STC = DeviceInfo(DevCodeEnum.STC.name, DevCodeEnum.STC, DevTypeEnum.Bit)
    STN = DeviceInfo(DevCodeEnum.STN.name, DevCodeEnum.STN, DevTypeEnum.Word)
    D = DeviceInfo(DevCodeEnum.D.name, DevCodeEnum.D, DevTypeEnum.Word)
    SD = DeviceInfo(DevCodeEnum.SD.name, DevCodeEnum.SD, DevTypeEnum.Word)
    A = DeviceInfo(DevCodeEnum.A.name, DevCodeEnum.A, DevTypeEnum.Word)
    V = DeviceInfo(DevCodeEnum.V.name, DevCodeEnum.V, DevTypeEnum.Word)
    Z = DeviceInfo(DevCodeEnum.Z.name, DevCodeEnum.Z, DevTypeEnum.Word)
    R = DeviceInfo(DevCodeEnum.R.name, DevCodeEnum.R, DevTypeEnum.Word)
    B = DeviceInfo(DevCodeEnum.B.name, DevCodeEnum.B, DevTypeEnum.Bit)
    W = DeviceInfo(DevCodeEnum.W.name, DevCodeEnum.W, DevTypeEnum.Word)
    SB = DeviceInfo(DevCodeEnum.SB.name, DevCodeEnum.SB, DevTypeEnum.Bit)
    SW = DeviceInfo(DevCodeEnum.SW.name, DevCodeEnum.SW, DevTypeEnum.Word)
    QV = DeviceInfo(DevCodeEnum.QV.name, DevCodeEnum.QV, DevTypeEnum.Bit)
    RWw = DeviceInfo(DevCodeEnum.RWw.name, DevCodeEnum.RWw, DevTypeEnum.Word)
    RWr = DeviceInfo(DevCodeEnum.RWr.name, DevCodeEnum.RWr, DevTypeEnum.Word)
    LZ = DeviceInfo(DevCodeEnum.LZ.name, DevCodeEnum.LZ, DevTypeEnum.DoubleWord)
    RD = DeviceInfo(DevCodeEnum.RD.name, DevCodeEnum.RD, DevTypeEnum.Word)
    LTT = DeviceInfo(DevCodeEnum.LTT.name, DevCodeEnum.LTT, DevTypeEnum.Bit)
    LTC = DeviceInfo(DevCodeEnum.LTC.name, DevCodeEnum.LTC, DevTypeEnum.Bit)
    LTN = DeviceInfo(DevCodeEnum.LTN.name, DevCodeEnum.LTN, DevTypeEnum.DoubleWord)
    LCT = DeviceInfo(DevCodeEnum.LCT.name, DevCodeEnum.LCT, DevTypeEnum.Bit)
    LCC = DeviceInfo(DevCodeEnum.LCC.name, DevCodeEnum.LCC, DevTypeEnum.Bit)
    LCN = DeviceInfo(DevCodeEnum.LCN.name, DevCodeEnum.LCN, DevTypeEnum.DoubleWord)
    LSTT = DeviceInfo(DevCodeEnum.LSTT.name, DevCodeEnum.LSTT, DevTypeEnum.Bit)
    LSTC = DeviceInfo(DevCodeEnum.LSTC.name, DevCodeEnum.LSTC, DevTypeEnum.Bit)
    LSTN = DeviceInfo(DevCodeEnum.LSTN.name, DevCodeEnum.LSTN, DevTypeEnum.DoubleWord)
    ER = DeviceInfo(DevCodeEnum.ER.name, DevCodeEnum.ER, DevTypeEnum.Word)
    TM = DeviceInfo(DevCodeEnum.TM.name, DevCodeEnum.TM, DevTypeEnum.Word)
    TS = DeviceInfo(DevCodeEnum.TS.name, DevCodeEnum.TS, DevTypeEnum.Word)
    TS2 = DeviceInfo(DevCodeEnum.TS2.name, DevCodeEnum.TS2, DevTypeEnum.Word)
    TS3 = DeviceInfo(DevCodeEnum.TS3.name, DevCodeEnum.TS3, DevTypeEnum.Word)
    CM = DeviceInfo(DevCodeEnum.CM.name, DevCodeEnum.CM, DevTypeEnum.Word)
    CS = DeviceInfo(DevCodeEnum.CS.name, DevCodeEnum.CS, DevTypeEnum.Word)
    CS2 = DeviceInfo(DevCodeEnum.CS2.name, DevCodeEnum.CS2, DevTypeEnum.Word)
    CS3 = DeviceInfo(DevCodeEnum.CS3.name, DevCodeEnum.CS3, DevTypeEnum.Word)
    OBM = DeviceInfo(DevCodeEnum.OBM.name, DevCodeEnum.OBM, DevTypeEnum.Word)
    SEND_RECV = DeviceInfo(DevCodeEnum.SEND_RECV.name, DevCodeEnum.SEND_RECV, DevTypeEnum.Word)

