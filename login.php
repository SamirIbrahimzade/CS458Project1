<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <title>Netflix</title>
    <link rel="icon" href="src/images/icon.png">
    <link rel="stylesheet" href="src/main.css">
</head>
<body>
    <div  class="container">
        <form class="form" id="SignIn" action="sign_in.php" method="post">
            <h1 class="form_title">Sign In</h1>
            <div class="form_message form_error_message"></div>
            <div class="form_input_group">
                <input type="text" id = "email" class="form_input" name="email" autofocus placeholder="Email" required>
                <div class="form_input_error_message"></div>
            </div>
            <div class="form_input_group">
                <input type="password" id = "password" class="form_input" name="password" autofocus placeholder="Password" required>
                <div class="form_input_error_message"></div>
            </div>
            <button id = "loginBtn" class="form_button" type="submit">Sign In</button>
            <p class="form_text">
                <a class="form_link" href="http://localhost/netflix/registration.php" id="LinkCreateAccount"> Sign Up</a>
            </p>
        </form>
    </div>
</body>
</html>
