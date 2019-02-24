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
        console.log(data.data)
        currentUserName.innerHTML = data.data.username;
        displayFirstname.innerHTML = data.data.firstname;
        displayLastname.innerHTML = data.data.lastname;
        displayOthernames.innerHTML = data.data.othernames;
        displayUsername.innerHTML = data.data.username;
        displayPhonenumber.innerHTML = data.data.phonenumber;
        displayUseremail.innerHTML = data.data.useremail;
        displayUserid.innerHTML = data.data.userid;
        if (data.data.usertype == false){
            displayUsertype.innerHTML = "Normal"
        }
    })
}