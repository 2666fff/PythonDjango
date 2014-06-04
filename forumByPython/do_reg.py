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
    if params.has_key('username') and params.has_key('password') and params.has_key('email_add') and params['username'].value != '' and params['password'].value != ''and params['email_add'].value != '':
        
        query = 'select user_name from reg_user;'
        cursor.execute(query)
        user_name_list = []
        user_list = cursor.fetchall()
        
        for i in user_list:
            user_name_list.append(i[0])    
        reg_now_user_name = params['username'].value
        
        if reg_now_user_name not in user_name_list and 'admin' not in reg_now_user_name:
            
        
            def get_user_id():
                query = 'select max(user_id) from reg_user;'
                cursor.execute(query)
                result_user_id = cursor.fetchone()[0]
                new_user_id = int(str(result_user_id))+1
                return new_user_id
        


            
            username_input = '''"%s"'''%(params['username'].value)   
            password_input = '''"%s"'''%(params['password'].value)     
            email_add_input = '''"%s"'''%(params['email_add'].value)
            user_id_input = '''"%s"'''%(get_user_id())
        
            sql = '''INSERT INTO reg_user(user_id,user_name,user_password,email_address,date_joined)
                VALUES(%s,%s,%s,%s,%s);'''%(user_id_input,username_input,password_input,email_add_input,"curdate()")
            cursor.execute(sql)      
            cursor.close()

            # Tidy up and free resources
            db.close()
            sess.close()
        
            # redirect to login page
            print """Content-Type: text/html"""
            print     
            print '''  <html xmlns="http://www.w3.org/1999/xhtml">
                    <head>
                    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
                    </head>
                    <h1>You have successfully registered, please check click following link to login now:</h1>
                    <br /><br /><body><i><i><br /><a href=\"login.py\">Login now!</a></i><br /></body>
                    <br /><a href=\"home.py\">Login later and back to Home</a></i><br />
                    </html>'''
        # error msg and links
        else:
            print """Content-Type: text/html"""
            print     
            print '''  <html xmlns="http://www.w3.org/1999/xhtml">
                    <head>
                    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
                    </head>
                    <h1>Oh, there is something wrong with your request of registering, please check against following:</h1>
                    <p>Don't use any 'admin'-alike word in your username, in order to avoid some issues.</p>
                    <p>If it still doesn't work, try a special and unique username that you can come up with!</p>
                    <br /><br /><body><i><i><br /><a href=\"reg.py\">Try again</a></i><br /></body>
                    <br /><a href=\"home.py\">Back to Home</a></i><br />
                    </html>'''
        
    # error msg and links
    else:
        print """Content-Type: text/html"""
        print     
        print '''  <html xmlns="http://www.w3.org/1999/xhtml">
                    <head>
                    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
                    </head>
                    <h1>Oh, there is something wrong with your request of registering, please check against following:</h1>
                    <p>Please fill in all the details asked.</p>
                    <br /><br /><body><i><i><br /><a href=\"reg.py\">Try again</a></i><br /></body>
                    <br /><a href=\"home.py\">Back to Home</a></i><br />
                    </html>'''


