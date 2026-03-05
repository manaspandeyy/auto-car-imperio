<?php
session_start(); // Start session for storing user login status

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve form data
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Database connection
    $con = new mysqli("localhost", "root", "", "test");

    // Check connection
    if ($con->connect_error) {
        die("Connection failed: " . $con->connect_error);
    }

    // Prepare SQL statement to retrieve user data by email
    $stmt = $con->prepare("SELECT * FROM registration WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $result = $stmt->get_result();

    // Check if user with given email exists
    if ($result->num_rows == 1) {
        // Fetch user data
        $user = $result->fetch_assoc();

        // Verify password
        if (password_verify($password, $user['password'])) {
            // Password is correct, set session variables
        
            $_SESSION['email'] = $user['email'];
            // Redirect to dashboard or home page after successful login
            header("Location: index.html");
            exit();
        } else {
            // Password is incorrect
            $error = "Invalid password";
        }
    } else {
        // No user found with given email
        $error = "No account found with that email";
    }

    // Close database connection
    $stmt->close();
    $con->close();
}
?>
