<?php
    $firstname = $_POST['firstname'];
    $lastname = $_POST['lastname'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $password_repeat = $_POST['password_repeat'];

    // Check if passwords match
    if ($password !== $password_repeat) {
        // Passwords don't match, handle the error (e.g., display an error message)
        echo "Passwords do not match. Please try again.";
        exit; // Stop execution further
    }

    // Database connection
    $conn = new mysqli('localhost','root','','test');
    if($conn->connect_error){
        echo "$conn->connect_error";
        die("Connection Failed : ". $conn->connect_error);
    } else {
        // Adjusted SQL query with correct number of placeholders
        $stmt = $conn->prepare("INSERT INTO registration (firstname, lastname, email, password) VALUES (?, ?, ?, ?)");
        
        // Adjusted bind_param to include data types for each parameter
        $stmt->bind_param("ssss", $firstname, $lastname, $email, $password);
        
        $execval = $stmt->execute();
        if($execval === FALSE) {
            echo "Error: " . $stmt->error;
        } else {
            echo "Registration successful...";
        }
        
        $stmt->close();
        $conn->close();
    }
?>

