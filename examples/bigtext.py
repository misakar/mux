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
logger.info("Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess")
logger.warning("you should be careful")
logger.error("oh god! you made a mistake")
logger.critical("ctrl-c to stop")
