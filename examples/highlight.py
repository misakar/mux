import os
import logging
from mux import MuxStreamHandler, mux_format

logger = logging.getLogger(__name__)
handler = MuxStreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info("your current path is {path}".format(
    path=mux_format(os.getcwd(), "red", "underline")))
logger.warning("be careful")