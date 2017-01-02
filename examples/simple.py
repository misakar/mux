import logging
from mux import muxStreamHandler

# setup
logger = logging.getLogger(__name__)
handler = muxStreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# use
logger.debug("debugging for better result")
logger.info("nothing goes wrong thus far")
logger.warning("you should be careful")
logger.error("oh god! you made a mistake")
logger.critical("ctrl-c to stop...")
