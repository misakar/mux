# mux

[![PyPI](https://img.shields.io/pypi/v/nine.svg)](https://pypi.python.org/pypi/mux-handler/0.1)

💋 an elegant handler for python terminal logging

## Install

    $ pip install mux-handler

## Examples
<hr/>

### Let the magic begin 😎

    # import
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

![simple](https://cloud.githubusercontent.com/assets/10671733/21593016/e53ac9e6-d14d-11e6-8b65-499a85095094.png)

### Exception traceback

    # import
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

![screen shot 2017-01-03 at 00 04 27](https://cloud.githubusercontent.com/assets/10671733/21593024/fbf74f56-d14d-11e6-8955-0b08fd84cbfb.png)

###  Big text friendly

    # import
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

![bigtext](https://cloud.githubusercontent.com/assets/10671733/21593033/0e8b2318-d14e-11e6-872a-6887e0c03a6e.png)

### Highlight customize

    # import
    import os
    import logging
    from mux import MuxStreamHandler, mux_format
    # setup
    logger = logging.getLogger(__name__)
    handler = MuxStreamHandler()
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    # use
    logger.info("your current path is {path}".format(
        path=mux_format(os.getcwd(), "red", "underline")))
    logger.warning("be careful")

![screen shot 2017-01-03 at 00 03 58](https://cloud.githubusercontent.com/assets/10671733/21593163/2cbf7fc2-d14f-11e6-85fb-ab551b3e06a4.png)

### Task progress bar

    # import
    import os
    import time
    import logging
    from mux import MuxStreamHandler, mux_progressbar, mux_format
    # setup
    logger = logging.getLogger(__name__)
    handler = MuxStreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    # use
    @mux_progressbar
    def init():
        time.sleep(4)
    if __name__ == '__main__':
        logger.info('start task')
        init()
        logger.info('task done')

![bar](https://cloud.githubusercontent.com/assets/10671733/21593157/19bcd294-d14f-11e6-9720-10caeffba8a6.gif)

## ToDo
<hr/>

+ [ ] add python3 support
+ [x] download progress logging bar
+ [x] big text friendly
+ [x] more useful info for ERROR and CRITICAL level
+ [x] user-defined message string highlight

## License

[MIT](https://github.com/neo1218/mux/blob/master/LICENSE) @ [neo1218](https://github.com/neo1218)

## ChangeLogs

+ **v0.1**
    - achieve the basic functions