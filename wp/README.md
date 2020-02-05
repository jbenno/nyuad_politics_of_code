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


