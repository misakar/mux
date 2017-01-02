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

![screen shot 2017-01-02 at 15 01 28](https://cloud.githubusercontent.com/assets/10671733/21585496/79d28c94-d0fc-11e6-8ea5-c1efcb4d517f.png)

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

![screen shot 2017-01-02 at 15 05 18](https://cloud.githubusercontent.com/assets/10671733/21585513/f168668e-d0fc-11e6-8496-049d9640b8aa.png)

## ToDo
<hr/>

+ [ ] big message text friendly
+ [x] more useful info for ERROR and CRITICAL level
+ [ ] user-defined message string highlight
