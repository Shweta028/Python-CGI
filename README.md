# Python-CGI 
# Installing apache web server to host HTTP client requests.

sudo apt-get install apache2
sudo service apache2 start

On installing apache2, a file will be created in /var/www/html/index.html
By default the localhost accesses this file on the browser
Type localhost or <localhost IP> i.e 127.0.0.1 on the browser:
  this will load the default page of apache(this means that the apache servive is running successfully)
We need to edit this file for running python CGI from a cgi script

The cgi script is to be saved in cgi-bin folder which is located at 
  /var/www/cgi-bin------In Redhat
  /usr/lib/cgi-bin------In Ubuntu
  
  Save your cgi script here in the cgi-bin folder
  CGI file can be .cgi or .py file
  
Suppose we have created a file named abc.py in cgi-bin, then we need to give path of this file in index.html file in form action attribute
We also need to give execution permission by the command chmod +x abc.py

Then run the html file on browser in the same way.
