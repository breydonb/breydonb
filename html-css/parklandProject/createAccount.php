<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Create Account</title>
<link href="style.css" rel="stylesheet" type="text/css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<!--<script type="text/javascript">
var check = function() {
  if (document.getElementById('passwd1').value == document.getElementById('passwd').value) {
	  
		document.getElementById('message').style.color = 'green';
		document.getElementById('message').innerHTML = 'matching';
	} 
	
	else {
	
		document.getElementById('message').style.color = 'red';
		document.getElementById('message').innerHTML = 'not matching';
	}
}
</script>-->
<script type="text/javascript">
$('#passwd, #passwd1').on('keyup', function () {
  if ($('#passwd').val() == $('#passwd1').val()) {
    $('#message').html('Matching').css('color', 'green');
  } else 
    $('#message').html('Not Matching').css('color', 'red');
});	
</script>
	
<?php

	require("library/functions.php");
	
	if (isset($_POST['test_submit'])) // form loaded itself
	{
		if($_POST['passwd'] == $_POST['passwd1']){
			
			if ($_POST['test_submit'] == "Create Account") // insert new record chosen
				{
					$dbconn = databaseConnection();
					
					$usrname= $_POST['usrname'];
					$encrypted_password= password_hash($_POST['passwd'], PASSWORD_DEFAULT);
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
			
			else if ($_POST['test_submit'] == "Cancel") // insert new record chosen
				{
					header("Location: welcome.php");
				}
    		}
		
		else{
			
			echo "<script>alert('broke')</script>";
		}
		
	}
		
			   	
		


?>

	
</head>
<body class="account-grid">
        <div id="createItem">
                <form method="POST" class="login-box" >
                        <label>Username:</label>
                        <input type="text" name="usrname" value='<?php echo showPost("usrname")?>'>
                        <br>
                        <label>Password:</label>
                        <input type="password" name="passwd" id="passwd1">
                        <br>
                        <label>Verify Password:</label>
                        <input type="password" name="passwd1" id="passwd"><span id='message'></span>
                        <br>
                        <label>First Name:</label>
                        <input type="text" name="firstName" value='<?php echo showPost("firstName")?>'>
                        <br>
                        <label>Last Name:</label>
                        <input type="text" name="lastName" value='<?php echo showPost("lastName")?>'>
                        <br>
                        <input type="submit" name="test_submit" value="Create Account">
                        <input type="submit" name="test_submit" value="Cancel">
                </form>
        </div>
</body>
</html>
