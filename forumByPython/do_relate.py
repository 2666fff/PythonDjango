import session, cgi, MySQLdb, redirect,string

# Manage the session
sess = session.Session(expires=20*60, cookie_path='/')

# Get a DB connection
db = MySQLdb.connect("creosote.eng.unimelb.edu.au", "group04", "04yapmqzoH04", "group04", 3306)
cursor = db.cursor()

# ---------------------------------------------------------------------------------------------------------------------
# send session cookie
print "%s\nContent-Type: text/html\n" % (sess.cookie)

# What came on the URL string?
params = cgi.FieldStorage()

if not sess.data.get('mod') or sess.data['loggedIn'] == 0:
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
    if params.has_key('r_id'):
        if params['r_id'].value.isdigit():
            cursor.execute("""
                               select thread_id_1,thread_id_2 from related_thread where thread_id_1 = %s and thread_id_2=%s
                               """,(params['r_id'].value,params['thread'].value))
            a = cursor.rowcount

            cursor = db.cursor()
            cursor.execute("""
                               select thread_id_1,thread_id_2 from related_thread where thread_id_2 = %s and thread_id_1=%s
                               """,(params['r_id'].value,params['thread'].value))
            b = cursor.rowcount

            
            if a !=1 and b!= 1:
                
                cursor = db.cursor()
                cursor.execute("""
                                   INSERT INTO related_thread Values( %s,%s)
                                   """,(params['r_id'].value,params['thread'].value))
        
                print "Done! Now back to Home."
        
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
                print "they are already realted."
        

        

    if params.has_key('t_id') :
        tid = params['t_id'].value
        if tid.isdigit():
            cursor.execute("""
                           select p.title from thread t inner join post p on p.thread_id = t.thread_id where t.thread_id = %s order by p.post_id asc limit 1
                           """,tid)
            if cursor.rowcount == 1:                    #A
                thread = cursor.fetchall()[0]
                print "so the thread you want realte to is <h3>%s</h3>" % thread[0]
                
                print """<button onClick="location.href='do_relate.py?thread=%s&r_id=%s'">relate</button>"""%(params['thread'][1].value,tid)
                print """<button onclick='history.back()';">back to manage</button>"""
            else:
                print "cant find this threa id try again."
            
        else:
            print "error, plz put in a thread_id digit."
            
        
