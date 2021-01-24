<sup>|[&uarr; Back to course home page](/README.md)</sup>  

# Wordpress and PHP
For full reference on php see https://www.php.net/manual/en/

## PHP
[Statistics on webpages running on php](https://w3techs.com/technologies/comparison/pl-js,pl-PHP)


## PHP in Wordpress

The Wordpress provides two user interfaces:
- The admin environment is installed by default under `/wp-admin/`
- The `Theme` which is a collection of php scripts sitting in a folder under `/wp-content/themes/`

Make a new folder under the themes folder and name it something like "simple" or "1".

### Minimal Wordpress Theme
The minimum theme consists of two files: `index.php` and a css style sheet referenced in the `index.php`
- Example files for [index.php](/files/wp/index.php) and [style.css](/files/wp/style.css).
- Once oploaded the files of the themes can be edited under the menu option `Appearence\Theme Editor`

This example calls the style sheet and displays the value of the character set variable sitting in the options-table in the sql database.
php-code is bracketed within the tags ```<?php ``` and ```?```
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
			echo "The echo command prints out text that is interpreted as html";
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

### The Loop

The basic function call for the site to become managed via the Wordpress database, however, is `the loop`:
```php
<?php
	if ( have_posts() ) : while ( have_posts() ) : the_post();
	endwhile;
	endif
?>
```
... which is sitting in the body of the html page. Here is the example with the '}'-brackets:

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
         	if ( have_posts() ) {
         		while ( have_posts() ) {
         			the_post();
         			echo '<h2><a href="'; the_permalink(); echo'">';
         			the_title(); echo'</a></h2>';
         			the_content();
         			} 
         	} else {
         		echo '404 Content not found';
         	}
         ?>

  </body>
</html>
```

### WP_Query

More generally, the content of the site can be queried and displayd using the ```WP_Query()``` function. If I want e.g. to display only posts written by me I can filter the results with the argument ```'author_name' => 'jbenno'```:

```html
         <?php
         	$the_query = new WP_Query(array('author_name' => 'jbenno'));
         	if ( $the_query->have_posts() ) {
         		while ( $the_query->have_posts() ) {
         			$the_query->the_post();
         			echo '<h2><a href="'; the_permalink(); echo'">';
         			the_title(); echo'</a></h2>';
         			the_content();
         			} 
         	} else {
         		echo '404 Content not found';
         	}
         ?>
```

The arguments in ```WP_Query``` can filter by any parameter of the post including values stored in custom variables in the post_meta array. the post_meta value is just a string and can easily get quite confusing, however it offers full flexibility to shape whatever criterea is needed.

Appart from filtering, WP_Query also allows sorting and controlling how many posts to display.  
By defining multiple queries it is possible to display different lineups of posts on the same page.

Documentation of the Loop:  
https://developer.wordpress.org/themes/basics/the-loop/

Documentation of WP_Query:  
https://developer.wordpress.org/reference/classes/wp_query/


Here you find the files to set up the simple theme including some basic styling:  [WP Simple Theme](/files/wp/simple_theme)

***

<sup>|[&uarr; Back to course home page](/README.md)</sup>  
  
<sup>NYU Abu Dhabi ***[Politics of Code](/README.md)*** by [Joerg Blumtritt](https://jbenno.net) [@jbenno](https://twitter.com/jbenno) - Other classes I teach: [github.com/jbenno](https://github.com/jbenno/teaching/blob/master/README.md)</sup>
