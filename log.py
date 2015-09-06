import logging

class Logger:

  def __init__(self):
    self.logger = logging.getLogger('wordpress-backup')
    hdlr = logging.FileHandler('/var/log/wordpress-backup.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    self.logger.addHandler(hdlr)
    self.logger.setLevel(logging.WARNING)
