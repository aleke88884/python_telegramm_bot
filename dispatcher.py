from main import bot, dp

from aiogram.types import Message
from config import id

async  def send_to_admin(dp):
    await  bot.send_message(chat_id=id, text="Hello!""\nWhat's your name")

@dp.message_handler()
async def echo(message:Message):
    if(message.text=="Alnur"):
        text = f"Salem ,{message.text} "
        await bot.send_message(chat_id=message.from_user.id, text=text)
        text = f"How are you {message.text} "
        await bot.send_message(chat_id=message.from_user.id,text=text)
    if(message.text=="Nice"):
        text = f"Cool"
        await bot.send_message(chat_id=message.from_user.id,text=text)
    elif(message.text=="Good"):
        text = f"Nice "
        await bot.send_message(chat_id=message.from_user.id, text=text)
    elif (message.text == "Bad"):
        text = f"Please be funny "
        await bot.send_message(chat_id=message.from_user.id, text=text)
        text = f"What was happen with you?"
        await bot.send_message(chat_id=message.from_user.id, text=text)
    if (message.text == "Nothing"):
        text = f"mmm ok i will go back soon"
        await bot.send_message(chat_id=message.from_user.id,text = text)