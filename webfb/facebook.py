
class login:
    """Facebook login page
    """
    def GET(self):
        return '''
Very cool
'''

def login_form(loginpage='fb'):
    """Return login button for facebook login
    """
    return '''
<form action="%s">
<input type=image src="static/facebook.gif">
</form>
''' % loginpage

