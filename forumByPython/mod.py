import session, cgi, MySQLdb, redirect,sys

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
    # ---------------------------------------------------------------------------------------------------------------------
    # Send head of HTML document, pointing to our style sheet
    if params.has_key('forum') and params.has_key('thread'):
        
        #get information from database.
        sql = """
            select p.title, replace(p.body,'\n','<BR>'), p.date_posted, t.num_views, u.user_name, t.thread_id, t.num_posts, p.post_id,t.date_closed
            from thread t
            inner join post p on t.thread_id=p.thread_id
            inner join reg_user u on p.user_id=u.user_id
            where t.forum_id=%s
              and t.thread_id=%s
            order by p.post_id asc limit 1                
        """                        #A
        cursor.execute(sql, (params['forum'].value, params['thread'].value))
    
        if cursor.rowcount == 1:                    #A
            threads = cursor.fetchall()[0]
            
            cursor = db.cursor()
        
        #=======close or open thread.==============
            if params.has_key('close'):
                if params['close'].value == "o":
                    cursor.execute("""update thread set date_closed = NULL where forum_id=%s and thread_id=%s; """,(params['forum'].value, params['thread'].value))
                else:
                    cursor.execute("""UPDATE thread SET date_closed = NOW()
                      where forum_id=%s
                      and thread_id=%s;
                      """, (params['forum'].value, params['thread'].value))
        #===========================================
        
        #=======censure post=======================
            if params.has_key('censure') and params.has_key('post'):
                if params['censure'].value == "o":
                    cursor.execute("""update post set censured = 0 where thread_id=%s and post_id = %s; """,(params['thread'].value,params['post'].value))
                else:
                    cursor.execute("""UPDATE post SET censured = 1
                      where thread_id=%s
                      and post_id = %s;
                      """, (params['thread'].value,params['post'].value))
                    
                # redirect to current thread.
                print """\
                    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
                    <html xmlns="http://www.w3.org/1999/xhtml">
                    <head>
                    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
                    <meta http-equiv="refresh" content="0;url=%s">
                    </head>
                    <body>
                    </body>
                    """ % redirect.getQualifiedURL( "/serve/wangw/info3/group4/forum/home.py?forum=%s&thread=%s"%(params['forum'].value, params['thread'].value))
                sys.exit() 
        #===========================================
            
            #reload information.
            cursor = db.cursor()
            sql = """
            select p.title, replace(p.body,'\n','<BR>'), p.date_posted, t.num_views, u.user_name, t.thread_id, t.num_posts, p.post_id,t.date_closed
            from thread t
            inner join post p on t.thread_id=p.thread_id
            inner join reg_user u on p.user_id=u.user_id
            where t.forum_id=%s
              and t.thread_id=%s
              and p.censured=0
            order by p.post_id asc limit 1                
            """                        #A
            cursor.execute(sql, (params['forum'].value, params['thread'].value))
            if cursor.rowcount == 1:                    #A
                threads = cursor.fetchall()[0]
                
        
        
        
        
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
                    <b><h3 style="text-align:center;">what do you want do with this Thread?</h3></b>
                    <p><b><h3 style="text-align:center;">%s</h3></b></p>
                    <center><button onClick="location.href='mod.py?forum=%s&thread=%s&close=%s'">%s thread</button></div></center>
                    <br/>
                    <div class="post">
                    <center>
                    <form method="post" action="do_relate.py?thread=%s">
                    <table><tr>Thread id: <input type="text" name="t_id" />
                    <input type="submit" name="thread" value="relate to thread"/></tr>
                    </table>
                    </center>
                    </form>      
                    </div>

                    <div id="post">
                    <center><button onClick="location.href='home.py?forum=%s&thread=%s'">Back To Thread</button></div></center>
                    
          '''  %(threads[0],params['forum'].value, params['thread'].value, 'c' if threads[8] == None else 'o',"Close" if threads[8] == None else "Open",params['thread'].value,params['forum'].value, params['thread'].value)

      

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
 
