const gameZone = document.getElementById("gameZone");
const statusText = document.getElementById("status");
const form = document.getElementById("scoreForm");
const inputTime = document.getElementById("reactionTime");

let startTime, timeout;

function resetGame() {
  gameZone.classList.remove("ready");
  gameZone.textContent = "Clique ici quand c’est vert";
  statusText.textContent = "Clique pour commencer…";
  form.style.display = "none";
}

gameZone.addEventListener("click", () => {
  if (gameZone.classList.contains("ready")) {
    const reactionTime = Date.now() - startTime;
    statusText.textContent = `Ton temps de réaction : ${reactionTime} ms`;
    inputTime.value = reactionTime;
    form.style.display = "block";
    gameZone.classList.remove("ready");
  } else if (!startTime) {
    statusText.textContent = "Prépare-toi...";
    timeout = setTimeout(() => {
      gameZone.classList.add("ready");
      gameZone.textContent = "Clique vite !";
      startTime = Date.now();
    }, Math.random() * 3000 + 2000); // entre 2 et 5 s
  } else {
    clearTimeout(timeout);
    statusText.textContent = "Trop tôt ! Clique pour recommencer.";
    startTime = null;
  }
});
