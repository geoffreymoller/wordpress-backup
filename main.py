from retrieve import Retrieve
from archive import Archive
from notifier import Notifier
from log import Logger

try:
  export_doc = Retrieve().get_export()
  Archive().backup(export_doc)
except Exception, e:
  logger = Logger().logger
  logger.error(e.message)
  Notifier().send_error(e.message)
