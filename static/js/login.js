function validateLogin(){
    let email = document.forms["login-input"]["login-email"].value;
    let password = document.forms["login-input"]["login-password"].value;
    let rememberMe = document.forms["login-input"]["rememberMe"].checked;
    if (password == "" || email == "") {
        alert("Please fill in all fields");
        return false;
      }
    // temp checker, to do: check with the database
    // if there is no email starting with that, return false
    // if there is email in database, then check if password hash the same or not
    //email first then password
    //this is user integration to do.
    if(email.endsWith("@gmail.com")==false){
        alert("Invalid Email Address");
        return false;
    }
}
