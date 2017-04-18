#!/usr/local/bin/python3

from cgitb import enable 
enable()

import pymysql as db
            
print('Content-Type: text/html')
print()

result = ''
try:
    connection = db.connect(# login)
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""SELECT candidate_name
                      FROM candidates 
                      ORDER BY candidate_name ASC""")
    if cursor.rowcount == 0:
        result = '<p>Sorry. There are no candidates at present.</p>'
    else:
        options = ''
        for row in cursor.fetchall():
            options += '<option value="%s">%s</option>' % (row['candidate_name'], row['candidate_name'])
        result = """<form action="update_vote.py" method="post">
                    <select name="candidate_name">%s</select>
                    <input type="submit" value="Vote now">
                    </form>""" % (options)
    cursor.close()  
    connection.close()
except db.Error:
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'
        
print("""
    <!DOCTYPE html>
        <html lang="en">
            <head>
                <title>Place your vote</title>
            </head>
            <body>
                %s
            </body>
            </html>""" % (result))
