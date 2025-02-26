# Бот обратной связи для Telegram

Асинхронный бот для обратной связи с подписчиками телеграм канала.

## Особенности
- Асинхронная обработка сообщений
- Простой интерфейс для пользователей
- Удобное управление диалогами для администратора
- Поддержка приватных чатов с каждым пользователем

## Установка

1. Клонируйте репозиторий
2. Установите зависимости:
```bash
pip install -r requirements.txt
```
3. Скопируйте файл `.env.example` в `.env` и заполните необходимые переменные:
   - `BOT_TOKEN` - токен вашего бота (получите у @BotFather)
   - `ADMIN_ID` - ваш Telegram ID (можно узнать у @userinfobot)

## Запуск

```bash
python bot.py
```

## Использование

### Для пользователей
1. Начните диалог с ботом командой `/start`
2. Отправьте ваше сообщение
3. Ожидайте ответа администратора

### Для администратора
1. Вы будете получать все сообщения от пользователей
2. Для ответа используйте функцию "Ответить" в Telegram
3. Ваш ответ будет отправлен соответствующему пользователю 