
import MySQLdb,sys,os,cgi,time,session,string,redirect

# Manage the session
sess = session.Session(expires=20*60, cookie_path='/')

db = MySQLdb.connect("creosote.eng.unimelb.edu.au", "group04", "04yapmqzoH04", "group04", 3306)

# ---------------------------------------------------------------------------------------------------------------------
# send session cookie
print "%s\nContent-Type: text/html\n" % (sess.cookie)

# What came on the URL string?
params = cgi.FieldStorage()

if sess.data['mod'] == 0 or sess.data['loggedIn'] == 0:
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

#=======================insert forum========================
if params.has_key('forumid') and params.has_key('forumname') and params.has_key('forum_description'):
    fid = params['forumid'].value
    fnm = params['forumname'].value
    fds = params['forum_description'].value
    if fid.isdigit():
        cursor = db.cursor()
        cursor.execute("select * from forum where forum_id = %s",fid)
        
        if cursor.rowcount == 0:
            cursor.execute("""INSERT INTO forum values (%s,%s,%s) ;""",(fid,fnm,fds))
            print "forum NO.:%s Title:%s Summary:%s has been insert." %(fid,fnm,fds)
            print """<button onclick='history.back()';">back</button>"""
        else:
            print "forum_id already exist."
            print """<button onclick='history.back()';">back</button>"""
    else:
        print "PLZ enter a valid forum ID"
        print """<button onclick='history.back()';">back</button>"""
    sys.exit()
        
    
#========================insert moderator====================

if params.has_key('moderation_id') and params.has_key('forum_id') and params.has_key('user_id'):
    mid = params['moderation_id'].value
    fid = params['forum_id'].value
    uid = params['user_id'].value
    if fid.isdigit() and uid.isdigit() and mid.isdigit():
        cursor = db.cursor()
        cursor.execute("select * from moderation where moderation_id = %s",mid)
        cu = db.cursor()
        cu.execute("select user_name from reg_user where user_id = %s",uid)
        
        
        if cursor.rowcount == 0 and cu.rowcount == 1:
            cursor.execute("""INSERT INTO moderation(moderation_id,moderator_from,user_id,forum_id) VALUES(%s,curdate(),%s,%s); ;""",(mid,uid,fid))
            
            print "forum NO.:%s Moderator:%s has been insert." %(fid,cu.fetchall()[0][0])
            print """<button onclick='history.back()';">back</button>"""
        else:
            print "moderator_id already exist or user_id donest exist."
            print """<button onclick='history.back()';">back</button>"""
    else:
        print "PLZ enter a valid ID"
        print """<button onclick='history.back()';">back</button>"""
    sys.exit()
    


#==============================================================================================
db = MySQLdb.connect("creosote.eng.unimelb.edu.au", "group04", "04yapmqzoH04", "group04", 3306)
cursor1 = db.cursor()
cursor1.execute(" select * from forum;")
cursor2=db.cursor()
cursor2.execute('select * from reg_user u left outer join moderation m on u.user_id = m.user_id order by m.moderation_id DESC;') 




print '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <link type="text/css" href="css/styles_admin.css" rel="stylesheet">
    <title>admin</title>
    
</head>

<body>
<p>welcome admin!</p> 

<h1>admin management interface</h1>
<h2>group 4's discussion board project</h2>
<ul align = 'middle'><button onClick="location.href='home.py'">Home</button></ul>

<div id="buttom">
<ul><form method="post" action="admin.py">
    <li><input id="forumid" type="text" name="forumid" value="forum id"></li>
    <li><input id="forumname" type="text" name="forumname" value="forum name"></li>
    <li><input id="forum_description" type="text" name="forum_description" value="description"></li>
</ul>
<ul><input id="addforum" value="add a new forum" type="submit" ></ul>
</form>'''

print '<ul>existing forums:</ul><table><tr><td>forum id</td><td>forum name</td><td>description</td></tr>'
for i in cursor1.fetchall():     print('<tr><td> %s </td><td> %s </td><td> %s</td> </tr>')% (i[0],i[1],i[2])
    
print '''
</table>
<form method="post" action="admin.py">
<ul>esisting registered users:</ul> <table><tr><td>user id</td><td>user nmae</td><td>moderation id</td><td>forum id</td></tr>'''
for j in cursor2.fetchall(): print('<tr><td>%s </td><td> %s</td><td> %s</td><td>%s</td> </tr>')% (j[0],j[1],j[5], j[8])
print '''
</table>
<li><input id="moderation_id" type="text" name="moderation_id" value="moderation id"></li>
<li><input id="forum_id" type="text" name="forum_id" value="forum id"></li>
<li><input id="user_id" type="text" name="user_id" value="user_id"></li>
<ul><input id="addmoderator" value="Add Moderators" type="submit"></ul></form>

<ul><button onClick="location.href='do_logout.py'">LogOut</button></ul>
</div>
</body>
</html>

'''