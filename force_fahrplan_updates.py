﻿#!/usr/bin/python3
# -*- coding: utf-8 -*-

#==============================================================================
# This script removes all schedule versions from the database which causes the
# schedule update script to import every schedule again
#==============================================================================

import os
import sys
from lxml import etree
from urllib import request

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "subtitleStatus.settings")

import django
django.setup()
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist

from www.models import Event

all_events = Event.objects.all()

for every_event in all_events:
    every_event.schedule_version = "force update"
    every_event.save()

print("Alle Fahrplanversionen zurück gesetzt!")
