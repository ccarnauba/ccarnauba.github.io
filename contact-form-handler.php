<?php

if(isset($_POST['submit'])) {
    $name = $_POST['name'];
    $mail_from = $_POST['email'];
    $subject = $_POST['subject'];
    $message = $_POST['message'];

    $mail_to = "ccarnauba@hotmail.com";
    $headers = "From: ".$mail_from;
    $txt = "Email from website, sent by: ".$name.".\n\n".$message;
    
    mail($mail_to, $subject, $txt, $headers);
    header("Location: index.php?mailsend");
}