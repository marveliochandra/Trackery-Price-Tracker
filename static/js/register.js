function registerResponse(response){
    switch (response) {
        case "blank":
          alert("Please fill in all fields");
          return false;
        case "accept":
          alert("Please accept Terms and Privacy Policy");
          return false;
        case "email":
          alert("Invalid Email Address");
          return false;
        case "pwlen":
          alert("Password is too short\n");
          return false;
        case "pwmismatch":
          alert("Password and confirm password is not the same");
          return false;
        case "dupeemail":
          alert("Email has been registered, please use another email");
          return false;
        case "ok":
          return true;
      }
}
