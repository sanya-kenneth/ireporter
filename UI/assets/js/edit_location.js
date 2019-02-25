let urlLocationEdit = (recordType) => {
    if(recordType === 'red-flag'){
        return 'https://ireporterch3.herokuapp.com/api/v1/red-flags'
    }
    else{
        return 'https://ireporterch3.herokuapp.com/api/v1/interventions'
    }
}


function remove_error(){
    document.getElementById("edit_location_error_box").style.display = 'none';
}

function remove_message(){
    document.getElementById("edit_location_message_box").style.display = 'none';
}

const editLocation = (event) => {
    event.preventDefault();
    let locationrecord_id = localStorage.getItem("incidentDataId");
    let locationrecordCurrentType = localStorage.getItem("incidentDataCurrentType")
    let locationlat = document.getElementById("newlocationlat").value;
    let locationlong = document.getElementById("newlocationlong").value;
    let locationValues = [Number(locationlat), Number(locationlong)];
    fetch(urlLocationEdit(locationrecordCurrentType) + "/" + `${locationrecord_id}` +
    "/" .concat("incident_location"),
    {
        method: 'PATCH',
        mode: 'cors',
        headers: {
                    'Content-type': 'application/json',
                    "Authorization": sessionStorage.getItem("access_token"),
                },
        body: JSON.stringify({
            "location": locationValues,
    })
})
.then((res) => res.json())
.then((data) => {

    if (data.message == `Updated ${locationrecordCurrentType} record's location`){
        let location_form = document.getElementById("edit_location_form");
        let edit_location_message_box = 
        document.getElementById("edit_location_message_box");
        edit_location_message_box.innerHTML = data.message;
        edit_location_message_box.style.display = 'block';
        setTimeout(remove_message, 3000);
        location_form.reset();

    }
    else if(data.message === "incident record not found"){
        let edit_location_error_box = 
        document.getElementById("edit_location_error_box");
        edit_location_error_box.innerHTML = data.message;
        edit_location_error_box.style.display = 'block';
        setTimeout(remove_error, 3000);
    }
    else{
        edit_location_error_box.innerHTML = data.error;
        edit_location_error_box.style.display = 'block';
        setTimeout(remove_error, 3000);
    }


});

}