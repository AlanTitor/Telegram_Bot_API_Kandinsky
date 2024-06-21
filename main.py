import base64
import telebot
import datetime


from ClassImgGenerate import Text2ImageAPI
from Global_Variables import *

bot = telebot.TeleBot(BOT_TOKEN)


def generate_image_bot(prompt, style="No style"):
    if __name__ == '__main__':
        api = Text2ImageAPI(URL, API_KEY, SECRET_KEY)
        model_id = api.get_model()
        uuid = api.generate(prompt, model_id, style)
        images = api.check_generation(uuid)

        image_base64 = images[0]
        image_data = base64.b64decode(image_base64)
        return image_data


@bot.message_handler(commands=['gen'])
def get_message(message):
    prompt = message.text
    if len(prompt) <= 4:
        return
    if prompt == prompt.find("."):
        style = prompt[5::prompt.count(".")]
        prompt = prompt[prompt.count(".")::]
        photo = generate_image_bot(prompt, style)
        current_time = datetime.datetime.now().time()
        print(f"Style - {style}, Prompt - {prompt}, Time - {current_time}")
        bot.send_photo(chat_id=message.chat.id, photo=photo)
    else:
        prompt = prompt[5::]
        photo = generate_image_bot(prompt)
        current_time = datetime.datetime.now().time()
        print(f"Style - NoN, Prompt - {prompt}, Time - {current_time}")
        bot.send_photo(chat_id=message.chat.id, photo=photo)


@bot.message_handler(commands=['sty'])
def get_style(message):
    list = {"Detailed photo": "Детальное фото",
            "Anime": "Аниме"}
    bot.send_message(chat_id=message.chat.id, text=str(list))


bot.infinity_polling()
