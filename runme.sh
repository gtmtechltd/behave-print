#!/bin/bash

export PYTHONUNBUFFERED=1   # force python to flush print statements

# We use --format=plain, as summary control codes can reset the cursor and overwrite the logs/prints
# We use --no-capture to not capture the stdout (logger.info still gets captured)

behave --no-capture --format=plain

