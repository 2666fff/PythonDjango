# The libraries we'll need
import sys, cgi, session, redirect, MySQLdb

# ---------------------------------------------------------------------------------------------------------------------
sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')

# ---------------------------------------------------------------------------------------------------------------------
# send session cookie
print "%s\nContent-Type: text/html\n" % (sess.cookie)

# ---------------------------------------------------------------------------------------------------------------------
# login logic
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
    form = cgi.FieldStorage()
    if not (form.has_key('username') and form.has_key('password')):
        sess.data['loggedIn'] = 0
    else:
        #check admin
        if form['username'].value == "admin" and form['password'].value == "adminpass":
            sess.data['loggedIn'] = 1
            sess.data['mod'] = 1
            sess.data['adm'] = 1
            sess.data['userName'] = "admin"
            # redirect to admin page
            print """\
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
            <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
            <meta http-equiv="content-type" content="text/html; charset=utf-8" />
            <meta http-equiv="refresh" content="0;url=%s">
            </head>
            <body>
            </body>
            """ % "admin.py"
            sys.exit()
        
            
            
        
        # Check user's username and password
        db = MySQLdb.connect("creosote.eng.unimelb.edu.au", "group04", "04yapmqzoH04", "group04", 3306)
        cursor = db.cursor()
        cursor.execute ("""
            SELECT user_name
            FROM reg_user
            WHERE user_name = %s
              AND user_password = %s
        """, (form["username"].value, form["password"].value))
        if cursor.rowcount == 1:
            sess.data['loggedIn'] = 1
            row = cursor.fetchone()
            sess.data['userName'] = row[0]
        else:
            sess.data['loggedIn'] = 0
            
        #check moderater###########-=-=-============================================ 
        
        if sess.data['loggedIn']:
            
            cursor.execute ("""
                select m.forum_id from moderation m
                inner join reg_user r on m.user_id = r.user_id
                where r.user_name = %s;
            """, (form["username"].value))
            rc = cursor.rowcount
            sess.data['mod'] = 0
            while rc > 0:
                sess.data['mod'] = []
                sess.data['mod'].append(cursor.fetchone()[0])
                rc = rc - 1
        ###########-=-=-============================================ ====================
        

        # tidy up
        cursor.close()
        db.close()

    whereToNext = "/serve/wangw/info3/group4/forum/home.py" if sess.data['loggedIn'] == 1 else "/serve/wangw/info3/group4/forum/login.py"
    sess.close()
    
    # redirect to home page or back to the login page
    print """\
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta http-equiv="refresh" content="0;url=%s">
    </head>
    <body>
    </body>
    """ % redirect.getQualifiedURL(whereToNext)

