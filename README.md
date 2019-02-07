# Savings-Calculator
AWS EC2 Ubuntu Instance, HTML5, Bootstrap, JavaScript (jQuery), Flask, wsgi, Apache, HTTPS
Author: Maithri Santhana Gopala Krishnan

Description:
A simple savings calculator designed and implemented using HTML5, Bootstrap and JavaScript (jQuery).  The implementation uses Flask - a python web framework which provides a simple interface – wsgi (Web Server Gateway Interface) to generate dynamic responses to web requests.  The website is hosted behind Apache and is enabled with a self-signed HTTPS connection.

Objective:
The Savings Calculator is designed with the objective that the users can plan their month ahead of time or can get a perspective, whenever they want to know about their financial status.

Prerequisites: 
To get the web application running, the user must have a:
Web Browser
(No other software installations necessary)

How to use the application:
1.	The user should direct to the following web address in their corresponding web browser.
https://ec2-52-14-104-23.us-east-2.compute.amazonaws.com/

2.	The user should fill in the fields (that apply) of the form by entering the amount in US dollars and click the “Calculate My Monthly Saving” button.  

3.	Once the button is clicked, the user can view the amount that they might save in that particular month.  The green box available in the right side of the webpage with a sign ($) will output the savings amount.

Documentation:
1.	An Amazon Web Services (AWS) EC2 instance is launched with Ubuntu server AMI.
2.	A security group is configured to access HTTP at port 80.
3.	After connecting to the instance, the apache webserver and mod_wsgi are installed.
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi

4.	Flask is installed using pip tool

sudo apt-get install python-pip
sudo pip install flask

5.	A project directory named – saving is created under /var/www/html/

mkdir ~/saving
sudo ln -sT ~/saving /var/www/html/saving

6.	Inside the saving folder folders named – templates is created and the calc_saving.html file is placed inside it.  Using WinSCP, files app.py and saving.wsgi are stored in the saving directory of the remote system.

7.	In the apache configuration file 000-default.conf, the following block is added

WSGIDaemonProcess saving threads=5
WSGIScriptAlias / /var/www/html/saving/saving.wsgi

<Directory saving>
    WSGIProcessGroup saving
    WSGIApplicationGroup %{GLOBAL}
    Order deny,allow
    Allow from all
</Directory>

8.	The apache webserver is restarted.

sudo apachectl restart

9.	To create a self-signed SSL certificate for Apache in Ubuntu, a self-signed key and certificate pair with OpenSSL is created using the command:
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt

10.	 The prompt asking for the country name, state, locality, organization name, department, common name, e-mail address are filled in and the files are stored under /etc/ssl directory.

11.	To create a strong Diffie-Hellman group, 

sudo openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048

12.	A new snippet in the /etc/apache2/conf-available directory is created and the file is named ssl-params.conf

sudo nano /etc/apache2/conf-available/ssl-params.conf

13.	The following code snippet is added to the file using the vi editor.



SSLCipherSuite EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH
SSLProtocol All -SSLv2 -SSLv3
SSLHonorCipherOrder On

Header always set Strict-Transport-Security "max-age=63072000; includeSubdomains"
Header always set X-Frame-Options DENY
Header always set X-Content-Type-Options nosniff

SSLCompression off 
SSLSessionTickets Off
SSLUseStapling on 
SSLStaplingCache "shmcb:logs/stapling-cache(150000)"

SSLOpenSSLConfCmd DHParameters "/etc/ssl/certs/dhparam.pem"

14.	The SSL Virtual Host file is opened to make adjustments.

sudo nano /etc/apache2/sites-available/default-ssl.conf

15.	The SSL, headers modules in Apache and SSL-ready Virtual Host are enabled and Apache server is restarted.

sudo a2enmod ssl
sudo a2enmod headers
sudo a2ensite default-ssl
sudo a2enconf ssl-params
sudo apache2ctl configtest
sudo systemctl restart apache2

16.	 Now a HTTPS security group is configured at port 443 in the EC2 instance and the web page is opened with https:// to see the Savings Calculator.

References from the web: https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-apache-in-ubuntu-16-04 https://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/
