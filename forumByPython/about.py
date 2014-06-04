# The libraries we'll need
import session, cgi


# Manage the session
sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')

print "%s\nContent-Type: text/html\n" % (sess.cookie)

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
            <h1><a href="home.py">Group 4's Discussion Board</a></h1>
        </div>
    </div>

    <div id="menu">
        <ul>
            <li><a href="home.py">Forums</a></li>
            <li class="current_page_item" ><a href="about.py">About</a></li>
            %s
        </ul>
    </div>
""" % ( "<li><a href=\"do_logout.py\"><font color=red>Logout</font></a></li>" if sess.data.get('loggedIn') else "<li><a href=\"login.py\">Login</a></li>")

#================ about details goes in here.=============
print """
    <div id = "page">
        <h1> Made By Group 4 team!</h1>
        <img src="./img/about.jpg"/ width=400 height =400 align="left">
    </div>
"""
#================ about details goes in here.=============


# Footer at the end
print """
    <div id="footer">
        <p><z style="color:red">CLAIM:</z> <ul>This discussion board is designed for the final project of informatics 3 by group04 team members.</ul><ul>Wang Xiaochuan</ul><ul>Song Kaiwen</ul><ul>Wang Weiqian</ul><ul>Ho Jan Hao</ul><ul>Narae Lee</ul><ul>All rights reserved (C) 2012</ul></p>
    </div>
</div>
</body>
</html>
"""

# Tidy up and free resources
sess.close()


