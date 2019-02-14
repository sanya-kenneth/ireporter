function remove_error(){
    document.getElementById("error_box").style.display = 'none';
}

let currenttype;

let url = (recordType) => {
    if(recordType === 'red-flag'){
        return 'http://127.0.0.1:5000/api/v1/red-flags'
    }
    else{
        return 'http://127.0.0.1:5000/api/v1/interventions'
    }
}

var incidentRecordId;

function switchPage(incidentrecordType){
    console.log(incidentrecordType)
    if (incidentrecordType === "red-flags"){
        window.location.href = "../templates/view-records-user.htm";
    } 
    else{
        window.location.href = "../templates/view-records-intervention.htm";
    }
    }



let returnType = (theType) => {
    currenttype = theType;
    return theType
}

let showData = (data) => {
    data.forEach(incident => {
        let recordDataId = document.createElement("h6");
        let infoType = document.createElement("h6");
        let contentHeaders = document.createElement("div");
        let datacard = document.createElement("div");
        let hr = document.createElement("hr");
        let metaData1 = document.createElement("div");
        let metaData2 = document.createElement("div");
        let msgBody = document.createElement("div");
        let infoIdheader = `<h6> Incident Id: ${incident.incidentid}</h6>`;
        let infoTypeheader = `<h6> Incident type: ${incident.record_type} </h6>`;
       
        let comment = `<article id="comment" onclick=
        "fetchOneIncident(${incident.incidentid}); activateModal();
        returnType(${incident.record_type});  "> ${incident.comment} </article>`
        recordDataId.textContent = incident.incidentid;
        infoType.textContent = incident.record_type;
        recordDataId.setAttribute("id", "incident_id");
        metaData1.setAttribute("id", "meta_data1");
        metaData2.setAttribute("id", "meta_data2");
        infoType.setAttribute("id", "record_type");
        datacard.setAttribute("id", "data_card");       
        metaData1.innerHTML = infoIdheader;
        metaData2.innerHTML = infoTypeheader ;
        msgBody.innerHTML = comment;
        contentHeaders.appendChild(metaData1);
        contentHeaders.appendChild(metaData2);
        datacard.appendChild(contentHeaders);
        datacard.appendChild(hr);
        datacard.appendChild(msgBody);

        let display = document.getElementById("display_record");
        display.appendChild(datacard);       
    });
   

}

let fetchOne = (data) => {
   let dataRecordType = document.getElementById("record_type_data");
   let dataRcordCreatedBy = document.getElementById("created_by_data");
   let dataRecordCreatedOn = document.getElementById("created_on_data");
   let dataRecordComment = document.getElementById("record_comment_data");
   let dataRecordLocation = document.getElementById("location_data");
   let dataRecordStatus = document.getElementById("record_status");
   dataRecordType.innerHTML = data.record_type;
   dataRcordCreatedBy.innerHTML = data.createdby;
   dataRecordCreatedOn.innerHTML = data.createdon;
   dataRecordComment.innerHTML = data.comment;
   dataRecordLocation.innerHTML = data.incident_location;
   dataRecordStatus.innerHTML = data.status;
}

const fetchIncidents = (incidentRecordType) => {
    
    fetch(url(incidentRecordType), {
        method: 'GET',
        headers: {
                    'Content-type': 'application/json',
                    "Authorization": sessionStorage.getItem("access_token"),
                }
    })
        .then((res) => res.json())
        .then((data) => {
            if ('data' in data){
                showData(data.data)
      
            }
            else if('message' in data){
                let error_box = document.getElementById("error_box");
                error_box.innerHTML = data.message;
                error_box.style.display = 'block';
                console.log(data);
            }
            else{
                let error_box = document.getElementById("error_box");
                error_box.innerHTML = data.error;
                console.log(data.message);
                error_box.style.display = 'block';
            }
        })
       
}

const fetchOneIncident = (recordId) => {
    
    fetch(url(currenttype) + "/".concat(recordId), {
        method: 'GET',
        headers: {
                    'Content-type': 'application/json',
                    "Authorization": sessionStorage.getItem("access_token"),
                }
    })
        .then((res) => res.json())
        .then((data) => {
            if ('data' in data){
                fetchOne(data.data)
      
            }
            else if('message' in data){
                let error_box = document.getElementById("error_box");
                error_box.innerHTML = data.message;
                error_box.style.display = 'block';
                console.log(data);
            }
            else{
                let error_box = document.getElementById("error_box");
                error_box.innerHTML = data.error;
                console.log(data.message);
                error_box.style.display = 'block';
            }
        });
    }

// Get the modal
var modal = document.getElementById("dataModal");

// Get the button that opens the modal
var activate = document.getElementById("comment");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
function activateModal() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
function closeModal() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

let switchTab = (event, tabName) => {
    let i, tabcontent, tabLink;
    document.getElementById("Record_details").style.display = "block";
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tabLink = document.getElementsByClassName("tablinks");
    for (i = 0; i < tabLink.length; i++){
        tabLink[i].className = tabLink[i].className.replace("active", "");

    }
    document.getElementById(tabName).style.display = "block";
    event.currentTarget.className += " active";

}
let detailsView = () => {
    let viewInfo = document.getElementById("Record_details");
    viewInfo.style.display = "block";
}

