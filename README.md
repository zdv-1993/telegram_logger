#### Необходимо определить 2 переменных окружения
1. TELEGRAM_LOGGER_TOKEN
2. TELEGRAM_LOGGER_CHAT_IDS


#### Получить chat_id `curl https://api.telegram.org/bot{ваш токен}/getUpdates`

#### 2 варианта настройки логгера:
1. ```
   import logging
   from telegram_log import TelegramHandler
   
   logger = logging.getLogger(__name__)
   logger.addHandler(TelegramHandler())
2. ```
   import logging
   from telegram_log import BASE_LOGGING_CONFIG
   
   logging.config.dictConfig(BASE_LOGGING_CONFIG)
   logger = logging.getLogger(__name__)

    
