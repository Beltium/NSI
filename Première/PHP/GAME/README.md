# Projet GAME

Ce projet est un mini-jeu web interactif développé avec HTML, CSS, JavaScript et PHP. Il permet aux utilisateurs de tester leur réactivité, d’enregistrer leur score, puis de consulter un classement.

## Aperçu du projet

Le site web est structuré autour des fonctionnalités suivantes :

- **Jeu interactif** : Test de réactivité avec un mini-jeu web simple.
- **Enregistrement de score** : Les utilisateurs peuvent soumettre leur score à la fin d'une partie.
- **Classement** : Une page affiche les meilleurs scores enregistrés dans un fichier JSON.

## Fonctionnalités

- **Interface simple** : Un design simple et intuitif basé sur le style d'un ancien projet.
- **Sauvegarde des scores** : Les scores sont envoyés à un fichier JSON via un script PHP (`submit.php`).
- **Classement dynamique** : Les scores sont affichés de manière dynamique à l'aide de `classement.php`.
- **Responsive** : Le site est adapté à tous types d’écrans (ordinateur, tablette, mobile).

## Technologies utilisées

- **HTML** : Structure de la page de jeu.
- **CSS** : Mise en forme et responsive design.
- **JavaScript** : Gestion de la logique du jeu.
- **PHP** : Interaction serveur pour enregistrer et lire les scores.
- **JSON** : Stockage des scores côté serveur.

## Installation

1. Clonez ce repository ou téléchargez-le :
   ```bash
   git clone https://github.com/Beltium/NSI.git
   ```
2. Placez le dossier `GAME` sur un serveur local prenant en charge PHP (comme XAMPP, WAMP ou MAMP).
3. Lancez le serveur et ouvrez `index.html` dans votre navigateur :
   ```
   http://localhost/GAME/
   ```

> 📌 Remarque : Assurez-vous que les permissions du fichier `scores.json` permettent l’écriture par le serveur PHP.

## Acknowledgements

- Ce projet a été développé dans un cadre éducatif pour expérimenter les interactions entre JavaScript, PHP et JSON.
- Merci aux enseignants et ressources open source ayant permis la conception de ce jeu web.
