from googletrans import Translator
import logging

from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN


translator = Translator()

# Configure logging
logging.basicConfig(level=logging.INFO)

# ADMIN = 5627225073

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

my_users = []


@dp.message_handler(commands=['start'])
async def first_message(msg: types.message):    
    if msg.from_user.id not in my_users:
        my_users.append(msg.from_user.id)
        # await bot.send_message(chat_id=ADMIN, text=f"Botda yangi odam:{msg.from_user.full_name}. Bazada {len(my_users)}")
    await msg.reply("Bizning botimizga hush kelibsiz. Bu bot auto tarjimon 😊😊😊")
    print(my_users)


@dp.message_handler(commands=['help'])
async def help_message(msg: types.message):
    await msg.reply("BU BOT:\n🇺🇿>🇺🇸\n🇺🇸>🇺🇿\n🇷🇺>🇺🇸\nSHU TILLAR ARO TARJIMA QILADI(Qoshiladi)")


@dp.message_handler(content_types=types.ContentType.ANY)
async def answer_user(msg: types.Message):
        
        #ADMIN MENU
    # if msg.from_user.id == ADMIN:
    #     for user in my_users:
    #         # await bot.send_message(chat_id=user, text=msg.text)

    #         # FORWARD
    #         # await bot.forward_message(chat_id=user, from_chat_id=ADMIN, message_id=msg.message_id)
    #         await bot.copy_message(chat_id=user, from_chat_id=ADMIN, message_id=msg.message_id)
    # else:

        """LANGUES"""
        til = translator.detect(msg.text)
        print()
        if til.lang == 'en':
            tarjima_soz = translator.translate(msg.text, dest='uz')
        elif til.lang == 'uz':
            tarjima_soz = translator.translate(msg.text, dest='en')
        elif til.lang == 'ru':
            tarjima_soz = translator.translate(msg.text, dest='en')
        # elif til.lang == '':
        #     tarjima_soz = translator.translate(msg.text, dest='en')
        else:
            tarjima_soz = translator.translate(msg.text, dest='uz')

        await msg.reply(tarjima_soz.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
