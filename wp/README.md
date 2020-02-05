# Wordpress and PHP
<sup>Go to this link to get back to the [Politics of Code homepage with syllabus and all information](https://github.com/jbenno/nyuad_politics_of_code/wiki).</sup>

For full reference on php see https://www.php.net/manual/en/

## PHP in Wordpress

The Wordpress provides two user interfaces:
- The admin environment is installed by default under `/wp-admin/`
- The `Theme` which is a collection of php scripts sitting in a folder under `/wp-content/themes/`

Make a new folder under the themes folder and name it something like "simple" or "1".

### Minimal Wordpress Theme
The minimum theme consists of two files: `index.php` and a css style sheet referenced in the `index.php`
- Once oploaded the files of the themes can be edited under the menu option `Appearence\Theme Editor`

This example calls the style sheet and displays the value of the character set variable sitting in the options-table in the sql database.
php-code is bracketed within the tags ```<?php` and ```?```
```html
<!DOCTYPE html>
<html>
	<head>
		<link rel="stylesheet" type="text/css" media="all" href="style.css" />
		<title>Minimal Wordpress Page</title> 
	</head>
	<body>
		<?php bloginfo( 'charset' ); ?>
	</body>
</html>
```

Try different variables, e.g. 
```php
<?php bloginfo( 'stylesheet_url' ); ?>

```

The command ```echo``` prints text back into the html. It can be any text including html-tags:

```html
<!DOCTYPE html>
<html>
	<head>
		<link rel="stylesheet" type="text/css" media="all" href="style.css" />
		<title>Minimal Wordpress Page</title> 
	</head>
	<body>
		<?php
			bloginfo( 'charset' );
			echo "<br>";
			echo "The echo command prints out text that is interpreted as html"
			echo "<br>";
			bloginfo( 'stylesheet_url' );
		?>
	</body>
</html>
```

Reading the variable together with dynamically generating html tags makes Wordpress dynamic:

```html
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
  <head>
    <meta charset="<?php bloginfo( 'charset' ); ?>" />
    <link rel="stylesheet" type="text/css" media="all" href="<?php bloginfo( 'stylesheet_url' ); ?>" />
    <link rel="pingback" href="<?php bloginfo( 'pingback_url' ); ?>" />
    <title><?php bloginfo( 'name' ); ?><?php wp_title( '&mdash;' ); ?></title>
  </head>

  <body <?php body_class(); ?>>
        <h1><a href="<?php bloginfo('url'); ?>"><?php bloginfo( 'name' ); ?></a></h1>
        <p id="description"><?php bloginfo( 'description' ); ?></p> 
  </body>
</html>
```

The basic function call for the site to become managed via the Wordpress database, however, is `the loop`:
```php
<?php
	if ( have_posts() ) : while ( have_posts() ) : the_post();
	endwhile;
	endif
?>
```
... which is sitting in the body of the html page:

```html
<!DOCTYPE html>
<html <?php language_attributes(); ?>>
  <head>
    <meta charset="<?php bloginfo( 'charset' ); ?>" />
    <link rel="stylesheet" type="text/css" media="all" href="<?php bloginfo( 'stylesheet_url' ); ?>" />
    <link rel="pingback" href="<?php bloginfo( 'pingback_url' ); ?>" />
    <title><?php bloginfo( 'name' ); ?><?php wp_title( '&mdash;' ); ?></title>
  </head>

  <body <?php body_class(); ?>>
        <h1><a href="<?php bloginfo('url'); ?>"><?php bloginfo( 'name' ); ?></a></h1>
        <p id="description"><?php bloginfo( 'description' ); ?></p> 

         <?php
         	if ( have_posts() ) : while ( have_posts() ) : the_post();
         ?>
         	<h2><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
         <?php 
            the_content();
         	endwhile;
		else : echo "404 Content not found";
         	endif;
         ?>
  </body>
</html>
```
Documentation of the loop:  
https://developer.wordpress.org/themes/basics/the-loop/



Here you find the files to set up the simple theme including some basic styling:  
https://github.com/jbenno/nyuad_politics_of_code/tree/master/wp/simple_theme
