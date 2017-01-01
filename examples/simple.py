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
print("\n")
logger.debug("debugging for better result")
logger.info("nothing goes wrong thus far")
logger.warning("you should be careful")
logger.error("oh god! you made a mistake")
logger.critical("ctrl-c to stop...")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

