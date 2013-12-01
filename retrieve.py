import os
import mechanize
import cookielib

class Retrieve:

  def __init__(self):

    self.br = mechanize.Browser()

    cj = cookielib.LWPCookieJar()
    self.br.set_cookiejar(cj)

    self.br.set_handle_equiv(True)
    self.br.set_handle_gzip(True)
    self.br.set_handle_redirect(True)
    self.br.set_handle_referer(True)
    self.br.set_handle_robots(False)
    self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    #DEBUG
    self.br.set_debug_http(True)
    self.br.set_debug_redirects(True)
    self.br.set_debug_responses(True)

    self.br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

  def login(self):
    url = 'https://en.wordpress.com/wp-login.php'
    self.br.open(url)
    self.br.select_form(nr=0)
    self.br["log"] = os.environ['WORDPRESS_USER']
    self.br["pwd"] = os.environ['WORDPRESS_PW']
    login_results = self.br.submit().read()
    #f = file('login.html', 'w')
    #f.write(login_results)
    #f.close()
    return self

  def get_export(self):
    backup_url = os.environ['WORDPRESS_BACKUP_URL']
    response = self.br.open(backup_url)
    return response.read()
    #print response.geturl()
    #print response.info()
    #print response.read()
