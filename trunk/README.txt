1) Installation: Steps required for someone to take the zip file and make the program work. The target environment and any additional steps required for setup are explained here

Firstly, it is necessary that the computer you run this software on has Python version 3.2.2 with Django version 1.6.5 installed within it.

From a command line, after having changed to the directory that contains the manage.py file in HealthNet (HealthNet/trunk/HealthNet) type "manage.py runserver".
The web server can be viewed from your computer by going to 127.0.0.1:8000 in the address bar of any internet browser. You will then be viewing the site with your own machine as a local host, meaning the site is not live in an actual sense. This software zip file contains the developed site, however it is up to you to choose how you would like to run it as a live site for your business. We the software engineers, are in the business of web development, not web servers! A good place to start looking for a way to run your live site might be to use Apache (http://httpd.apache.org/). Don't be afraid to investigate other places as well.

2) Known bugs and disclaimers.

Disclaimer: This is the first release of the software. It is intended to deliver some, but not all, of the functionality requested by Dr. House. The main objective of this software is not to deliver to Dr. House a final working product for him to deploy for business use but to provide a prototype for his review, and for him to give feedback to the software developers about what he would like to have changed and/or added to a future release.

3) Known missing Release-x features

Statistical data for the users of the system may not be available with this release
Patient tests (such as x-ray, blood tests, etc.) are not yet a part of the system. This means they cannot have associated images yet as well.

4) Basic execution and usage instructions (logins & passwords)

For the purposes of editing the objects within the system, one can (after running the server as described in part (1) of this file) login to the admin page of the site by going to (127.0.0.1:8000/admin) in the address bar and login by using the general administration account:

Login: "admin"
Password: "password"

It is important to realize that the admin account can view/change any user information and thus it should remain secret.

For normal use, go to (127.0.0.1:8000) in the address bar. From there you should be able to engage in the various activites HealthNet provides, such as signing up, sending messages to other users, viewing/creating appointments with other users, etc. While the first release is not the most aesthetically pleasing site, it delivers basic functionality to the users and there are more features to come in future releases.