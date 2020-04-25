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
	
function printTable($conn){
	
	$sqlCMD = "SELECT * FROM users;";
	$result = $conn -> query($sqlCMD);
	
	if($result -> num_rows > 0){
		
		echo "<table class='list-db'>";
		echo "<tr>";
		echo "<th>ID</th>"."<th>Username</th>"."<th>Password</th>"."<th>First Name</th>". "<th>Last Name</th>";
		echo "</tr>";
		
		while($row = $result-> fetch_assoc()){	//associative array, using strings as array values. After running, returns false and falls out of loop
			
			echo "<tr>";
			echo "<td>". $row['id'] ."</td>"
				."<td>". $row['usrname']. "</td>"
				."<td>". $row['encrypted_password']. "</td>"
				."<td>". $row['firstName']. "</td>"
				."<td>". $row['lastName']. "</td>";
			echo "</tr>";
		}
		
		echo "</table>";
		
	}
	
	else{
		
		echo "No results found";
		
	}
	
}

function showPost($name){
	
	if (isset($_POST[$name])){
		
		return $_POST[$name];
	}
	
	else{
		
		return "";
		
	}
}

?>
