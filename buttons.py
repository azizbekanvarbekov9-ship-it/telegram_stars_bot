from mailbox import Message

from aiogram.utils.keyboard import InlineKeyboardBuilder


def profile_btn():
    kb = InlineKeyboardBuilder()
    kb.button(text="💎 Hisobni toldirish", callback_data="buy")
    return kb.as_markup()


def buy_menu_btn():
    kb = InlineKeyboardBuilder()

    for i in range(1, 11):
        kb.button(text=f"{i*2}⭐ = {i}💎", callback_data=f"pay_{i}")

    kb.adjust(2)
    return kb.as_markup()
async def come_back(message: Message):
    return InlineKeyboardBuilder().button(text="Profil ga qaytish", callback_data="come_back profile").as_markup()
