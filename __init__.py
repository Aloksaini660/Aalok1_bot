from telethon import TelegramClient
import logging
import time


api_id="1125689"
api_hash="4772d1792ed194020a8fb06a91ffb8fa"
bot_token="6160964410:AAHc0xMbEszbtUHN0R9g42W7Gbm1FOYXlhQ"

bot = TelegramClient("Aalok", api_id, api_hash).start(bot_token = bot_token)