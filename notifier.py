import os
import smtplib
from email.mime.text import MIMEText

class Notifier:

  def send_error(self, message):
    msg = MIMEText("")
    wordpress_user = os.environ['WORDPRESS_USER']
    pd_user = os.environ['PAGER_DUTY_USER']

    msg['Subject'] = 'Wordpress backup failed: ' + message
    msg['From'] = wordpress_user
    msg['To'] = wordpress_user

    s = smtplib.SMTP('localhost')
    s.sendmail(wordpress_user, [pd_user, wordpress_user], msg.as_string())
    s.quit()