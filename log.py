import logging

class Log:
  def __new__(self):
      format = '[%(levelname)s::%(filename)s-%(funcName)s():line %(lineno)d] : %(message)s'
      logging.basicConfig(encoding='utf-8', level=logging.DEBUG, format=format)
      return logging

log = Log()