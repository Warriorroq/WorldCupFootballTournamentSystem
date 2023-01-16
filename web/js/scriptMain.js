//global variables
const teamsData = new Map();

let teamsBlocks = [...document.querySelectorAll("[id=team]")].map(i => {
  var block = {
    lastValue : "",
    htmlData : i,
    selector : i.getElementsByClassName("teamsSelect")[0],
    image : i.getElementsByClassName("teamImg")[0],
    score : i.getElementsByClassName("score")[0]
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
  removeOptionFromAllSelectorsByValue("None");
  for (const team of teamsBlocks) {
    team.selector.addEventListener("change", function () {
        selectTeamFunc(team, this.value);
    });

    createDefaultOptions(team);
  }
}

function selectTeamFunc(team, value) {
  addOptionToAllSelectors(team.lastValue, team);
  team.image.src = teamsData.get(value);
  removeOptionFromAllSelectorsByValue(value, team);
  team.lastValue = value;
}

function createDefaultOptions(team) {
  var frag = document.createDocumentFragment();
  for (let [key, value] of teamsData) {
    var opt = document.createElement("option");
    opt.value = key;
    opt.innerHTML = key;
    frag.appendChild(opt);
  }
  team.selector.appendChild(frag);
}

function removeOptionFromAllSelectorsByValue(value, teamToSkip = null){
  let option = null;
  if(value == "")
    return;

  for (const team of teamsBlocks) {
    if(team == teamToSkip)
      continue;
    option = team.selector.querySelector(`[value="${value}"]`).style.display = "none";
  }
}

function addOptionToAllSelectors(value, teamToSkip = null) {
  let option = null;
  if(value == "")
    return;

  for (const team of teamsBlocks) {
    if(team == teamToSkip)
      continue;
    option = team.selector.querySelector(`[value="${value}"]`).style.display = "";
  }
}

function sendFirstTourTeamsDataToPython(){
  for (const team of teamsBlocks){
    if(team.lastValue == "")
    {
      var alertDiv = document.getElementsByClassName('alert')[0];
      alertDiv.style.display = "";
      return;
    }
  }
  eel.readDataFromFontEnd(teamsBlocks.map(i => [i.lastValue, i.score.value]))();
  window.location.href = "tournament.html";
}