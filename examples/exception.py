import logging
from mux import muxStreamHandler

# setup
logger = logging.getLogger(__name__)
handler = muxStreamHandler()
handler.setLevel(logging.ERROR)
logger.addHandler(handler)
logger.setLevel(logging.ERROR)

# use
try:
    x = 1 / 0
except ZeroDivisionError as e:
    logger.exception('ZeroDivisionError: %s', e)
