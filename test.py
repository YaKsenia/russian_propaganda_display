#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:40:51 2024

@author: ksenia
"""

from scrape_1_channel import translate

with open('new.txt', 'r') as file:
    data = file.read().replace('\n', '')
    translation = translate(data)
    print(translation)
    print(len(translation))