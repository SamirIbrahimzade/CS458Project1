<?php
session_start();

$connect = mysqli_connect('eu-cdbr-west-03.cleardb.net', 'be555d81b53d34','d87c6d4d');
mysqli_select_db($connect, 'mysql db');

$first_name = $_POST['first_name'];
$last_name = $_POST['last_name'];
$email = $_POST['email'];
$password = $_POST['password'];

$result = " SELECT * FROM `user_info` WHERE `email` = '$email'";
$number = mysqli_num_rows(mysqli_query($connect, $result));

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


if($number == 1){
    echo "This email already taken";
}
else{
    header('location:login.php');

    $register = "INSERT INTO `user_info`(`first_name`, `last_name`,`email`, `password`) VALUES ('$first_name', '$last_name', '$email', '$password')";
    mysqli_query($connect, $register);
    echo "Registration successful.";
}
?>
