import web

fbAppId = None
welcomePage = None

def init(appid, welcomepage='welcome'):
    global fbAppId
    global welcomePage
    fbAppId = appid
    welcomePage = welcomepage

def login_form(loginpage='fb',icon='static/facebook.gif'):
    """Return login button for facebook login
    """
    return '''
<form action="%s">
<input type=image src="%s">
</form>
''' % (loginpage, icon)

class login:
    """Facebook login page
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
      var path = 'https://www.facebook.com/dialog/oauth?';
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

