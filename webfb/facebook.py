import web

fbAppId = None
welcomePage = None

def init(appid, welcomepage='welcome'):
    """Initiate variables for later use

    @author ykk
    @date May 2011
    """
    global fbAppId
    global welcomePage
    fbAppId = appid
    welcomePage = welcomepage

def login_form(loginpage='fb',icon='static/facebook.gif'):
    """Return login button for facebook login

    @author ykk
    @date May 2011
    """
    return '''
<form action="%s">
<input type=image src="%s">
</form>
''' % (loginpage, icon)

class login:
    """Facebook login page

    This page redirects the page to facebook and allows the username to login.
    This is done using javascript.  The access token is then processed by 
    javascript and the user name is returned to the welcome page.

    @author ykk
    @date May 2011
    """
    def GET(self):
        global fbAppId
        global welcomePage
        return '''
<html> 
  <head> 
    <title>webfb login page</title> 
  </head> 
  <body> 
    <script> 
      function submitUser(user) {
      var userName = document.getElementById('userName');
      fbLogin.userName.value = user.name;
      fbLogin.submit();
      }
      
      if (window.location.hash.length == 0) {
      var path = 'http://www.facebook.com/dialog/oauth?';
      var queryParams = ['client_id=' + %s,
      'redirect_uri=' + window.location,
      'response_type=token'];
      var query = queryParams.join('&');
      var url = path + query;
      window.location=url;
      } else {
      var accessToken = window.location.hash.substring(1);
      var path = "https://graph.facebook.com/me?";
      var queryParams = [accessToken, 'callback=submitUser'];
      var query = queryParams.join('&');
      var url = path + query;
      
      // use jsonp to call the graph
      var script = document.createElement('script');
      script.src = url;
      document.body.appendChild(script);        
      }
    </script> 
    <form method="post" name="fbLogin" action="%s">
      <input type="hidden" name="userName">
    </form>
  </body> 
</html>
''' % (fbAppId, welcomePage)

