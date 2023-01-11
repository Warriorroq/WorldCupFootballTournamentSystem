//global variables
const teamsData = new Map();

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
      addOption(team.lastValue, team);
      removeOptionByValue(this.value, team);
      team.lastValue = this.value;
    });

    for (let [key, value] of teamsData) {
      var opt = document.createElement("option");
      opt.value = key;
      opt.innerHTML = key;
      team.selector.appendChild(opt);
    }
  }
}

function removeOptionByValue(value, teamToSkip = null){
  if(value == "")
    return;
  for (const team of teamsBlocks) {
    if(team == teamToSkip)
      continue;
    for (var i=0; i<team.selector.length; i++) {
      if (team.selector.options[i].value == value)
        team.selector.remove(i);
    }
  }
}

function addOption(value, teamToSkip = null) {
  if(value == "")
    return;

  for (const team of teamsBlocks) {
    if(team == teamToSkip)
      continue;

    var opt = document.createElement("option");
    opt.value = value;
    opt.innerHTML = value;
    team.selector.appendChild(opt);
  }
}

