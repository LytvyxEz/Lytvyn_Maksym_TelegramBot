from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
from ..data import get_joke
from ..utils import edit_or_answer

jokes_router = Router()


@jokes_router.message(Command("jokes"))
async def jokes(message: Message):
    while True:
        joke = await get_joke()
        await edit_or_answer(
            message,
            f"Catch ur today joke:\n "
            f"\n"
            f" {joke}",
        )
        await asyncio.sleep(24 * 60 * 60)


@jokes_router.message(Command("joke"))
async def jokes(message: Message):
    joke = await get_joke()
    await edit_or_answer(
        message,
        f"Catch ur joke:\n "
        f"\n"
        f" {joke}",
    )
