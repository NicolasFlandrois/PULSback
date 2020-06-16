#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Nicolas Flandrois
# Date:   Tue 16 June 2020 11:16:40
# Last Modified time: Tue 16 June 2020 12:06:22 

# Description:"""
WSGI config for backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()
