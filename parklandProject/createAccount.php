<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Create Account</title>
<link href="style.css" rel="stylesheet" type="text/css">
<?php

	
	if (isset($_POST['test_submit'])) // form loaded itself
	{
		if ($_POST['test_submit'] == "Create Account") // insert new record chosen
			{
					require("library/functions.php");
					$dbconn = databaseConnection();
					
					$usrname= $_POST['usrname'];
					$encrypted_password= $_POST['passwd'];
					$usergroup="user";
					$email="none set";
					$firstName=$_POST['firstName'];
					$lastName=$_POST['lastName'];		
			
					$stmt = $dbconn -> prepare("INSERT INTO users (usrname,encrypted_password,usergroup,email,firstName,lastName) VALUES (?,?,?,?,?,?)");
					$stmt -> bind_param("ssssss",$usrname,$encrypted_password, $usergroup,$email,$firstName,$lastName);
					/*$stmt = $dbconn->prepare("INSERT INTO users (usrname) VALUES (?)");
					$stmt -> bind_param("s",$usrname);*/

					$stmt -> execute();
			
					mysqli_close($dbconn);

					header("Location: welcome.php");
			}
			if ($_POST['test_submit'] == "Cancel") // insert new record chosen
			{
					header("Location: welcome.php");
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
                        <label>First Name:</label>
                        <input type="text" name="firstName">
                        <br>
                        <label>Last Name:</label>
                        <input type="text" name="lastName">
                        <br>
                        <input type="submit" name="test_submit" value="Create Account">
                        <input type="submit" name="test_submit" value="Cancel">
                </form>
        </div>
</body>
</html>
