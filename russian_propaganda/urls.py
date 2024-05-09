#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 20:33:15 2024

@author: ksenia
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.title_list, name='title_list'),
]