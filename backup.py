import os
import mechanize
import cookielib

br = mechanize.Browser()

cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

#DEBUG 
br.set_debug_http(True)
br.set_debug_redirects(True)
br.set_debug_responses(True)

br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

theurl = 'https://en.wordpress.com/wp-login.php'
br.open(theurl)
br.select_form(nr=0)
br["log"] = os.environ['WORDPRESS_USER']
br["pwd"] = os.environ['WORDPRESS_PW']
login_results = br.submit().read()
f = file('login.html', 'w')
f.write(login_results) 
f.close()

backup_url = os.environ['WORDPRESS_BACKUP_URL']
response = br.open(backup_url)
print response.geturl()
print response.info()
print response.read()

