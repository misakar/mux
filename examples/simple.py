import logging
from mux import MuxStreamHandler

# setup
logger = logging.getLogger(__name__)
handler = MuxStreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# use
logger.debug("let the magic begin")
logger.info("everything ok")
logger.warning("be careful")
logger.error("you made a mistake")
logger.critical("ctrl-c to stop...")
