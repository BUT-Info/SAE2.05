---
title: 'SAÉ 2.05 Gestion d’un projet'
author:
- Léo Tuaillon
- Mathéo Hersan
- Yvan Calatayud
date: 'Mai 2023'
lang: fr-FR
...

\tableofcontents
-------------
Contexte


Notre SAE consiste à manipuler et à analyser un jeu de données libres et ouvertes. Pour ce faire, nous avons sélectionné une base de données des chansons les plus écoutées sur Spotify.

L'objectif de notre projet est d'exploiter ces données pour en extraire des informations pertinentes, des graphiques et des statistiques. Nous avons commencé par trouver des questions sur ces données et définir les statistiques que nous souhaitions obtenir. Par exemple, nous avons chercher à comprendre les tendances du marché musical, à identifier les artistes les plus populaires ou à prévoir la popularité future d'une chanson en fonction de son style et de sa durée.

Après avoir défini nos questions, nous proposerons un modèle de structuration de nos données. Nous utiliserons des outils numériques pour analyser les données et créer une base de données. Ensuite, nous rédigerons un script pour importer les données collectées dans notre base de données, en veillant à traiter les données au préalable pour supprimer les doublons, le cas échéant.

Enfin, nous analyserons nos données et présenterons les résultats sous forme visuelle pour répondre aux questions que nous avons identifiées dans la première partie. Nous utiliserons des packages Python tels que pandas et matplotlib pour faciliter l'analyse et la visualisation des données.

Livrables
---------

- Application fonctionnelle gérant les cas précisés précédemment
- Documentation de l'architecture et du rôle de chaque composant de l'application

Référentiel


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
