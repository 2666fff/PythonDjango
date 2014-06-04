# The libraries we'll need
import sys, cgi, session, redirect, MySQLdb

# ---------------------------------------------------------------------------------------------------------------------
sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')

# ---------------------------------------------------------------------------------------------------------------------
# send session cookie

print "%s\nContent-Type: text/html\n" % (sess.cookie)
# ---------------------------------------------------------------------------------------------------------------------

if loggedIn:
    
     # ---------------------------------------------------------------------------------------------------------------------
   
    # Send head of HTML document, pointing to our style sheet
    print """
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
   
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta name="keywords" content="" />
    <meta name="description" content="" />
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title>Informatics 3 Discussion Board</title>
    <link href="css/style.css" rel="stylesheet" type="text/css" media="screen" />
    </head>
    <body>
    """
     # Main HTML content, starting with header and main menu
    print """
    <div id="wrapper">
        <div id="header">
            <div id="logo">
                <h1><a href="home.py"></a>OPEN A NEW THREAD</h1>
            </div>
        </div>
    """
  
   

    print """
        <div id="page">
        <div id="page-bgtop">
        <div id="page-bgbtm">   
            <div id="content">
            <div class="post">
                <form method="post" action="thread_post_input.py">
                <h1>Initial Post</h1>
                <table><tr><td><p class="meta">Title</td><td><input style="width: 260px; text-align:center;" type="text" name="title" /></p></td></tr>
                <tr><td><p class="meta">Body </td><td><textarea name="body" cols ="50" rows = "5"></textarea></p></td></tr>
                <tr><td><input type="submit" name="open" id="search-submit" value="Open"/></td><td><i style="text-align:right;"><a href=\"home.py\">Cancel and Back to Home</a></i></td></tr>  
                </table> 
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

else:

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
    """ % redirect.getQualifiedURL("serve/hojh/info3/group4/forum/login.py")



# Tidy up and free resources
sess.close()    