from dotenv import load_dotenv
from os import getenv


from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode


from .routers import default_router, jokes_router

load_dotenv()

root_router = Router()
root_router.include_routers(default_router, jokes_router, )


async def main() -> None:

    token = getenv("BOT_TOKEN")

    bot = Bot(token, parse_mode=ParseMode.HTML)

    dp = Dispatcher()
    dp.include_router(root_router)

    await dp.start_polling(bot)


