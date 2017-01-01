import logging
from mux import muxStreamHandler
import logging, traceback

# setup
logger = logging.getLogger(__name__)
handler = muxStreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# use
logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
logger.critical("critical")
