import os
import retriever

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='TELEGRAM_BOT_TOKEN_HERE')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
        await message.reply("Hi!\n\nI'm UiTinLeuvenBot!\n\nYour gateway to enjoying the wonderous glories of Leuven.\n\nFor me to help you with today's happenings, send me a category or a search term (/categories or /search <term>)\n\n")

@dp.message_handler(commands=['free_concerts', ])
async def send_free_concerts(message: types.Message):
        await message.reply(retriever.getEvents('https://www.uitinvlaanderen.be/agenda/search/rss?facet%5Bdatetype%5D%5B0%5D=today&facet%5Bcategory_eventtype_id%5D%5B0%5D=0.50.4.0.0&facet%5Bcategory_flandersregion_id%5D%5B0%5D=reg.16&gratis=1'))

@dp.message_handler(commands=['free_fitness', ])
async def send_free_fitness(message: types.Message):
        await message.reply(retriever.getEvents('https://www.uitinvlaanderen.be/agenda/search/rss?facet%5Bdatetype%5D%5B0%5D=today&facet%5Bcategory_eventtype_id%5D%5B0%5D=0.59.0.0.0&facet%5Bcategory_flandersregion_id%5D%5B0%5D=reg.16&gratis=1'))

@dp.message_handler(commands=['categories', ])
async def send_categories(message: types.Message):
        await message.reply(retriever.getCategories())

@dp.message_handler(regexp='search *')
async def send_search(message: types.Message):
        await message.reply(retriever.getSearch(message.text))

if __name__ == '__main__':
        executor.start_polling(dp)