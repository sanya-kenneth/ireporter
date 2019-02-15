let urlEdit = (recordType) => {
    if(recordType === 'red-flag'){
        return 'http://127.0.0.1:5000/api/v1/red-flags'
    }
    else{
        return 'http://127.0.0.1:5000/api/v1/interventions'
    }
}

function remove_error(){
    document.getElementById("edit_comment_error_box").style.display = 'none';
}

function remove_message(){
    document.getElementById("edit_comment_message_box").style.display = 'none';
}


const editComment = (event) => {
    event.preventDefault();
    let newrecord_id = localStorage.getItem("incidentDataId");
    let newrecordCurrentType = localStorage.getItem("incidentDataCurrentType")
    let newComment = document.getElementById("newcomment").value;
    fetch(urlEdit(newrecordCurrentType) + "/" + `${newrecord_id}` + "/" .concat("incident_comment"),
    {
        method: 'PATCH',
        mode: 'cors',
        headers: {
                    'Content-type': 'application/json',
                    "Authorization": sessionStorage.getItem("access_token"),
                },
        body: JSON.stringify({
            "comment": newComment,
        })
    })
    .then((res) => res.json())
    .then((data) => {
        if (data.message == `Updated ${newrecordCurrentType} record's comment`){
            let comment_form = document.getElementById("edit_comment_form");
            let edit_comment_message_box = 
            document.getElementById("edit_comment_message_box");
            edit_comment_message_box.innerHTML = data.message;
            edit_comment_message_box.style.display = 'block';
            setTimeout(remove_message, 3000);
            comment_form.reset();
  
        }
        else if(data.message === "incident record not found"){
            let edit_comment_error_box = 
            document.getElementById("edit_comment_error_box");
            edit_comment_error_box.innerHTML = data.message;
            console.log(data.message)
            edit_comment_error_box.style.display = 'block';
            setTimeout(remove_error, 3000);
        }
        else{
            edit_comment_error_box.innerHTML = data.error;
            console.log(data.error)
            edit_comment_error_box.style.display = 'block';
            setTimeout(remove_error, 3000);
        }
    });

}