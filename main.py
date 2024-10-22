import asyncio

from core.handlers import routers
from core.tools import get_token
from core.tools import UniversalLogger

from aiogram import Bot, Dispatcher

logger = UniversalLogger("bot_logs")


async def main():
    bot = Bot(get_token('TG_bot'))
    dp = Dispatcher()
    try:
        dp.include_routers(*routers)
        await dp.start_polling(bot)
        logger.info("Bot successfully started", extra="bot")
    except Exception as e:
        logger.error(f"An error occurred when the bot was running{e}", extra="bot")
    finally:
        await bot.close()


if __name__ == "__main__":
    asyncio.run(main())
