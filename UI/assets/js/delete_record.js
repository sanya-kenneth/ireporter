let urlDelete = (recordType) => {
    if(recordType === 'red-flag'){
        return 'http://127.0.0.1:5000/api/v1/red-flags'
    }
    else{
        return 'http://127.0.0.1:5000/api/v1/interventions'
    }
}


// Function to delete a record
let deleteMethod = (event) => {
    event.preventDefault();
    let confirmDelete= confirm("Are you sure you want to delete this record?");
    let deleteId = localStorage.getItem("incidentDataId");
    let deleteCurrentType = localStorage.getItem("incidentDataCurrentType");
    if (confirmDelete == true){
        fetch(urlDelete(deleteCurrentType) + "/".concat(deleteId),
        {
            method: 'DELETE',
            mode: 'cors',
            headers: {
                        'Content-type': 'application/json',
                        "Authorization": sessionStorage.getItem("access_token"),
                    }
    }
    )
    .then((res) => res.json())
    .then((data) => {
        if ("message" in data){
            alert(data.message)
        }
        else{
            alert(error.message)
        }
    })
     
    }
}