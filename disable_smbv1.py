#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: Hrvoje T.
Date: June, 2017.

This script disables SMBv1 protocol in Windows
by editing registry key.

# HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters
# Registry entry: SMB1 REG_DWORD: 0 = Disabled
"""

import winreg


key = winreg.OpenKey(
        winreg.HKEY_LOCAL_MACHINE,
        'SYSTEM\\CurrentControlSet\\Services\\lanmanserver\\parameters', 0,
        winreg.KEY_SET_VALUE)
winreg.SetValueEx(
        key, 'SMB1', 0, winreg.REG_DWORD, 0)
key.Close()


#import _winreg as wreg
#key = wreg.CreateKey(wreg.HKEY_LOCAL_MACHINE, "Software\\TestCompany\\TestProject")
## Create new subkey
#wreg.SetValue(key, 'NewSubkey', wreg.REG_SZ, 'testsubkey')
#print wreg.QueryValue(key, 'NewSubKey')
## prints 'testsubkey'
## Create new value
#wreg.SetValueEx(key, 'ValueName', 0, wreg.REG_SZ, 'testvalue')
#print wreg.QueryValueEx(key,'ValueName')
## prints (u'testvalue', 1)
#key.Close()