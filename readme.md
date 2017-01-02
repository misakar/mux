# mux

💋 an elegant handler for python terminal logging

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
    logger.debug("debugging for better result")
    logger.info("everything is ok, so far")
    logger.warning("you should be careful")
    logger.error("oh, you made a mistake")
    logger.critical("ctrl-c to stop...")

![screen shot 2017-01-02 at 19 27 46](https://cloud.githubusercontent.com/assets/10671733/21588434/a5dcaa70-d121-11e6-8026-7ce9bb842234.png)

### Elegant exception traceback

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

![screen shot 2017-01-02 at 19 29 11](https://cloud.githubusercontent.com/assets/10671733/21588453/cd960c78-d121-11e6-8b73-31fb6cb0bf6f.png)

##  Big text friendly

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

![screen shot 2017-01-02 at 19 30 27](https://cloud.githubusercontent.com/assets/10671733/21588499/3ce8d34e-d122-11e6-8535-dcef4d34f548.png)

## Highlight customize

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

![screen shot 2017-01-02 at 19 35 26](https://cloud.githubusercontent.com/assets/10671733/21588544/b1a4bcf2-d122-11e6-8767-66be82b62283.png)

## Complete example

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
    logger.info("start project magic")
    try:
        os.mkdir('./magic')
    except OSError as e:
        logger.exception('{path} already exist'.format(
            path=mux_format(os.getcwd(), 'green', 'underline')))
    logger.info('start project magic done')

![screen shot 2017-01-02 at 19 37 57](https://cloud.githubusercontent.com/assets/10671733/21588567/06c01a06-d123-11e6-9565-4b38822bc04c.png)

## ToDo
<hr/>

+ [ ] download progress logging bar
+ [x] big text friendly
+ [x] more useful info for ERROR and CRITICAL level
+ [x] user-defined message string highlight

## License

[MIT]() @ [neo1218](https://github.com/neo1218)