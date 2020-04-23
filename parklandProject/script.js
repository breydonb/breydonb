function passwdCheck(){
	
	var passwd = document.getElementById("passwd");
	var verifyPasswd= document.getElementById("verifyPasswd");

	var compareString = passwd.localeCompare(verifyPasswd);

	if(compareString != 0 ){

		alert("incorrect passwod");

	}
}