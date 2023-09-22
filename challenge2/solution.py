import logging

logger = logging.getLogger("some_app")

def some_api_call(foo):
    return

def bad1(secret):
    logger.info("here is my secret value: %s",secret)

def bad2(api_key):
    try:
        some_api_call(api_key)
    except:
        logger.error("api call using api key %s failed",api_key)

def ok(api_key):
    try:
        some_api_call(api_key)
    except:
        logger.exception("api call failed.  Check your API key!")
