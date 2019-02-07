let url = (recordType) => {
    if(recordType == 'red-flags'){
        return 'http://127.0.0.1:5000/api/v1/red-flags'
    }
    else{
        return 'http://127.0.0.1:5000/api/v1/interventions'
    }
}

const fetchIncidents = () => {
    let incidentType = document.getElementById("select_type").value
    fetch(url(incidentType), {
        method: 'GET',
        headers: {
                    'Content-type': 'application/json',
                    "Authorization": sessionStorage.getItem("access_token"),
                }
    })
        .then((res) => res.json())
        .then((data) => {
            if('data' in data){
            data.data.forEach(element => {
                let createdBy = element.createdby;
                let recordComment = element.comment;
                let createdOn = element.createdon;
                let recordLocation = element.incident_location;
                let recordId = element.incidentid;
                let incidentRecordType = element.record_type;
                let recordStatus = element.status;
                let display = '<div> </div>';

                display = `
                <table>
                <tbody>
                <tr>
                <td>${createdBy}</td>
                <td>${createdOn}</td>
                <td>${recordComment}</td>
                <td>${recordId}</td>
                <td>${recordLocation}</td>
                <td>${incidentRecordType}</td>
                <td>${recordStatus}</td>
                </tr>
                </tbody>
                </table>
                ` 
                document.getElementById("display_record").innerHTML = display;
                console.log(element)
            });
            }
            else{
                console.log(data)
            }
        })
}
