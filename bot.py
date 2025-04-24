
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# 🔐 Токен твоего бота
TOKEN = '7910010935:AAE1pqIVlsqWf1YeI9vr5WMal2MeYWQOmAE'

# 📢 Название твоего канала (обязательно с @)
CHANNEL_ID = '@amnezijchik'  # замени на своё, если нужно

# 📨 Сообщение, которое бот будет оставлять
MESSAGE = "⏬ Перед написанием сообщения прочитайте Правила! ⏬\n👍🌐"

# 📜 Полный текст правил (будет отправлен в отдельном сообщении по команде или по ссылке)
RULES_TEXT = """
📌 <b>Общие правила:</b>

1️⃣ Будьте вежливы и уважительны – оскорбления, дискриминация, токсичное поведение запрещены.  
2️⃣ Любые проявления ненависти, расизма, сексизма и травли строго запрещены.  
3️⃣ Без политики и религии – чтобы избежать конфликтов, не обсуждаем спорные темы.  
4️⃣ Не спамить и не флудить – многократное повторение сообщений, капс-лок и бессмысленные символы запрещены.  
5️⃣ Легкие подколы и шуточные оскорбления (без злого умысла) разрешены, но если кто-то просит прекратить – останавливаемся.  

📌 <b>Для текстового чата:</b>

6️⃣ Запрещена реклама и самопиар – не продвигаем свои каналы, проекты или сторонние ресурсы без разрешения.  
7️⃣ Не обсуждаем пермабан и модерацию – если есть вопросы по блокировке, обращайтесь в личные сообщения модераторам.  
8️⃣ Без NSFW-контента – запрещены непристойные изображения, сообщения и шутки 18+.  

📌 <b>Для голосового чата:</b>

9️⃣ Говорим по очереди – не перебиваем других, даем возможность всем высказаться.  
🔟 Без громких звуков и фонового шума – используйте наушники и микрофон с шумоподавлением.  
🔈 Запрещены звуковые эффекты и голосовые изменения – любые искажения голоса или саундпады запрещены.  

🔄 Администрация оставляет за собой право изменять правила без предварительного уведомления.  
⚠️ Нарушение правил может привести к муту, кику или бану.  
💖 Уважайте друг друга и наслаждайтесь общением!
"""

def handle_new_post(update: Update, context: CallbackContext):
    if update.channel_post:
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("📜 Правила / Rules", callback_data='show_rules')]
        ])
        context.bot.send_message(
            chat_id=CHANNEL_ID,
            text=MESSAGE,
            reply_to_message_id=update.channel_post.message_id,
            reply_markup=keyboard
        )

def handle_button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == 'show_rules':
        query.answer()
        query.message.reply_text(RULES_TEXT, parse_mode='HTML', disable_web_page_preview=True)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.update.channel_posts, handle_new_post))
dp.add_handler(MessageHandler(Filters.callback_query, handle_button_click))

print("Бот запущен и следит за новыми постами...")
updater.start_polling()
updater.idle()
