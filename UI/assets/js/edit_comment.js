let urlEdit = (recordType) => {
    if(recordType === 'red-flag'){
        return 'http://127.0.0.1:5000/api/v1/red-flags'
    }
    else{
        return 'http://127.0.0.1:5000/api/v1/interventions'
    }
}


const editComment = (event) => {
    event.preventDefault();
    let newrecord_id = localStorage.getItem("incidentDataId");
    let newrecordCurrentType = localStorage.getItem("incidentDataCurrentType")
    let newComment = document.getElementById("newcomment").value;
    console.log(newComment);
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
        console.log(data);
    })

}