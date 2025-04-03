document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("contact-form");
    const responseMessage = document.getElementById("response-message");
    const easterEggMessage = document.getElementById("easter-egg-message");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        // Récupérer le message entré par l'utilisateur
        const userMessage = document.getElementById("message").value.trim();

        // Afficher le message de confirmation
        responseMessage.textContent = "Merci pour votre message !";
        responseMessage.classList.remove("hidden");

        // Vérifier si le message est "Trinity"
        if (userMessage === "Trinity") {
            easterEggMessage.textContent = "Bravo, vous avez découvert un secret ! 🔥";
                }
    });
});
