---
title: 'SAÉ 2.05 Gestion d’un projet'
author:
- Clément Fréville
- Bastien Ollier
date: 'Mai 2022'
lang: fr-FR
...

\tableofcontents

Contexte
========

Une entreprise de jeu vidéo souhaite intégrer un système d'objets dans un logiciel pour ordinateur.
Les objets sont être référençables par leur nom et chaque objet a des capacités qui lui sont propres. L'utilisateur dispose d'objets au début et peut en récupérer dans l'environnement décrit par le jeu vidéo.
Le joueur a la capacité d'obtenir de nouveaux objets en combinant d'autres objets. Par exemple, trois "bâtons" forment une fois assemblés un "javelot".

Livrables
---------

- Application fonctionnelle gérant les cas précisés précédemment
- Documentation de l'architecture et du rôle de chaque composant de l'application

Référentiel
===========

Décomposition des tâches
------------------------

Écrire les algorithmes
- Trouver une structure de données
- Implémenter cette structure de données
- Trouver un algorithme de recherche
Documenter l'application
- Écrire des descriptions courtes
- Étudier la complexité
- Rédiger un rapport
- Écrire un script de déploiement
Développer l'interface utilisateur
- réaliser un menu
- relier vue et modèle
- vérifier les entrées utilisateur

Tâches identifiées
------------------

- 1h : Définir les objets
- 2h : Implémenter la liste d'adjacence (antécédent : objets)
- 3h : Implémenter la matrice d'adjacence (antécédent : objets)
- 1h : Implémenter l'algorithme de recherche (antécédents : structures de données)
- 2h : Extraire une base commune (antécédent : implémentation)
- 1h : Comparer les implémentations (antécédent : base commune)
- 3h : Écrire la documentation (antécédents ?)

- 1h : Implémenter la persistence des données
- 2h : Créer un menu

Contraintes
-----------

Coût prévisionnel
-----------------

Ce projet nécessite une long développement informatique et demande plusieurs développeurs pour être en mesure de livrer le projet dans les temps. Le projet aura également besoin de faire appel à un graphiste pour les différents éléments visuels de l'interface graphique. L'entreprise a besoin de locaux, d'équipements informatiques et fait le choix de faire appel à des sociétés extérieures pour l'hébergement de son code informatique et la publication des versions finales.

|Domaine|Nombre|Durée|Coût prévisionnel|
|----|--|--|----|
|Developpeurs|2|2 mois|2 × 2500€/mois = 10000€|
|Artiste|1|1 mois|2000€|
|Locaux|30 m2|2 mois|3000€|
|Logiciels|3|2 mois|400€|
|Hébergement|1|2 mois|50 €|
|Publication|1|unique|30 €|

Dates jalons
------------

Les tâches de documentation marquent la fin des étapes importantes. Elles marquent l'aboutissement d'un cycle de développement.

PERT temps
