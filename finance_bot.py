from aiogram import Bot, Dispatcher, types
import logging
import asyncio
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command

# تنظیمات لاگ‌ها برای بررسی مشکلات
logging.basicConfig(level=logging.INFO)

# توکن ربات تلگرام خود را اینجا وارد کنید
API_TOKEN = '7800792594:AAFq17u9oVnP-p3N0ksLPI-tzFPxrs4uDoU'

# آیدی گروه خود را اینجا وارد کنید
GROUP_ID = '-4642492016'

# ایجاد شی Bot
bot = Bot(token=API_TOKEN)

# استفاده از MemoryStorage برای ذخیره‌سازی داده‌ها
storage = MemoryStorage()

# ایجاد Dispatcher بدون ارسال bot
dp = Dispatcher(storage=storage)

# دستور /start برای خوشامدگویی به کاربر
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply("سلام! ربات شما آماده است. برای ارسال پیام به گروه، فقط اینجا پیام ارسال کنید.")

# ارسال پیام به گروه زمانی که کاربر پیامی ارسال می‌کند
@dp.message()
async def forward_message_to_group(message: types.Message):
    # ارسال پیام به گروه
    await bot.send_message(GROUP_ID, message.text)

# راه اندازی ربات با asyncio
async def on_start():
    # storage را هنگام start_polling به Dispatcher ارسال می‌کنیم
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(on_start())
