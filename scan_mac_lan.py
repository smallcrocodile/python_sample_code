#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Filename: scan_mac_lan.py
# -------------------------------------------------------------------------------
# Name:        [scan_mac]
# Purpose: 通过scapy获取局域网所有主机mac地址
# Author:      [ZhouKe]
# Created:     2014 -11 -11
# Copyright:   (c) ZhouKe 2014
# Licence:     <GPL>
# -------------------------------------------------------------------------------

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from scapy import srp, Ether, ARP, conf
import scapy


ipscan = '192.168.1.1/24'
try:
    ans, unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF") / ARP(pdst=ipscan), timeout=2, verbose=False)
except Exception, e:
    print str(e)
else:
    for snd, rcv in ans:
        list_mac = rcv.sprintf("%Ether.src% - %ARP.psrc%")
        print list_mac