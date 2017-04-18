#!/usr/local/bin/python3

from cgitb import enable 
enable()

from cgi import FieldStorage, escape
import pymysql as db
            
print('Content-Type: text/html')
print()

form_data = FieldStorage()

result = ''
candidate=''

candidate= form_data.getfirst('candidate')

try:
    if candidate !=None:
        connection = db.connect(# login)
        cursor = connection.cursor(db.cursors.DictCursor)
        cursor.execute("""SELECT candidate_name FROM candidates WHERE candidate_name= %s""" , (candidate))
        if cursor.rowcount==1 :
            result=('Sorry, your candidate was already found in the database.')
        else:
            cursor.execute("""INSERT into candidates (candidate_name, total_votes)
                      values (%s,0)""" , (candidate))
            connection.commit()
            cursor.close()
            connection.close()
            result=('Thanks for adding a candidate!')
    else:
        result=('Go Ahead, enter one!')
except db.Error:
    raise
    result = '<p>Sorry! We are experiencing problems at the moment. Please call back later.</p>'
        
print("""
    <!DOCTYPE html>
        <html lang="en">
            <head>
                <title>Insert Candidate Page</title>
            </head>
                <body style='background: linear-gradient(to left, #4776E6 , #8E54E9);'>
                    <h1>Welcome to my voting page for ruler of the world</h1>
                        <form action="insert_candidate.py" method="post">
                            <label>Enter in a candidate to vote for: </label>
                            <p>
                            <input name='candidate' type="text" name="Who Do you want to vote for?" placeholder='Enter a candidate name here'>
                            </p>
                            <p>
                            <input type="submit" value="Add my candidate!">
                            </p>
                        <p>
                            <b>%s</b>
                        </p>
                        </form>
                </body>
            </html>""" % (result))
