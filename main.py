import os
import requests

BOT_TOKEN = os.getenv("")  # Токен бота (скрыт в настройках)
CHANNEL_USERNAME = "https://t.me/ArtNeir0"  # Например, "@art_neuro"

# Создаем кнопку для подписки
keyboard = {
    "inline_keyboard": [[
        {
            "text": "🚀 ПОДПИСАТЬСЯ",
            "url": f"tg://resolve?domain={CHANNEL_USERNAME.replace('@', '')}"
        }
    ]]
}

# Текст сообщения
message = "🎨 **Арты нейросетей каждый день!**\nЖми кнопку и забирай крутые обои! 👇"

# Отправляем сообщение через API Telegram
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
params = {
    "chat_id": CHANNEL_USERNAME,
    "text": message,
    "reply_markup": keyboard,
    "parse_mode": "Markdown"
}

response = requests.post(url, json=params)
print("Результат:", response.status_code)
