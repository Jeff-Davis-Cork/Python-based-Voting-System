#!/usr/local/bin/python3

from cgitb import enable 
enable()

from cgi import FieldStorage, escape
import pymysql as db

from http.cookies import SimpleCookie

from os import environ

cookie=SimpleCookie() # makes an object from class def.
cookie['id']='Votes'  # sets name of cookie to 'votes'
cookie['id']['expires']=157680000 # 5 year exp.  Persistant Cookie
form_data=FieldStorage()
candidate_name=form_data.getfirst('candidate_name')
connection = db.connect(#login)


http_cookie_header = environ.get('HTTP_COOKIE')
if not http_cookie_header: # client did not send cookie
    cursor = connection.cursor(db.cursors.DictCursor)
    cursor.execute("""SELECT candidate_name FROM candidates WHERE candidate_name= %s """ , candidate_name)
    if cursor.rowcount!=1 :
        result=('Sorry, your candidate was not found in the database.')
    else:
        cursor = connection.cursor(db.cursors.DictCursor)
        cursor.execute("""UPDATE candidates SET total_votes = total_votes + 1 WHERE candidate_name=%s""" , candidate_name)
        connection.commit()
        
        result='You vote has been counted. You have been heard!'
else:
    cookie.load(http_cookie_header)# loads the cookie present in HTTP header
    if 'Votes' not in cookie:
        cookie['Votes']=1
        cursor = connection.cursor(db.cursors.DictCursor)
        cursor.execute("""SELECT candidate_name FROM candidates WHERE candidate_name= %s """ , candidate_name)
        if cursor.rowcount!=1:
            result=('Sorry, your candidate was not found in the database.')
        else:
            cursor = connection.cursor(db.cursors.DictCursor)
            cursor.execute("""UPDATE candidates SET total_votes = total_votes + 1 WHERE candidate_name=%s""" , candidate_name)
            connection.commit()
            result='You vote has been counted. You have been heard!'
    else:
        cookie['Votes']=int(cookie['Votes'].value) + 1
        result='''Actually, it looke like you have voted before.
        Nice Try, you can only vote once.'''




print(cookie)
            
print('Content-Type: text/html')
print()

print("""
    <!DOCTYPE html>
        <html lang="en">
            <head>
                <title>You Have Voted!</title>
            </head>
                <body style='background: linear-gradient(to left, #4776E6 , #8E54E9);'>
                    <h1>You have voted for ruler of the world!</h1>
                        <p>
                            <b>%s</b>
                        </p>
                </body>
            </html>""" % (result))


    
                      
