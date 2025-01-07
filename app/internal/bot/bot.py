import aiogram
import asyncio
test_router = aiogram.Router()

class TgBot:
	__bot: aiogram.Bot = None
	__dispatcher: aiogram.Dispatcher = None

	def __init__(self):
		pass


	def get_bot(self) -> aiogram.Bot:
		if self.__bot is None:
			self.__bot = aiogram.Bot(token="TOKEN")
			return self.__bot

		return self.__bot

	def get_dispatcher(self) -> aiogram.Dispatcher:
		if self.__dispatcher is None:
			self.__dispatcher = aiogram.Dispatcher()
			self.__dispatcher.include_routers(
				aiogram.Router(),
				aiogram.Router()
			)
		return self.__dispatcher




	def send_message(self):
		"""Для отправки сообщений"""
		pass

	async def startup_bot(self):
		await self.get_dispatcher().start_polling(bot=self.get_bot())

if __name__ == "__main__":
	bot = TgBot()

	asyncio.run(bot.startup_bot())