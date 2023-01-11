//global variables
const teamsData = new Map();

const globalEventAnchor = document.getElementById("global-event-anchor");

let teamsBlocks = Array.from(document.querySelectorAll("[id=team]"), i => {
  var block = {
    lastValue : "",
    htmlData : i,
    selector : i.getElementsByClassName("teamsSelect")[0],
    image : i.getElementsByClassName("teamImg")[0]
  }
  return block;
});

//functions
function loadData(){
  eel.readAllCountryImages()(function (result) {
    result.forEach((element) => teamsData.set(element[0], element[1]));
  });
}

function startFunc() {
  document.getElementById("startDiv").style.display = "none";
  loadTeams();
}

function loadTeams() {
  for (const team of teamsBlocks) {
    team.selector.addEventListener("change", function () {
      team.image.src = teamsData.get(this.value);
      globalEventAnchor.dispatchEvent(new CustomEvent("optionChange", {
        detail: {
          last : team.lastValue,
          current: this.value
        }
      }));
      team.lastValue = this.value;
      //removeOptionByValue(this.value);
    });

    for (let [key, value] of teamsData) {
      var opt = document.createElement("option");
      opt.value = key;
      opt.innerHTML = key;
      team.selector.appendChild(opt);
    }
  }
}

function removeOptionByValue(value){
  for (const team of teamsBlocks) {
    let selector = team[1].getElementsByClassName("teamsSelect")[0];
    for (var i=0; i<selectobject.length; i++) {
      if (selectobject.options[i].value == 'A')
        selectobject.remove(i);
    }
  }
}

function addOption(value) {
  for (const team of teamsBlocks) {
    var opt = document.createElement("option");
    opt.value = value;
    opt.innerHTML = value;
    team.selector.appendChild(opt);
  }
}

//main
globalEventAnchor.addEventListener("optionChange", function(event){
  if(event.detail.last != "")
    addOption(event.detail.last);
});
