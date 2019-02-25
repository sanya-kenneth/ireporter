let redflagType = "red-flag";
let interventionType = "interventions";

let showRedflags = () => {
    window.location.href = "../templates/change-status.htm"
}
let showInterventions = () => {
    window.location.href = "../templates/change-status-imtervention.htm"
}

let showResolved = () => {
    window.location.href = "../templates/resolved.html"
}

let showDraft = () => {
    window.location.href = "../templates/draft.html"
}

let showunderInv = () => {
    window.location.href = "../templates/investigation.html"
}

let showRejected = () => {
    window.location.href = "../templates/rejected.html"
}

let urlStatistics = (recordType) => {
    if(recordType === 'red-flag'){
        return 'https://ireporterch3.herokuapp.com/api/v1/red-flags'
    }
    else{
        return 'https://ireporterch3.herokuapp.com/api/v1/interventions'
    }
}

let redflagData = [];
let interventionData = [];
let draftRecords = [];
let resolvedRecords = [];
let underInvestigationRecords = [];
let rejectedRecords = [];
let totalRedflags = document.getElementById("total_redflags");
let totalInterventions = document.getElementById("total_interventions");
let resolvedRecordsArea = document.getElementById("resolved_records");
let draftRecordsArea = document.getElementById("draft_records");
let underInvestigationRecordsArea = document.getElementById("under_investigation_records");
let rejectedRecordsArea = document.getElementById("rejected_records");


const fetchRecords = (recordtypeSelected) => {
    fetch(urlStatistics(recordtypeSelected),{
        method: 'GET',
        headers: {
                    'Content-type': 'application/json',
                    "Authorization": sessionStorage.getItem("access_token"),
                }
    })
    .then((res) => res.json())
    .then((data) => {
        data.data.forEach(recordElement => {
            if (recordElement.record_type == "red-flag"){
                redflagData.push(recordElement);
            }
            if (recordElement.record_type == "intervention"){
                interventionData.push(recordElement);
              
            }
            if (recordElement.status == "Draft"){
                draftRecords.push(recordElement);
            }
            if (recordElement.status == "resolved"){
                resolvedRecords.push(recordElement);
            }
            if (recordElement.status == "under investigation"){
                underInvestigationRecords.push(recordElement);
            }
            if (recordElement.status == "rejected"){
                rejectedRecords.push(recordElement);
            }
            
        });
        localStorage.setItem("redflag_number", redflagData.length);
        localStorage.setItem("intervention_number", interventionData.length);
        totalRedflags.innerHTML = localStorage.getItem("redflag_number");
        totalInterventions.innerHTML = localStorage.getItem("intervention_number");
        resolvedRecordsArea.innerHTML = resolvedRecords.length;
        draftRecordsArea.innerHTML = draftRecords.length;
        underInvestigationRecordsArea.innerHTML = underInvestigationRecords.length;
        rejectedRecordsArea.innerHTML = rejectedRecords.length;
        localStorage.setItem("resolvedList", JSON.stringify(resolvedRecords));
        localStorage.setItem("draftList", JSON.stringify(draftRecords));
        localStorage.setItem("underInv", JSON.stringify(underInvestigationRecords));
        localStorage.setItem("rejectedList", JSON.stringify(rejectedRecords));
       
    })

}

let displayResolved = () => {
    let resolvedList = JSON.parse(localStorage.getItem("resolvedList"));
    resolvedList.forEach(resolved => {
        let resolvedDisplay = document.getElementById("resolved_display");
        let commentResolved = document.createElement("div");
        let resolvedType = document.createElement("div");
        let hr = document.createElement("hr")
        commentResolved.innerHTML = `<p> Comment: ${resolved.comment}</p>`;
        resolvedType.innerHTML = `<h4> Record type: ${resolved.record_type} </h4>`;
        resolvedDisplay.appendChild(resolvedType)
        resolvedDisplay.appendChild(commentResolved);
        resolvedDisplay.appendChild(hr)
    });
    }

let displayDraft = () => {
    let draftList = JSON.parse(localStorage.getItem("draftList"));
    draftList.forEach(draft => {
        let draftDisplay = document.getElementById("draft_display");
        let hr = document.createElement("hr")
        let commentDraft = document.createElement("div");
        let draftType = document.createElement("div");
        commentDraft.innerHTML = `<p> Comment: ${draft.comment}</p>`;
        draftType.innerHTML = `<h4> Record type: ${draft.record_type} </h4>`;
        draftDisplay.appendChild(draftType)
        draftDisplay.appendChild(commentDraft);
        draftDisplay.appendChild(hr)

    })
}


let displayunderInv = () => {
    let underInvList = JSON.parse(localStorage.getItem("underInv"));
    underInvList.forEach(inv => {
        let invDisplay = document.getElementById("inv_display");
        let hr = document.createElement("hr")
        let commentinv = document.createElement("div");
        let invType = document.createElement("div");
        commentinv.innerHTML = `<p> Comment: ${inv.comment}</p>`;
        invType.innerHTML = `<h4> Record type: ${inv.record_type} </h4>`;
        invDisplay.appendChild(invType);
        invDisplay.appendChild(commentinv);
        invDisplay.appendChild(hr)

    })
}

let displayRejected = () => {
    let rejectedList = JSON.parse(localStorage.getItem("rejectedList"));
    rejectedList.forEach(reject => {
        let rejectDisplay = document.getElementById("reject_display");
        let hr = document.createElement("hr")
        let commentreject = document.createElement("div");
        let rejectType = document.createElement("div");
        commentreject.innerHTML = `<p> Comment: ${reject.comment}</p>`;
        rejectType.innerHTML = `<h4> Record type: ${reject.record_type} </h4>`;
        rejectDisplay.appendChild(rejectType);
        rejectDisplay.appendChild(commentreject);
        rejectDisplay.appendChild(hr)

    })
}
    

