from telebot.types import Message

from keyboards.general import main_keyboard, all_chanels_markup
from dispatcher import bot, db
from i18n import START_MESSAGE


@bot.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await bot.reply_to(message, START_MESSAGE,
                       reply_markup=main_keyboard())
    
    db.writeUser(message.from_user)


@bot.message_handler(state="*", commands=['cancel'])
async def cancel(message: Message):
    await bot.delete_state(message.from_user.id, message.chat.id)
    await bot.send_message(message.chat.id, "Дія була припинена",
                       reply_markup=main_keyboard())
            

@bot.message_handler(text = "Підтримка 💁‍♂️")
async def help_message(message: Message):
    await bot.send_message(message.chat.id,"Корисні посилання:", reply_markup=all_chanels_markup())


#купіть слона