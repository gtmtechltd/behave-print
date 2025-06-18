import logging
import sys
import time
from behave import given

logger = logging.getLogger(__name__)

@given("I am authenticated")
def step_impl(context):
    print("AUTHENTICATED!")
    logger.info("AUTHED1")
    logger.info("AUTHED2")
    logger.info("AUTHED3")
    sys.stdout.write("OMG")
    sys.stdout.flush()
    time.sleep(1)

