from telebot.types import Message

from keyboards.general import main_keyboard, all_chanels_markup
from misc.announcements_method import send_announcement
from dispatcher import bot, db

@bot.message_handler(text = "Мої запити 📝")
async def my_requests(message: Message):
    requests = db.get_user_requests(message.chat.id)
    if requests:
        await bot.send_message(message.chat.id, 'Ваші запити:')
        for request in requests:
            qwery = f'{message.from_user.id}.{request}'
            await send_announcement(bot, message.chat.id, request)
    else:
        await bot.send_message(message.chat.id, 'У вас немає запитів')
