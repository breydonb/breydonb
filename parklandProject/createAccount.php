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

	if (isset($_POST['submit'])) // form loaded itself
	{
	    if ($_POST['submit'] == "Create Account") // insert new record chosen
		{
       			$stmt = $conn -> prepare("INSERT INTO users (usrname,encrypted_password,usergroup,email) VALUES (?,?,?,?)");
			$stmt -> bind_param("ssss",$usrname,$encrypted_password, $usergroup,$email);
			$usrname= $_POST['usrname'];
			$encrypted_password=$_POST['passwd'];
			$usergroup="user";
			$email="none set";
			
			$stmt -> execute();

			header("Location: welcome.php");
    		}
    		if ($_POST['submit'] == "Cancel") // insert new record chosen
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
			<input type="text" name="usrname">
			<br>
			<label>Password:</label>
			<input type="password" name="passwd" id="passwd">
			<br>
			<label>Verify Password:</label>
			<input type="password" id="verifyPasswd">
			<br>
			<input type="submit" name="submit" value="Create Account">
			<input type="submit" name="submit" value="Cancel">
		</form>
	</div>
</body>
</html>
