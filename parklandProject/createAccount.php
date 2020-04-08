<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Create Account</title>
<link href="style.css" rel="stylesheet" type="text/css">
<?php

function databaseConnection(){
	
	$user = "bbrennan9";
	$password = "bbrennan9";
	$database= "bbrennan9";
	
	$conn = mysqli_connect("localhost",$user,$password,$database);
	if (mysqli_connect_errno()) {                                                        
        die("<b>Failed to connect to MySQL: " . mysqli_connect_error() . "</b>");        
    }                                                                                    
                                                                                         
    return $conn;

	if (isset($_POST['selection'])) // form loaded itself
	{

    if ($_POST['selection'] == "Create Account") // insert new record chosen
    {
        // store the record (next slide) 
        header("Location: welcome.php");
    }
    if ($_POST['selection'] == "Cancel") // insert new record chosen
    {
        header("Location: welcome.php");
    }
	}

	
}


?>
</head>

<body>
	<div class="login-box">
		<form method="POST">
			<label>Username:</label>
			<input type="text" name="Username">
			<br>
			<label>Password:</label>
			<input type="password" id="passwd">
			<br>
			<label>Verify Password:</label>
			<input type="password" id="verifyPasswd">
			<br>
			<input type="submit" value="Create Account">
			<input type="submit" value="Cancel">
		</form>
	</div>
</body>
</html>
