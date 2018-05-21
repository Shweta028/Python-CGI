#!/usr/bin/python3

import cgi,cgitb
cgitb.enable()

print("Content-type:text/html")
print("")

out=cgi.FieldStorage()
name=out.getvalue('name')
gender=out.getvalue('gen')
if gender=="Male":
	print ("")
	print ("</H1> Hello Mr. "+ name + "!!!</H1>")
elif gender=="Female":
	print ("")
	print ("</H1> Hello Ms. "+ name + "!!!</H1>")
else:
	print ("")
	print ("</H1> Hello dear "+ name + "!!!</H1>")
