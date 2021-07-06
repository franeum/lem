#!/usr/bin/env python3

import configlogger as log  
import submodule

logger = log.Logger(__name__, log_file=True)

logger.debug('Messaggio di debug')
logger.info('Messaggio info')
logger.warning('Avviso')
logger.error('Messaggio di errore')
logger.critical('Errore grave')

logger.info("ciao ciao")
