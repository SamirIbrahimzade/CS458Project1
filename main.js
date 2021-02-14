function display(){
    alert("Hello");
}


function checkUser(){
    
    signInUser = true;
    userMail = document.getElementById("loginMail").value;
    userPassword = document.getElementById("loginPassword").value;
    
   
    if(userPassword == ''){
        alert("Password cannot be blank")
        signInUser = false;
    }
    else if(userMail == ''){
        alert("Email cannot be blank")
        signInUser = false;
    }
    else if(userPassword.length<4 || userPassword.length > 60){
        alert("Password length must be between 4 and 60 characters");
        signInUser = false;
    }
    else if(!userMail.includes("@")){
        alert("Email is not valid");
        signInUser = false;
    }
    else if(!userMail.includes(".")){
        alert("Email is not valid");
        signInUser = false;
    }
    else if(userMail.charAt(userMail.length-1) == "." || userMail.charAt(userMail.length-1) == "@"){
        alert("Email is not valid");
        signInUser = false;
    }

    if(signInUser == true){
        alert("User logged in successfully");
    }

}

function registerUser(){

    //alert("Registered");
    regUser = true;

    userName = document.getElementById("name").value;
    userMail = document.getElementById("email").value;
    userSurname = document.getElementById("surname").value;
    userPassword = document.getElementById("password").value;

    if(userName == ''){
        alert("First name cannot be blank")
        regUser = false;
    }
    else if(userSurname == ''){
        alert("Last name cannot be blank")
        regUser = false;
    }
    else if(userPassword == ''){
        alert("Password cannot be blank")
        regUser = false;
    }
    else if(userMail == ''){
        alert("Email cannot be blank")
        regUser = false;
    }
    else if(userPassword.length<4 || userPassword.length > 60){
        alert("Password length must be between 4 and 60 characters");
        regUser = false;
    }
    else if(!userMail.includes("@")){
        alert("Email is not valid");
        regUser = false;
    }
    else if(!userMail.includes(".")){
        alert("Email is not valid");
        regUser = false;
    }
    else if(userMail.charAt(userMail.length-1) == "." || userMail.charAt(userMail.length-1) == "@"){
        alert("Email is not valid");
        regUser = false;
    }

    if(regUser == true){
        alert("User registered successfully");
    }


}