from typing import Union
from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.utils.markdown import hbold
from ..utils import edit_or_answer

default_router = Router()


@default_router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    await state.clear()
    await edit_or_answer(
        message,
        f"Hello, {hbold(message.from_user.full_name)}, i am bot-joke."
        f" I will send for u jokes every 24 hours."
        f"\nU can check my list of commands, /help\n"
        "if u want to get jokes every 24 hours , use /jokes\n"
        "if u have problem , just restart the bot.\n"
        "P.s do not use /jokes more than 1 time, if u want get more than 1 joke every day, use /joke"

    )


@default_router.message(Command("about"))
async def about_handler(message: Message):
    descr = await message.bot.get_my_description()
    await edit_or_answer(
        message,
        descr.description,
        ReplyKeyboardRemove(),
    )


@default_router.message(Command("help"))
async def help_handler(message: Message):
    text = "Ось перелік моїх команд:"
    commands = await message.bot.get_my_commands()
    for command in commands:
        text += f"\n/{command.command} -> {command.description}"
    await edit_or_answer(
        message,
        text,
        ReplyKeyboardRemove(),
    )


@default_router.callback_query(F.data == "back")
@default_router.message(Command("back"))
async def back_handler(message: Union[Message, CallbackQuery], state: FSMContext) -> None:
    await state.clear()
    return await start_handler(message, state)


@default_router.message(Command("clear"))
async def clear_handler(message: Message, state: FSMContext):
    await state.clear()
    chat = message.chat
    _id = message.message_id
    while _id > 0:
        try:
            await chat.delete_message(_id)
            print(f"deleting {_id} message")
            _id -= 1
        except:
            break
