document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("form");
    const tBody = document.getElementById("t-body");
    form.addEventListener("input", e => {
        const value = e.target.value;
        if (value) {
            fetch(`database/${value}`)
            .then(res => res.json())
            .then(aircrafts => {
                tBody.innerHTML = "";
                aircrafts.forEach(aircraft => {
                    const tBody = document.getElementById("t-body");
                    const tRow = document.createElement("tr");
                    const tICAO24 = document.createElement("td");
                    const tReg = document.createElement("td");
                    const tOperator = document.createElement("td");
                    const tModel = document.createElement("td");
        
                    tICAO24.textContent = aircraft.icao24;
                    tReg.textContent = aircraft.registration;
                    tOperator.textContent = aircraft.operator;
                    tModel.textContent = aircraft.model;
        
                    tRow.appendChild(tICAO24);
                    tRow.appendChild(tReg);
                    tRow.appendChild(tOperator);
                    tRow.appendChild(tModel);

                    tRow.setAttribute("onclick", `teste(${aircraft.id})`);
        
                    tBody.appendChild(tRow);
                });
            })
        } else {
            tBody.innerHTML = "";
        }
    })
});

function teste(id) {
    window.location.href = `aircraft/${id}`;
}
  