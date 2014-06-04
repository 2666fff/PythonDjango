import session, cgi,redirect

# Manage the session
sess = session.Session(expires=20*60, cookie_path='/')

# send session cookie
print "%s\nContent-Type: text/html\n" % (sess.cookie)

if sess.data.get('loggedIn'):
    # redirect to home page
    print """\
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta http-equiv="refresh" content="0;url=%s">
    </head>
    <body>
    </body>
    """ % redirect.getQualifiedURL( "/serve/wangw/info3/group4/forum/home.py")
    
else:
    # ---------------------------------------------------------------------------------------------------------------------
    # Send head of HTML document, pointing to our style sheet
    print """
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
            
            <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
            <meta name="keywords" content="" />
            <meta name="description" content="" />
            <meta http-equiv="content-type" content="text/html; charset=utf-8" />
            <title>Informatics 3 Discussion Board - registering page</title>
            <link href="css/style.css" rel="stylesheet" type="text/css" media="screen" />
            </head>
            <body>
            <div id="wrapper">
                <div id="header">
                    <div id="logo">
                        <h1><a href="home.py">Our Discussion Board</a></h1>
                    </div>
                </div>
             </div>
    <div style="clear: both;">&nbsp;</div>
            """   

# =========================fill here==========

    print '''      <div id="post">   
                    <b><h2 style="text-align:center;">To register as a memeber, please enter the following information:</h2></b>
                    <center><form method="post" action="do_reg.py">
                    <tabel>
                    <tr><td><p class="meta">Username :</p></td><td><input style="text-align:center;" type="text" text-align:center; name="username" /></td></tr>
                    <tr><td><p class="meta">Password :</p></td><td><input style="text-align:center;" type="password" name="password" /></td></tr>
                    <tr><td><p class="meta">Email-address:</p></td><td><input style="text-align:center;" type="text" name="email_add" value="@" /></td></tr>
                    <tr><center><input id="submit" name="submit" value="Register now!" type="submit"/><center></tr><tr><ul></ul></tr>
                    <tr><ul style="text-align:center;"><a href=\"home.py\">Cancel and Back to Home</a></ul></tr> </table>
                    </form></div></center> 
                    <ul></ul>
                    <ul></ul>
 '''  

      

# =========================fill here==========
 
 
    # Footer at the end
print """
        <div id="footer"> 
            <p>This discussion board is designed for the final project of informatics 3 by group04 team members.</p>
        </div>
    </body>
    </html> 
    """

# Tidy up and free resources
sess.close()

