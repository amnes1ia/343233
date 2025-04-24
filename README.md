
# Telegram Бот для Канала

Этот бот автоматически оставляет сообщение под каждым новым постом в канале Telegram с кнопкой "📜 Правила".

## 📦 Что внутри
- `bot.py` — основной код бота
- `requirements.txt` — зависимости
- `README.md` — как запускать

## 🚀 Как запустить на Render

1. Создай GitHub-репозиторий и залей эти файлы
2. Перейди на [https://render.com](https://render.com)
3. Нажми **"New" → "Background Worker"**
4. Подключи свой репозиторий
5. В настройках укажи:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`
   - **Instance Type**: Free

Готово! Бот будет активен 24/7 ✨
