# The libraries we'll need
import sys, session, cgi, MySQLdb, redirect

# ---------------------------------------------------------------------------------------------------------------------
sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')

# Get a DB connection
db = MySQLdb.connect("creosote.eng.unimelb.edu.au", "group04", "04yapmqzoH04", "group04", 3306)
cursor = db.cursor()

# What came on the URL string?
params = cgi.FieldStorage()  

if "submit" in params:
    if params.has_key('body') and params.has_key('title') and params['title'].value != '' and params['title'].value != '': 
        
        def get_post_id():
            query = 'select max(post_id) from post;'
            cursor.execute(query)
            result_post_id = cursor.fetchone()[0]
            new_post_id = int(str(result_post_id))+1
            return new_post_id
        
        def get_user_id():
            query = '''            
            SELECT user_id
            FROM reg_user
            WHERE user_name = '%s' ;'''%(sess.data.get('userName'))
            cursor.execute(query)
            result_user_id = cursor.fetchone()[0]            
            return result_user_id
        
        def get_response_post_id():
            query = '''            
                    select response_post_id from
                    (select f.title as Name_of_forums, p.title as Title_of_threads,t.num_posts as Number_of_posts,p.post_id as response_post_id
                    from forum f
                    inner join thread t on f.forum_id = t.forum_id
                    inner join post p on t.thread_id = p.thread_id 
                    where date(p.date_posted) <= all (select date(p.date_posted) from post)
                    and p.post_id = some (select min(post.post_id) from post group by post.thread_id)
                    and p.thread_id = %s
                    group by p.title
                    order by num_posts asc) temp; ;'''%(sess.data.get('thread_info'))
            cursor.execute(query)
            result_response_post_id = cursor.fetchone()[0]            
            return result_response_post_id
            
        title_input = '''"%s"'''%(params['title'].value)    #Art
        body_input = '''"%s"'''%(params['body'].value)      #Art
        post_id_input = '''"%s"'''%(get_post_id())
        thread_id_input = '''"%s"'''%(sess.data.get('thread_info'))
        user_id_input = '''"%s"'''%(get_user_id())
        response_post_input = '''"%s"'''%(get_response_post_id())
        
        sql = '''INSERT INTO post(post_id,title,body,date_posted,user_id,thread_id,in_response_to)
                 VALUES(%s,%s,%s,%s,%s,%s,%s);'''%(post_id_input,title_input,body_input,"now()",user_id_input,thread_id_input,response_post_input)
        cursor.execute(sql)
        
        #============increase thread num_pots.=======================
        cursor.execute("""
                       update thread set num_posts = num_posts + 1 where thread_id = %s
                       """
                       ,sess.data.get('thread_info'))
        #=============================================================
              
        cursor.close()

        # Tidy up and free resources
        db.close()
        
        
        # redirect to home page
        print """Content-Type: text/html"""
        print 
        print """  <html xmlns="http://www.w3.org/1999/xhtml">
                    <head>
                    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
                    <meta http-equiv="refresh" content="0;url=home.py?forum=%s&thread=%s">
                    </head>
                    <body>
                    </body>
                    </html>
                """ %(sess.data.get('forum_info'),sess.data.get('thread_info'))
        
        
        
    # error msg and a link back to home page
    else:
        print """Content-Type: text/html"""
        print     
        print '''  <html xmlns="http://www.w3.org/1999/xhtml">
                    <head>Error: Please fill in both field of title and body, in order to make the reply!
                    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
                    </head>
                    <body><i><br /><a href=\"home.py\">Back to Home</a></i><br />
                    </body>
                    </html>'''
if "open" in params:
    if params.has_key('body') and params.has_key('title'):
        
        def get_thread_id():
            query = 'select max(thread_id) from thread'
            cursor.execute(query)
            result_thread_id = cursor.fetchone()
            new_thread_id = int(result_thread_id[0])+1
            return new_thread_id
        
        def get_post_id():
            query = 'select max(post_id) from post'
            cursor.execute(query)
            result_post_id = cursor.fetchone()
            new_post_id = int(result_post_id[0])+1
            return new_post_id
        
        def get_user_id():
            query = 'select user_id from reg_user where user_name = "%s"'%(sess.data.get('userName'))
            cursor.execute(query)
            result_user_id = cursor.fetchone()
            return result_user_id
        
        title_input = '''"%s"'''%(params['title'].value)    #Art
        body_input = '''"%s"'''%(params['body'].value)      #Art
        post_id_input = '''"%s"'''%(get_post_id())
        thread_id_input = '''"%s"'''%(get_thread_id())
        user_id_input = '''"%s"'''%(get_user_id())
        forum_id_input ='''"%s"'''%(sess.data.get('forum_info'))
          
         
        sql1 = '''INSERT INTO thread(thread_id,num_views,num_posts,forum_id,attitude_id)
                 VALUES(%s,%s,%s,%s,%s);'''%(thread_id_input,0,1,forum_id_input,'null')
        sql2 = '''INSERT INTO post(post_id,title,body,date_posted,user_id,thread_id,in_response_to)
                 VALUES(%s,%s,%s,%s,%s,%s,%s);'''%(post_id_input,title_input,body_input,'now()',user_id_input,thread_id_input,'null')
        
        cursor.execute(sql1)  
        cursor.execute(sql2)
        
        
        
        
        print """Content-Type: text/html"""
        print
        print """  <html xmlns="http://www.w3.org/1999/xhtml">
                    <head>
                    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
                    <meta http-equiv="refresh" content="0;url=home.py?forum=%s&thread=%s">
                    </head>
                    <body>
                    </body>
                    </html>
                """ %(sess.data.get('forum_info'),get_thread_id()-1)

        
    else:
        print """Content-Type: text/html"""
        print     
        print '''  <html xmlns="http://www.w3.org/1999/xhtml">
                    <head>Error: Please fill in both field of title and body, in order to make the reply!
                    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
                    </head>
                    <body><i><br /><a href=\"home.py\">Back to Home</a></i><br />
                    </body>
                    </html>'''
        # Tidy up and free resources
    db.close()
    cursor.close()    
# redirect to home page
else:

    print """Content-Type: text/html"""
    print 
    print """  <html xmlns="http://www.w3.org/1999/xhtml">
                    <head>
                    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
                    <meta http-equiv="refresh" content="0;url=home.py?forum=%s&thread=%s">
                    </head>
                    <body>
                    </body>
                    </html>
                """ %(sess.data.get('forum_info'),sess.data.get('thread_info'))
sess.close()

