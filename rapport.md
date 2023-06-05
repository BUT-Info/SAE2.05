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
-----------
Contexte
----------

Notre SAE consiste à manipuler et à analyser un jeu de données libres et ouvertes. Pour ce faire, nous avons sélectionné une base de données des chansons les plus écoutées sur Spotify.

L'objectif de notre projet est d'exploiter ces données pour en extraire des informations pertinentes, des graphiques et des statistiques. Nous avons commencé par trouver des questions sur ces données et définir les statistiques que nous souhaitions obtenir. Par exemple, nous avons chercher à comprendre les tendances du marché musical, à identifier les artistes les plus populaires ou à prévoir la popularité future d'une chanson en fonction de son style et de sa durée.

Après avoir défini nos questions, nous avons proposé un modèle de structuration de nos données. Nous avons utilisé des outils numériques pour analyser les données et créer une base de données. Ensuite, nous avons rédigé un script pour importer les données collectées dans notre base de données, en veillant à traiter les données au préalable pour supprimer les doublons ainsi que les données incohérentes.

Enfin, nous avons analysé nos données et nous présenterons prochainement les résultats sous forme visuelle pour répondre aux questions que nous avons identifiées dans la première partie. Nous utiliserons des packages Python tels que pandas et matplotlib pour faciliter l'analyse et la visualisation des données.

Genèse de projet
---------
Bien que ce projet nous ait été assigné par notre professeur, il est facile d'imaginer une entreprise ou un client qui pourrait bénéficier d'un tel projet. Une maison de disques, par exemple, serait intéressée par une analyse approfondie des tendances musicales et des goûts des auditeurs. Ces informations pourraient influencer leurs décisions en matière de marketing et de promotion, en ciblant plus efficacement leur public et en adaptant leur offre musicale aux préférences du marché.

Ou de même, Spotify lui-même, ou d'autres plateformes de streaming musical, pourraient trouver une telle analyse utile pour mieux comprendre leurs utilisateurs, optimiser leurs algorithmes de recommandation et améliorer l'expérience utilisateur.

Maître d'oeuvre, d'ouvrage et de projet
---------

En tant que maître d'œuvre, nous avons la responsabilité de la conception et de la réalisation du projet. Nous avons décidé ensemble des méthodes à adopter, des outils à utiliser et du calendrier à respecter pour mener à bien notre mission.

Le maître d'ouvrage est notre professeur, M. Azemar, qui nous a confié ce projet. Il définit les objectifs et les contraintes du projet, valide les choix techniques et s'assure que le résultat correspond à ses attentes.

Pour organiser notre équipe, nous avons opté pour une approche collaborative plutôt qu'hierarchique. En d'autres termes, il n'y avait pas à proprement parler de chef d'équipe. Nous avons préféré mettre en place une structure horizontale, où chacun a la possibilité d'exprimer ses idées et où les décisions sont prises de manière consensuelle. Cette approche a facilité la communication et la collaboration au sein de l'équipe, en permettant à chacun de contribuer à part égale à la réussite du projet.

Chacun de nous a été chargé de certaines tâches en fonction de ses compétences et de ses intérêts. Léo s'est concentré sur l'analyse des données, Mathéo a travaillé sur la conception de la base de données, et Yvan a été en charge de la collecte et du nettoyage des données. Cette répartition des rôles a permis d'optimiser notre travail en tirant parti de nos forces individuelles, tout en veillant à ce que chaque membre de l'équipe ait une compréhension globale du projet.

Nous avons organisé des réunions au début de chaque séance. Durant ces réunions, chacun présentait l'avancement de sa tâche et nous discutions ensemble de la suite du projet. Ces moments ont été essentiels pour maintenir une bonne communication au sein de l'équipe, pour résoudre les problèmes rapidement et pour prendre des décisions éclairées.

Pour faciliter notre communication et notre collaboration, nous avons choisi d'utiliser plusieurs outils. Notion a été notre principal outil de gestion de projet, nous permettant de suivre l'avancement du projet, de partager des ressources et de planifier nos tâches. CodeFirst a été utilisé pour le partage et la collaboration sur le code source du projet. Enfin, pour la communication en temps réel, nous avons utilisé Discord, qui offre des fonctionnalités de chat et d'appel vidéo. Ces outils ont été choisis pour leur facilité d'utilisation, leur flexibilité et leur capacité à favoriser la collaboration à distance.



Livrables
-----------------------------

À la fin de notre projet (SAE 2.04 exploitation de bdd), nous avons livré plusieurs éléments :

- Une base de données bien structurée contenant les données des chansons les plus écoutées sur Spotify. Cette base de données a été nettoyée et est prête à être utilisée pour d'autres analyses ou projets.
- Un ensemble de scripts Python que nous avons utilisés pour collecter, nettoyer et analyser les données. Ces scripts sont documentés et peuvent être réutilisés ou modifiés pour d'autres projets similaires.
- Un rapport détaillé présentant notre méthodologie, nos résultats et nos conclusions. Ce rapport comprend des graphiques et des statistiques pour illustrer nos découvertes.
- Une présentation visuelle de nos résultats, que nous avons préparée pour notre professeur et d'autres parties intéressées.

Niveau de confidentialité
-------------------------

Si un client réel nous avait demandé un tel projet, le niveau de confidentialité aurait été relativement faible, étant donné que nous travaillons avec un jeu de données public trouvé sur Internet. Cependant, il est important de noter que même si les données sont publiques, nous avons toujours une responsabilité envers notre client et envers les utilisateurs de Spotify de respecter leur vie privée et de ne pas utiliser les données de manière abusive.

De plus, si le client avait des données supplémentaires qu'il souhaitait que nous intégrions à notre analyse (par exemple, des données d'écoute spécifiques à leur entreprise), le niveau de confidentialité aurait été plus élevé. Dans ce cas, nous aurions mis en place des mesures de sécurité supplémentaires pour protéger ces données, comme l'utilisation de protocoles de chiffrement et la limitation de l'accès aux données.

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
