let fetchUserDetails = () => {
    let currentUserName = document.getElementById("logged_user_name");
    let displayFirstname = document.getElementById("user_firstname");
    let displayLastname = document.getElementById("user_lastname");
    let displayOthernames = document.getElementById("user_othernames");
    let displayUsername = document.getElementById("user_username");
    let displayPhonenumber = document.getElementById("user_phonenumber");
    let displayUseremail = document.getElementById("user_email");
    let displayUserid = document.getElementById("user_id");
    let displayUsertype = document.getElementById("user_type");
    fetch('http://127.0.0.1:5000/api/v1/user', 
    {
        method: 'GET',
        headers: {
                    'Content-type': 'application/json',
                    "Authorization": sessionStorage.getItem("access_token"),
                }
    })
    .then((res) => res.json())
    .then((data) => {
        currentUserName.innerHTML = data.data.username;
        if (displayFirstname != null){
            displayFirstname.innerHTML = data.data.firstname;
        }
        if (displayLastname != null){
            displayLastname.innerHTML = data.data.lastname;
        }
        if (displayOthernames != null){
            displayOthernames.innerHTML = data.data.othernames;
        }
        if (displayUsername != null){
            displayUsername.innerHTML = data.data.username;
        }
       if (displayPhonenumber != null){
        displayPhonenumber.innerHTML = data.data.phonenumber;
       }
       if ( displayUseremail != null){
        displayUseremail.innerHTML = data.data.useremail;
       }
       if (displayUserid != null){
        displayUserid.innerHTML = data.data.userid;
       }
        if (data.data.usertype == false){
            if (displayUsertype != null){
                displayUsertype.innerHTML = "Normal";
            } 
        }
        else{
            if(displayUsertype != null){
                displayUsertype.innerHTML = "Administrator";
            }
        }
    })
}