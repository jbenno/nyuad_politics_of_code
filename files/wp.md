<sup>|[&uarr; Back to course home page](/README.md)</sup>  
# Installing and Running a Wordpress Blog

https://docs.google.com/spreadsheets/d/1AYytmijpAMuoYe9XtK-uOeOpou1oVgUVAYqL6gcSTQg/edit?usp=sharing


See also [Wordpress Documentation at https://wordpress.org/support/](https://wordpress.org/support/).

#### Prerequisites
- FTP client (e.g. FileZilla https://filezilla-project.org )
- Webspace with FTP access (read/write/execute) and PHP 7.x running
- sql database on the webspace

#### Webspace
You can use the domains, webspace, ftp-server and database I will provide in class with X from 1 to 6:  
URL `http://nyuadX.f3c.me` 
ftp `ftp.nyuadX.f3c.me`

#### Installation
1. Download the current Wordpress distribution at https://wordpress.org/download/  
If you download the compressed file wordpress-x.x.x.tar you have to decompress it after downloading it. It will unpack into a folder wordpress
2. Prepare wp-config.php
  Open the file `wp-config-sample.php` in an editor.  
  Add the required credentials for the database in lines 22 ff - note: these are different credentials than for the ftp login. You find them in the line "DB" in the Google spreadsheet.
  Input for `DB_NAME` and `DB_USER` for the database are the same.  
  
    *Very Important!*  
  At line 66 change the value of `$table_prefix = 'wp_';` from wp to the name of your subdomain `$table_prefix = 'nyuadX_';`  
  Since we are all using the same database the data of the other installations will be overwritten otherwise.  
  
    Rename the file to `wp-config.php`.
  

3. Transfer (upload) the all files and subfolders in the `/wordpress` folder to your webspace. Put `ftp.nyuadX.f3c.me` (X from 1 to 6 whatever is yours), login and password as provided.
3. Open the url `http://nyuadX.f3c.me` in your browser (X 1 to 6).  
  Select the language.  
  Populate the form - chose a name like wp_admin for the user name; more users can be added later.  
  Generally you should chose an email address that you don't need to work with on this blog later. The administrater email should be seperate from the users.
  Copy the password because it will not be displayed later.
  Log in with the admin user name and the copied password.
  In the Menu go to `users` and add yourself as a user. Set the field `Role` to `Administrator` - otherwise you will not be able to do much.
  Log out, and log in with your user name and password.
  The web user interface you are working in is called `dashboard` and can be accessed under the URL `http://nyuadX.f3c.me/wp_admin`.
  
#### SQL Database
https://w008f8b5.kasserver.com/mysqladmin/kaslogin.php
  
#### Themes
- The "themes" are administrated in the dashboard under the menu item `Appearence`.
- The files for the themes are located in the folder `/wp-content/themes`.
- To install new themes you can upload the theme's files to a new folder under /wp-content/themes

[Here we have a closer look on how the theme scripts work](/files/wp/README.md)


***

<sup>|[&uarr; Back to course home page](/README.md)</sup>  
  
<sup>NYU Abu Dhabi ***[Politics of Code](/README.md)*** by [Joerg Blumtritt](https://jbenno.net) [@jbenno](https://twitter.com/jbenno) - Other classes I teach: [github.com/jbenno](https://github.com/jbenno/teaching/blob/master/README.md)</sup>

