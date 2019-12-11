#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:45:28 2019

@author: nmazgaleev
"""

from cryptography.fernet import Fernet

file = open('key.key', 'rb')
key = file.read()
file.close()

with open('Nmazgaleev.txt.encrypted', 'rb') as f:
    data = f.read()
    
fernet = Fernet(key)
decrypted = fernet.decrypt(data)
print(decrypted)