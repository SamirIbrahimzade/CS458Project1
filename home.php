<?php
session_start();
?>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <title>Netflix</title>
    <link rel="icon" href="src/images/icon.png">
    <link rel="stylesheet" href="src/main.css">
</head>
<body>
<form class="form" id="LogOut" action="log_out.php" method="post">
    <div  class="container message">
        <h1>Welcome to Netflix</h1>
        <button id = "homeBtn" class="form_button log_out" type="submit">Log Out</button>
    </div>
</form>
</body>
</html>
