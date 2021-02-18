<?php
session_start();

$connect = mysqli_connect('eu-cdbr-west-03.cleardb.net', 'be555d81b53d34','d87c6d4d');
if (!$connect){
    die("Database Connection Failed");
}
mysqli_select_db($connect, 'mysql db');

$email = $_POST['email'];
$password = $_POST['password'];


$email = $_POST["email"];
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
  $emailErr = "Invalid email format";
  die(json_encode(['error'=>'Invalid email format']));
}

if(strlen($password)>4 && strlen($password)<60){
    $passErr='Password must be between 4 - 60';
}
else{
    die(json_encode(['password'=>'Invalid password format']));

}



$result = " SELECT * FROM `user_info` WHERE `email` = '$email' && `password` = '$password' ";
$number = mysqli_num_rows(mysqli_query($connect, $result));

if($number == 1){
    header('location:http://localhost/netflix/home.php');
}
else {
    header('location:http://localhost/netflix/login.php');
}
?> 

