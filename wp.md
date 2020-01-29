# Installing and Running a Wordpress Blog
<sup>[Back to the course wiki](https://github.com/jbenno/nyuad_politics_of_code/wiki/01#wordpress)</sup>

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
  Add the required credentials for the database in lines 22 ff  
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
  
#### Themes
- The "themes" are administrated in the dashboard under the menu item `Appearence`.
- The files for the themes are located in the folder `/wp-content/themes`.
- To install new themes you can upload the theme's files to a new folder under /wp-content/themes
- A minimal wordpress theme: [/wp/simple_theme](/wp/simple_theme)  


Upload the files in a folder under `/wp-content/themes/`.  
Now the theme can be activated from the `Appearence` menu.

- The files of the themes can be edited under the menu option `Appearence\Theme Editor`
