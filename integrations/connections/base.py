from utils.logger import Logger


class Connection():
    def __init__(self):
        self.logger = Logger(caller=self)

    def build_tags(self, **kwargs):
        return self.logger.build_tags(**kwargs)

    def error(self, message, tags={}, **kwargs):
        self.logger.error(message, tags, **kwargs)

    def exception(self, message, tags={}, **kwargs):
        self.logger.exception(message, tags, **kwargs)

    def info(self, message, tags={}, **kwargs):
        self.logger.info(message, tags, **kwargs)