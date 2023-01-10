const countries = new Map();

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
  const collection = document.querySelectorAll("[id=team]");

  for (const team of collection) {

    let selector = team.getElementsByClassName("teamsSelect")[0];
    let image = team.getElementsByClassName("teamImg")[0];

    selector.addEventListener("change", function () {
    image.src = countries.get(this.value);
    });

    for (let [key, value] of countries) {
      var opt = document.createElement("option");
      opt.value = key;
      opt.innerHTML = key;
      selector.appendChild(opt);
      }
  }
}
