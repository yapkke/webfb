#!/usr/bin/env python
import web
import webfb.facebook as fb

##The three urls needed
urls = (
    r'/', 'index',
    r'/fb', 'webfb.facebook.login',
    r'/welcome', 'welcome'
    )

##Initialize with app id for facebook app and 
##can define where to go after login (default to "welcome")
fb.init(105259509564192)

class welcome:
    """Sample welcome page that prints username
    """
    def POST(self):
        return '''
Welcome %s!
''' % str(web.input()['userName'])

class index:
    """Sample index page with just facebook login icon
    """
    def GET(self):
        return '''
<html><body><center>
%s
</center></body></html>
''' % fb.login_form()

##Run server
app = web.application(urls, globals())
if __name__ == "__main__":
    app.run()
