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

![screen shot 2017-01-02 at 15 08 25](https://cloud.githubusercontent.com/assets/10671733/21585534/68427a1a-d0fd-11e6-9ccc-53f141511c16.png)

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

![screen shot 2017-01-02 at 15 08 40](https://cloud.githubusercontent.com/assets/10671733/21585535/6897c0b0-d0fd-11e6-853b-70ffec5ed723.png)

## ToDo
<hr/>

+ [ ] big message text friendly
+ [x] more useful info for ERROR and CRITICAL level
+ [ ] user-defined message string highlight
