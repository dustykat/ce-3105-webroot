# CE 3105 Fluid Mechanics Laboratory for Civil Engineers

This repository is a deployable website for the fluids laboratory at Texas Tech University.  

Users can clone and install the repository onto a webserver, then change the URL to their server IP address.  Most internal links are to http://54.243.252.9 (Use of http protocol is intentional, the server uses a self-signed certificate and most enterprise security will not allow complete connections -- even if users set an exception)

## Suggested steps to replicate http://54.243.252.9/ce-3105-webroot/

1. Clone the repository onto your server (It works with both nginx and apache webservers)
2. As root create a symlink to your server webroot that points to the repository
3. Modify your index page to link to this symlink - verify and you have a working copy
4. Then use `sed` to either search-and-replace all instances of http://54.243.252.9  with http://YourWebrootYourServer
5. Step 4 should work with either DNS or IP entries.  
6. If you omit steps 4 and 5, it will attempt to link to my server - which creates a Cross-Site Scripting situation, and your administrator will likely disallow it - go ahead and fix the links and you will be a lot happier. 

