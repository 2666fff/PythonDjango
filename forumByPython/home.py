# The libraries we'll need
import sys, session, cgi, MySQLdb

# Get a DB connection
db = MySQLdb.connect("creosote.eng.unimelb.edu.au", "group04", "04yapmqzoH04", "group04", 3306)
cursor = db.cursor()

# Manage the session
sess = session.Session(expires=20*60, cookie_path='/')

# ---------------------------------------------------------------------------------------------------------------------
# send session cookie
print "%s\nContent-Type: text/html\n" % (sess.cookie)

# What came on the URL string?
params = cgi.FieldStorage()

singleForum = 0
singleThread = 0


# Check if user is viewing a specific forum
if params.has_key('forum'):
    sess.data['forum_info'] =  params['forum'].value
    # Find all threads in the forum
    sql = """
        select p.title, replace(p.body,'\n','<BR>'), p.date_posted, t.num_views, u.user_name, t.thread_id, t.num_posts, t.date_closed
        from thread t
        inner join post p on t.thread_id=p.thread_id
        inner join reg_user u on p.user_id=u.user_id
        where t.forum_id=%s
         and p.in_response_to is NULL
        order by p.post_id asc
    """
    cursor.execute(sql, params['forum'].value)
    threads = cursor.fetchall()
    singleForum = 1

    # Check if user is viewing a specific thread
    if params.has_key('thread'):
        sess.data['thread_info'] =  params['thread'].value
        # If viewing specific thread, fetch that one only
        sql = """
            select p.title, replace(p.body,'\n','<BR>'), p.date_posted, t.num_views, u.user_name, t.thread_id, t.num_posts, p.post_id,t.date_closed,p.censured
            from thread t
            inner join post p on t.thread_id=p.thread_id
            inner join reg_user u on p.user_id=u.user_id
            where t.forum_id=%s
              and t.thread_id=%s
            order by p.post_id asc limit 1                
        """                        #A
        cursor.execute(sql, (params['forum'].value, params['thread'].value))
    
        if cursor.rowcount == 1:                    #A
            threads = cursor.fetchall()
            singleThread = 1

cursor.close()



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
            <li class="current_page_item"><a href="home.py">Forums</a></li>
            <li><a href="about.py">About</a></li>
            %s
        </ul>
    </div>

    <div id="page">
    <div id="page-bgtop">
    <div id="page-bgbtm">
        <div id="content">
""" % ( "<li><a href=\"do_logout.py\"><font color=red>Logout</font></a></li>" if sess.data.get('loggedIn') else "<li><a href=\"login.py\">Login</a></li>")

#===========================welcome===========================
if sess.data.get('loggedIn'):
    print """<h5>welcome back %s, your current user group is %s!</h>""" % ( sess.data['userName'],"Moderator" if sess.data.get('mod') else "Member")
#===========================welcome===========================


# If looking at particular forum
if singleForum == 1:

    # Next, loop through all the threads
    for row in threads:

        # Display thread details
        print """
            <div class="post">
                <h2 class="title"><a href="home.py?forum=%s&thread=%s">%s</a></h2>
                <p class="meta"><span class="date"><a href="home.py">%s</a>,&nbsp;%s</span><span class="posted">%s reads&nbsp;|&nbsp;%s posts</span></p>
                <div style="clear: both;">&nbsp;</div>
                <div class="entry">
                    %s
                </div>
            </div>
        """ % (params['forum'].value, row[5], row[0], row[4], row[2], row[3], row[6], row[1] if singleThread == 1 else "")
        

        # If looking at particular thread
        if singleThread == 1:

            if sess.data.get('loggedIn'):
                print """
                    <div class="post">
                        <h3 >%s
                    
                """ % ( "This thread is closed" if row[8] != None else """<a href="newPost.py?forum=%s&thread=%s"><font color="red">Post to thread</font></a>"""%(params['forum'].value,params['thread'].value))
                
                #==========================MODERSTOR========================
                if sess.data.get('mod'):
                    print """
                    
                        <a href="mod.py?forum=%s&thread=%s"><font color="blue"><B><span style ="float:right;">%s</span></B></font></a></h3>
                    
                """ % (params['forum'].value,params['thread'].value,
                       "Manage Thread")
                print "</div>"
                    
                    
    
        
            # Grab its posts 
            cursor = db.cursor()
            sql = """
                select u.user_name, p.title, replace(p.body,'\n','<BR>'), p.date_posted, NULL, p.post_id,p.censured
                from post p
                inner join reg_user u on p.user_id=u.user_id
                where p.thread_id=%s
                  and p.post_id <> %s
                order by p.post_id asc
            """

            cursor.execute(sql, (params['thread'].value,row[7]))
            posts = cursor.fetchall()
    #===============================increase views===================Na
            cursor.execute ("""
                update thread set num_views = num_views + 1 where thread_id = %s
            """, params['thread'].value)
    #================================================================
            cursor.close()

            # Display them in order
            for p in posts:
        
                if int(p[6]) == 0 or sess.data.get('mod')!=0 :
                    print """
                        <div class="comment">
                            <div class="commentByLine">
                                Posted By %s | %s %s
                            
                        """ % (p[0], p[3], " | In response to a comment by %s" % p[4] if p[4] != None else "")
            
                    #===============MOd post=========================
                    if sess.data.get('mod') and sess.data.get('loggedIn'):
                        print """
                            <a href="mod.py?forum=%s&thread=%s&post=%s&censure=%s"><font color="blue"><B><span style ="float:right;">%s</span></B></font></a>
                            
                        """ % (params['forum'].value,params['thread'].value,p[5],'o' if int(p[6])==1 else 'c',
                           "Uncensure" if int(p[6])==1 else "Censure Post")
                    #===============MOd post=========================
            
                    print """
                            </div>
                            <div class="commentBody">
                                %s
                            </div>
                            <div class="commentByLine">%s</div>
                        </div>
                    """ % (p[2], "<a href='newPost.py?forum=%s&thread=%s'><font color=\"red\">Respond to post</font></a>"%(params['forum'].value,params['thread'].value) if                                     sess.data.get('loggedIn') and row[8] == None else "")
        


    if singleThread != 1 and sess.data.get('loggedIn'):
        print """
            <div class="post">
                <h3 style="text-align: right"><a href="newThread.py?forum=%s"><font color="red">Start new thread</font></a></h3>
            </div>
        """ % (params['forum'].value)
            

else:
    
    # Just landed on the home page, nothing clicked yet.
    print """
        <h1>Welcome to our discussion board!</h1>
    """

# Display left side bar
print """
        <div style="clear: both;">&nbsp;</div>
        </div>

        <div id="sidebar">
            <ul>
                <li>
                    <h2>Forums</h2>
                    <ul>
"""

# Display all our forums in order
cursor = db.cursor()
sql = """
    select forum_id, title
    from forum
    order by forum_id
"""

cursor.execute(sql)
forums = cursor.fetchall()
cursor.close()

for f in forums:
    print """
        <li><a href="home.py?forum=%s">%s</a></li>
    """ % (f[0], f[1])
    
print """
                    </ul>
                </li>
            </ul>
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
db.close()
sess.close()
