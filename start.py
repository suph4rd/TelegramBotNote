import os

from aiogram import Bot, Dispatcher, executor, types
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'TelegramBotNote.settings'
django.setup()
from django.conf import settings
from asgiref.sync import sync_to_async
from core.models import Note


bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome to the club! It's NB4444 bot, made by Andrey Bernyak!")


@dp.message_handler()
async def main_handler(message: types.Message):
    await sync_to_async(Note.objects.create)(text=message.text)
    await message.answer("Your message saved successful!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
