# The libraries we'll need
import sys, cgi, redirect, session

# Get the session and check if logged in
sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')

# ---------------------------------------------------------------------------------------------------------------------
# send session cookie
print "%s\nContent-Type: text/html\n" % (sess.cookie)

# debug - what's in the session
#print(sess.data)
#sys.exit()

if loggedIn:
    
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
    <title>Informatics 3 Discussion Board - Login page</title>
    <link href="css/style.css" rel="stylesheet" type="text/css" media="screen" />
    </head>
    <body>
    """
    # Main HTML content, starting with header and main menu
    print """
    <div id="wrapper">
        <div id="header">
            <div id="logo">
                <h1><a href="home.py">Group 4's Discussion Board</a></h1>
            </div>
        </div>

        <div id="menu">
            <ul>
                <li><a href="home.py">Forums</a></li>
                <li><a href="about.py">About</a></li>
                %s
            </ul>
        </div>
    """ % ( "<li ><a href=\"do_logout.py\"><font color=red>Logout</font></a></li>" if sess.data.get('loggedIn') else "<li class=\"current_page_item\"><a href=\"login.py\">Login</a></li>")

    print """
        <div id="page">
        <div id="page-bgtop">
            <div id="content">
                <p class = "meta">Not a member yet?<h><a href = "reg.py"> Regesiter now!</a></h></p>
            </div>
        <div id="page-bgbtm">
            <div id="content">
            <div class="post">
                <form method="post" action="do_login.py">
                <p class="meta">Username <input style="text-align:center;" type="text" name="username" /></p>
                <p class="meta">Password <input style="text-align:center;" type="password" name="password" /></p>
                <input type="submit" id="search-submit" value="Login" />
                </form>
            </div>
    """

    # debug - what's in the session
    #print(sess.data)

    # Display left side bar
    print """
            <div style="clear: both;">&nbsp;</div>
            </div>

            <div id="sidebar">
            </div>

            <div style="clear: both;">&nbsp;</div>
        </div>
        </div>
        </div>

    </div>
    """

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
