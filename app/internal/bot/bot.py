import aiogram
import asyncio
from app.internal.bot.button import auth
from app.internal.bot.command import admin_command

from app.pkg.settings import settings

class TgBot:

    __bot: aiogram.Bot = None
    __dispatcher: aiogram.Dispatcher = None
    __counter = 0

    def get_bot(self) -> aiogram.Bot:
        if self.__bot is None:
            self.__bot = aiogram.Bot(token=settings.TELEGRAM.API_BOT_TOKEN)
        return self.__bot

    def get_dispatcher(self) -> aiogram.Dispatcher:
        if self.__dispatcher is None:
            self.__dispatcher = aiogram.Dispatcher()
            self.__dispatcher.include_routers(
                auth.router,
            )
        return self.__dispatcher

    def send_message(self):
        """Для отправки сообщений"""
        pass

    async def startup_bot(self):
        bot = self.get_bot()
        dispatcher = self.get_dispatcher()
        await dispatcher.start_polling(bot)
