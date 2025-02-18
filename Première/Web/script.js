function sayHello() {
    alert("Hello World !");
    document.getElementById("texte").innerHTML = "Texte Modifié !";
}

function ajouterElement() {
    const nouvelleLigne = document.createElement("li");
    nouvelleLigne.innerHTML = "Nouvel élément de liste";
    document.getElementById("liste").appendChild(nouvelleLigne);
}