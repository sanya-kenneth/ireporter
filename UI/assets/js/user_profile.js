let fetchUserDetails = () => {
    let currentUserName = document.getElementById("logged_user_name");
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
    })
}