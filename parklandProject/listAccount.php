<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>List Account</title>
<link href="style.css" rel="stylesheet" type="text/css">
<?php
	
	require("library/functions.php");
	$conn = databaseConnection();
	
	
?>
	
</head>
<body>
	<?php printTable($conn); ?>
</body>
</html>