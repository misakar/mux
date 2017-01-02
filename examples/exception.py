import logging
from mux import MuxStreamHandler

# setup
logger = logging.getLogger(__name__)
handler = MuxStreamHandler()
handler.setLevel(logging.ERROR)
logger.addHandler(handler)
logger.setLevel(logging.ERROR)

# use
try:
    x = 1 / 0
except ZeroDivisionError as e:
    logger.exception('ZeroDivisionError: %s', e)
