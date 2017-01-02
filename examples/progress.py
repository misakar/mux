import os
import time
import logging
from mux import MuxStreamHandler, mux_progressbar, mux_format

logger = logging.getLogger(__name__)
handler = MuxStreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

@mux_progressbar(logger=logger,
                 start="init start",
                 end="init done")
def init():
    time.sleep(5)
    try:
        os.mkdir('./magic')
    except OSError as e:
        logger.exception('{path} already exist'.format(
            path=mux_format(os.getcwd(), 'green', 'underline')))

if __name__ == '__main__':
    init()