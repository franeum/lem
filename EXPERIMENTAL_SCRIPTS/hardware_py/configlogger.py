import colorlog, logging 

OUTPUT_FILE = 'tastoma.log'

class Logger:
    def __init__(self, name, stream=True, log_file=False):
        self.logger = logging.getLogger(name.replace('_','')) 
        self.logger.setLevel(logging.DEBUG)
        self.formatter = colorlog.ColoredFormatter('%(log_color)s%(asctime)s\t-\t%(name)-8s\t - %(levelname)s: %(message)s')
        self.check_file(log_file)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch) 

    def __getattr__(self, name):
        def wrapper(message):
            if name in ['debug','info','warning','error','critical']:
                return getattr(self.logger, name)(message.upper())
        return wrapper

    def check_file(self, logfile):
        if logfile:
            fh = logging.FileHandler(OUTPUT_FILE)
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(self.formatter)
            self.logger.addHandler(fh)
