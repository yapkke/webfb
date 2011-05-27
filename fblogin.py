#!/usr/bin/env python
import web
import webfb.facebook as fb

urls = (
    r'/', 'index',
    r'/fb', 'webfb.facebook.login',
    r'/welcome', 'welcome'
    )

fb.init(105259509564192)

class welcome:
    """Welcome page
    """
    def POST(self):
        return '''
Welcome %s!
''' % str(web.input()['userName'])


class index:
    """Index page
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
