import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# تنظیمات اصلی
API_TOKEN = '7800792594:AAFq17u9oVnP-p3N0ksLPI-tzFPxrs4uDoU'
GROUP_CHAT_ID = -4642492016  # آی‌دی گروه واحد مالی

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# حافظه موقت برای ذخیره اطلاعات کاربران
user_data = {}

# منوی اصلی
def main_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📤 رسیدهای پرداختی", callback_data="payment_receipt")],
        [InlineKeyboardButton(text="📥 رسیدهای دریافت", callback_data="receive_receipt")],
        [InlineKeyboardButton(text="💰 دریافتی‌ها از مشتریان", callback_data="customer_receipt")]
    ])
    return keyboard

# هندلر برای فرمان /start
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("سلام! لطفاً بخش مورد نظر خود را انتخاب کنید:", reply_markup=main_menu())

# هندلر برای کلیک روی دکمه‌ها
@dp.callback_query()
async def handle_menu(call: types.CallbackQuery):
    user_id = call.from_user.id
    if call.data == "payment_receipt":
        user_data[user_id] = {'step': 1, 'type': 'payment'}
        await call.message.edit_text("لطفاً عکس‌های رسید پرداختی خود را ارسال کنید.")
    elif call.data == "receive_receipt":
        user_data[user_id] = {'step': 1, 'type': 'receive'}
        await call.message.edit_text("لطفاً عکس‌های رسید دریافت خود را ارسال کنید.")
    elif call.data == "customer_receipt":
        user_data[user_id] = {'step': 1, 'type': 'customer'}
        await c
