function remve_error(){
    document.getElementById("error_box").style.display = 'none';
}

function remve_message(){
    document.getElementById("message_box").style.display = 'none';
}


const logInAdmin = (event) => {
    event.preventDefault()
    let userEmail = document.getElementById('email').value;
    let password = document.getElementById('password').value;

    fetch('http://127.0.0.1:5000/api/v1/users/login/admin', {
          method: 'POST',
          mode: 'cors',
          headers: {
              'Content-type': 'application/json' 
          },
          body: JSON.stringify({
               "email": userEmail,
               "password": password
          })
    })
    .then((response) => response.json())
    .then((data) => {
        if(data.message == "You are now loggedin"){
            let message_box = document.getElementById("message_box");
            message_box.innerHTML = data.message;
            message_box.style.display = 'block';
            setTimeout(remve_message, 3000)
            sessionStorage.setItem("access_token", data.access_token)
            setTimeout(()=>{window.location.href = 
                "../templates/change-status.htm"}, 1000)
            

       }
       else{
           let error_box = document.getElementById("error_box");
           error_box.innerHTML = data.error;
           error_box.style.display = 'block';
           setTimeout(remve_error, 3000)  
       }
    })

}