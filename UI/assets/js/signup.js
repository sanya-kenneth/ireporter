function remove_error(){
    document.getElementById("error_box").style.display = 'none';
}

function remove_message(){
    document.getElementById("message_box").style.display = 'none';
}

function redirectToLogin(){
    window.location.replace('../templates/index.htm')
}

const signUp = (event) => {
    event.preventDefault()
    let firstName = document.getElementById('firstname').value;
    let lastName  = document.getElementById('lastname').value;
    let otherNames = document.getElementById('othernames').value;
    let userName  = document.getElementById('username').value;
    let userEmail = document.getElementById('email').value;
    let phoneNumber = document.getElementById('phonenumber').value;
    let password = document.getElementById('password').value;

    fetch('http://127.0.0.1:5000/api/v1/users', {
          method: 'POST',
          mode: 'cors',
          headers: {
              'Content-type': 'application/json' 
          },
          body: JSON.stringify({
               "firstname": firstName,
               "lastname": lastName,
               "othernames": otherNames,
               "username": userName,
               "email": userEmail,
               "phonenumber": Number(phoneNumber),
               "password": password
          })
    })
    .then((response) => response.json())
    .then((data) => {
        if(data.status == 201){
            let message_box = document.getElementById("message_box");
            message_box.innerHTML = data.message;
            message_box.style.display = 'block';
            setTimeout(remove_message, 3000)
            setTimeout(redirectToLogin(), 1000)
       }
       else{
           let error_box = document.getElementById("error_box");
           error_box.innerHTML = data.error;
           error_box.style.display = 'block';
           setTimeout(remove_error, 3000)
           
       }
    })

}