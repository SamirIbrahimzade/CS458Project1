<!DOCTYPE html>
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
    <form class="form" id="CreateAccount" action="sign_up.php" method="post">
            <h1 class="form_title">Create Account</h1>
            <div class="form_message form_error_message" id="sign_up_error"></div>
            <div class="form_input_group">
                <input type="text" class="form_input" name="first_name" autofocus placeholder="First Name" required>
                <div class="form_input_error_message"></div>
            </div>
            <div class="form_input_group">
                <input type="text" class="form_input" name="last_name" autofocus placeholder="Last Name" required>
                <div class="form_input_error_message"></div>
            </div>
            <div class="form_input_group">
                <input type="text" class="form_input" name="email" autofocus placeholder="Email Address" required>
                <div class="form_input_error_message"></div>
            </div>
            <div class="form_input_group">
                <input type="password" class="form_input" name="password" autofocus placeholder="Password" required>
                <div class="form_input_error_message"></div>
            </div>
            <button class="form_button" type="submit">Start Membership</button>
            <p class="form_text">
                <a class="form_link" href="login.php" id="LinkLogin">Already have an account? Sign in</a>
            </p>
        </form>
    </div>
</body>
</html>
