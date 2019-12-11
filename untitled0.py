import temp as z
from telebot import TeleBot,types
bot = TeleBot('999864039:AAF1fo6sqEN6KuBzwQvjVV9qhmaXwhJg6A4')

def show_zodiac_thing(message):
    keyboard = types.InlineKeyboardMarkup()
    
    for zod in z.zods:
        key_zod = types.InlineKeyboardButton(text=zod, callback_data='zodiac')
        keyboard.add(key_zod)
    
    bot.send_message(message.from_user.id, 'text', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == r'\hello':
        bot.send_message(message.from_user.id, 'test')
        show_zodiac_thing(message)
    elif message.text == r'\help':
        bot.send_message(message.from_user.id, r'type \hello')
    else:
        bot.send_message(message.from_user.id, r'type \help')
        
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'zodiac':
        msg = z.get_predictions()
        bot.send_message(call.message.chat.id, msg)



       
bot.polling(none_stop=True, interval=0)