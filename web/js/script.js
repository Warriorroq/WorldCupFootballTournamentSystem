const countries = new Map();
const teams = document.querySelectorAll("[id=team]");
const globalEventAnchor = document.getElementById("global-event-anchor");

globalEventAnchor.addEventListener("optionChange", function(){
  console.log("changed");
});
function startFunc() {
  document.getElementById("startDiv").style.display = "none";
  loadTeams();
}

function loadData(){
  eel.readAllCountryImages()(function (result) {
    result.forEach((element) => countries.set(element[0], element[1]));
  });
}

function loadTeams() {
  for (const team of teams) {

    let selector = team.getElementsByClassName("teamsSelect")[0];
    let image = team.getElementsByClassName("teamImg")[0];

    selector.addEventListener("change", function () {
      image.src = countries.get(this.value);
      globalEventAnchor.dispatchEvent(new CustomEvent("optionChange", {
        
      }));
      //add last option
      //call global event
    });

    for (let [key, value] of countries) {
      var opt = document.createElement("option");
      opt.value = key;
      opt.innerHTML = key;
      selector.appendChild(opt);
    }
  }
}

function removeOptionByValue(){
  //remove option
}

function addOption(value, key) {
  for (const team of teams) {
    let selector = team.getElementsByClassName("teamsSelect")[0];
    let image = team.getElementsByClassName("teamImg")[0];
    var opt = document.createElement("option");
    opt.value = key;
    opt.innerHTML = key;
    selector.appendChild(opt);
    }
}