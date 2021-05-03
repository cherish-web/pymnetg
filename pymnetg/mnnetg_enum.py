# _*_ coding: utf-8 _*_
# @Time : 2021/4/28 上午 09:07 
# @Author : cherish_peng
# @Email : 1058386071@qq.com 
# @File : mnnetg_enum.py
# @Software : PyCharm
from enum import Enum


class ChanEnum(Enum):
    MEL_SEC_NET_H1 = 51
    MEL_SEC_NET_H2 = 52
    MEL_SEC_NET_H3 = 53
    MEL_SEC_NET_H4 = 54
    CC_Link_1 = 81
    CC_Link_2 = 82
    CC_Link_3 = 83
    CC_Link_4 = 84
    CC_Link_IE_Controller_1 = 151
    CC_Link_IE_Controller_2 = 152
    CC_Link_IE_Controller_3 = 153
    CC_Link_IE_Controller_4 = 154
    CC_Link_IE_Field_1 = 181
    CC_Link_IE_Field_2 = 182
    CC_Link_IE_Field_3 = 183
    CC_Link_IE_Field_4 = 184





class DevTypeEnum(Enum):
    Bit = 0
    Word = 1
    DoubleWord = 2


class DevCodeEnum(Enum):
    X = 1
    Y = 2
    L = 3
    M = 4
    SM = 5
    F = 6
    TT = 7
    TC = 8
    TN = 11
    CT = 9
    CC = 10
    CN = 12
    STT = 26
    STC = 27
    STN = 35
    D = 13
    SD = 14
    A = 19
    V = 20
    Z = 21
    R = 22
    B = 23
    W = 24
    SB = 25
    SW = 28
    QV = 30
    RWw = 36
    RWr = 37
    LZ = 38
    RD = 39
    LTT = 41
    LTC = 42
    LTN = 43
    LCT = 44
    LCC = 45
    LCN = 46
    LSTT = 47
    LSTC = 48
    LSTN = 49
    ER = 22000
    TM = 15
    TS = 16
    TS2 = 16002
    TS3 = 16003
    CM = 17
    CS = 18
    CS2 = 18002
    CS3 = 18003
    OBM = 50
    SEND_RECV = 101








