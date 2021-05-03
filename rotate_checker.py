import logging

logger = logging.getLogger(__name__)


def check_rotate_log():
    for x in range(1, 1000):
        logger.debug('Debug message %d', x)
        logger.info('Info message %d', x)
