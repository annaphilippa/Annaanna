#!/usr/local/bin/python3
import cgi
import cgitb

cgitb.enable()
form = cgi.FieldStorage()
username = form.getvalue('submitted-name')

htmlPage = """<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Hello!</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="/style.css">
  </head>
  <body>
    <h1>Hello {username}!</h1>
    <p>I I I</p>
  </body>
</html>""".format(username=username)

print(htmlPage)