<!doctype html>
<html>
<head>
<?php
function databaseConnection(){
	
		$user = "bbrennan9";
		$password = "bbrennan9";
		$database= "bbrennan9";

		$conn = mysqli_connect("localhost",$user,$password,$database);
		if (mysqli_connect_errno()) 
		{
			die("<b>Failed to connect to MySQL: " . mysqli_connect_error() . "</b>");
		}

		return $conn;
}
	
?>

</head>

<body>
</body>
</html>