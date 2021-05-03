import json
import logging
from logging.handlers import RotatingFileHandler

from credentials import DISCORD_WEBHOOK, DISCORD_HOST

logging.basicConfig(
    level=logging.DEBUG,
    filename='./logs/program.log',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)

# Настраиваем логгер rotate
rotate_logger = logging.getLogger('rotate_checker')
rotate_logger.setLevel(logging.INFO)
rotate_handler = RotatingFileHandler(
    './logs/rotate.log', maxBytes=1000, backupCount=5)
rotate_logger.addHandler(rotate_handler)


# Настраиваем логгер http
class HTTPHandler(logging.handlers.HTTPHandler):
    def mapLogRecord(self, record):
        record = {'content': json.dumps(record.__dict__)}
        return record


http_logger = logging.getLogger('http_checker')
http_logger.setLevel(logging.INFO)
http_handler = HTTPHandler(
    DISCORD_HOST,
    DISCORD_WEBHOOK,
    method='POST',
    secure=True,
)
http_logger.addHandler(http_handler)
http_handler.propagate = False
