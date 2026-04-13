#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8353176536:AAHonA4GEyuctgPSq2WnGArKcYCV0yKINqc")
    API_ID = int(os.environ.get("API_ID", "37813625"))
    API_HASH = os.environ.get("API_HASH", "f4483e5f1a61d19f27072aa81551859d")
    AUTH_USERS = "6134299100"

