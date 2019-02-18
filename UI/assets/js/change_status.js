let redflagValue = document.getElementById("select_type")

let setDefaultType = () => {
    localStorage.setItem("incidentDataCurrentType", "red-flag")
}

let urlEditStatus = (recordType) => {
    if(recordType === 'red-flag'){
        return 'http://127.0.0.1:5000/api/v1/red-flags'
    }
    else{
        return 'http://127.0.0.1:5000/api/v1/interventions'
    }
}

function remove_error_status(){
    document.getElementById("edit_status_error_box").style.display = 'none';
}

function remove_message_status(){
    document.getElementById("edit_status_message_box").style.display = 'none';
}

function switchPageAdmin(){
    if (redflagValue.value == "redflags"){
        localStorage.setItem("incidentDataCurrentType", "red-flag");
        window.location.href = "../templates/change-status.htm";
    } 
    else{
     
        localStorage.removeItem("incidentDataCurrentType");
        localStorage.setItem("incidentDataCurrentType", "intervention");
        window.location.href = "../templates/change-status-imtervention.htm";
    }
    }

const changeRecordStatus = (event) => {
    event.preventDefault();
    let recordToChangeId = localStorage.getItem("incidentDataId");
    let recordToChangeType = localStorage.getItem("incidentDataCurrentType");
    let newStatus = document.getElementById("change_status_select").value;
    fetch(urlEditStatus(recordToChangeType) + "/" + `${recordToChangeId}` + "/" .concat("status"),
    {
        method: 'PATCH',
        mode: 'cors',
        headers: {
                    'Content-type': 'application/json',
                    "Authorization": sessionStorage.getItem("access_token"),
                },
        body: JSON.stringify({
            "status": newStatus,
        })
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.message == `${recordToChangeType} record's status was successfuly updated`){
            let edit_status_message_box = 
            document.getElementById("edit_status_message_box");
            edit_status_message_box.innerHTML = data.message;
            edit_status_message_box.style.display = 'block';
            setTimeout(remove_message_status, 3000);
        }
        else if(data.message === "incident record not found"){
            let edit_status_error_box = 
            document.getElementById("edit_comment_error_box");
            edit_status_error_box.innerHTML = data.message;
            console.log(data.message)
            edit_status_error_box.style.display = 'block';
            setTimeout(remove_error_status, 3000);
        }
        else{
            edit_status_error_box.innerHTML = data.error;
            console.log(data.error)
            edit_status_error_box.style.display = 'block';
            setTimeout(remove_error_status, 3000);
        }


    });

}