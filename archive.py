import urllib
import os
import shutil
import tarfile
import datetime

from bs4 import BeautifulSoup
from boto.s3.connection import S3Connection
from boto.s3.key import Key


class Archive:

  def process(self, doc):
    self.backup_root = "/tmp"
    self.files = []
    self.backup_location = self.backup_root + "/wp_backup"
    try:
      shutil.rmtree(self.backup_location)
    except:
      pass
    try:
      os.makedirs(self.backup_location)
    except Exception,e:
      pass

    soup = BeautifulSoup(doc, "lxml")
    attachments = soup.findAll('wp:attachment_url')
    for attachment in attachments:
      filename = attachment.text.split('/')[-1]
      filepath =  self.backup_location + "/" + filename
      try:
        urllib.urlretrieve(attachment.text, filepath)
        self.files.append(filepath)
      except Exception:
        pass
    return self

  def save(self):
    self.archive_file_name = "wordpress_backup_" + datetime.datetime.now().strftime("%y%m%d") + ".tar"
    self.archive_file_path = self.backup_root + "/" + self.archive_file_name
    try:
      tar = tarfile.TarFile(self.archive_file_path, "w")
      for file_path in self.files:
        tar.add(file_path)
      tar.close()
    except Exception:
      pass
    return self

  def backup(self, export_doc):
    self.process(export_doc)
    self.save()
    try:
      conn = S3Connection(os.getenv('AMAZON_KEY'), os.getenv('AMAZON_SECRET'))
      bucket = conn.get_bucket("geoffreymoller")
      k = Key(bucket)
      k.key = self.archive_file_name
      k.set_contents_from_filename(self.archive_file_path)
    except Exception:
        pass
    return self
    self.cleanup();

  def cleanup(self):
    shutil.rmtree(self.backup_location)
    os.remove(self.archive_file_path)
    return self


