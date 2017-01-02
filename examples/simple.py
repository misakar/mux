import logging
from mux import MuxStreamHandler

# setup
logger = logging.getLogger(__name__)
handler = MuxStreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# use
logger.debug("debugging for better result")
logger.info("everything ok, so far")
logger.warning("you should be careful")
logger.error("oh god! you made a mistake")
logger.critical("ctrl-c to stop")
