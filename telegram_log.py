import logging
from logging import Handler
import telebot
import os
from time import time, sleep


TELEGRAM_TOKEN_NAME_ENV = 'TELEGRAM_LOGGER_TOKEN'
TELEGRAM_LOGGER_CHAT_IDS_ENV = 'TELEGRAM_LOGGER_CHAT_IDS'
TELEGRAM_LOG_TIMEOUT = 30


class TelegramHandler(Handler):
    def __init__(self, *_, **__):
        assert os.environ.get(TELEGRAM_TOKEN_NAME_ENV), f'Environment variable "{TELEGRAM_TOKEN_NAME_ENV}" is not set!'
        assert os.environ.get(TELEGRAM_LOGGER_CHAT_IDS_ENV), f'Environment variable "{TELEGRAM_LOGGER_CHAT_IDS_ENV}" is not set!'
        super().__init__(*_, **__)
        self._telebot = telebot.TeleBot(os.environ[TELEGRAM_TOKEN_NAME_ENV])
        self._chat_ids = os.environ[TELEGRAM_LOGGER_CHAT_IDS_ENV].split(',')

    def emit(self, record):
        msg = self.format(record)
        for chat_id in self._chat_ids:
            t0 = time()
            while time() - t0 < TELEGRAM_LOG_TIMEOUT:
                try:
                    self._telebot.send_message(chat_id, msg, parse_mode="HTML")
                    break
                except Exception:
                    logging.exception("Exception while sending %s to %s:", msg, chat_id)
                    sleep(1)


BASE_LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            '()': TelegramHandler,
            'level': 'DEBUG',
            'formatter': 'default',
        }
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG'
    }
}
