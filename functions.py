from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from aiogram.filters import Command

from buttons import profile_btn, buy_menu_btn

router = Router()


users = {}


@router.message(Command("start"))
async def start_cmd(message: Message):
    users.setdefault(message.from_user.id, {
        "name": message.from_user.full_name,
        "balance": 0
    })
    await message.answer("Xush kelibsiz!")


@router.message(Command("profile"))
async def profile_cmd(message: Message):
    user = users.get(message.from_user.id)

    if not user:
        await message.answer("Siz ro'yxatdan o'tmagansiz. /start buyrug'ini bering.")
        return

    await message.answer(
        f"👤 {user['name']}\n"
        f"🆔 ID: {message.from_user.id}\n"
        f"💎 Balance: {user['balance']}",
        reply_markup=profile_btn()
    )


@router.callback_query(F.data == "buy")
async def buy_menu(callback: CallbackQuery):
    await callback.message.answer(
        "Nechta olmos?",
        reply_markup=buy_menu_btn()
    )


@router.callback_query(F.data.startswith("pay_"))
async def pay(callback: CallbackQuery, bot: Bot):
    count = int(callback.data.split("_")[1])
    stars = count * 2

    await bot.send_invoice(
        chat_id=callback.from_user.id,
        title="Olmos",
        description=f"{count} ta olmos",
        payload=f"diamond_{count}",
        provider_token="",
        currency="XTR",
        prices=[LabeledPrice(label="olmos", amount=stars)]
    )


@router.pre_checkout_query()
async def pre_checkout(q: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(q.id, ok=True)


@router.message(F.successful_payment)
async def success(message: Message):
    count = int(message.successful_payment.invoice_payload.split("_")[1])
    users[message.from_user.id]["balance"] += count

    await message.answer(f"✅ Tolov amalga oshdi sizga +{count}💎 qoshildi")
