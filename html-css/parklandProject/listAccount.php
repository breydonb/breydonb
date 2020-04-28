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
	<div class="container">
		<h1>Listing Accounts</h1>
	</div>
	<br />
	<div class="grid-menu">
		<?php printTable($conn); mysqli_close($conn);?>
	</div>
</body>
</html>