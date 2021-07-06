#!/usr/bin/env python3

import configlogger as log  
import logging

logger = log.Logger(__name__, log_file=False)

logger.info('Messaggio from submodule')