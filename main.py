from retrieve import Retrieve
from archive import Archive

#TODO - exception handling

export_doc = Retrieve().login().get_export()
Archive().process(export_doc).save().backup().cleanup()
