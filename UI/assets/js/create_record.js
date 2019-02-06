function remove_error(){
    document.getElementById("error_box").style.display = 'none';
}

function remove_message(){
    document.getElementById("message_box").style.display = 'none';
}


let url = (recordType) => {
    if(recordType == 'red-flag'){
        return 'http://127.0.0.1:5000/api/v1/red-flags'
    }
    else{
        return 'http://127.0.0.1:5000/api/v1/interventions'
    }
}

const createRecord = (event) => {
    event.preventDefault()
    let incidentType = document.getElementById('select_category').value;
    let comment  = document.getElementById('comment').value;
    let latCordinate = document.getElementById('lat_cordinate').value;
    let longCordinate  = document.getElementById('long_cordinate').value;
    let incidentLocation = [latCordinate, longCordinate]

    fetch(url(incidentType), {
          method: 'POST',
          mode: 'cors',
          headers: {
              'Content-type': 'application/json',
              "Authorization": sessionStorage.getItem("access_token")
          },
          body: JSON.stringify({
               "incident_type": incidentType,
               "location": incidentLocation,
               "comment": comment,
          })
    })
    .then((response) => response.json())
    .then((data) => {
        if(data.status == 201){
            let message_box = document.getElementById("message_box");
            message_box.innerHTML = data.message;
            message_box.style.display = 'block';
            setTimeout(remove_message, 3000)
       }
       else{
           let error_box = document.getElementById("error_box");
           error_box.innerHTML = data.error;
           error_box.style.display = 'block';
           setTimeout(remove_error, 3000)
           
       }
    })

}