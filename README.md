# Simulations de Physique Moderne - MI4-K-1

Ce dépôt regroupe un ensemble de scripts de simulation numérique en Python développés dans le cadre du module de Physique Moderne. L'objectif est d'illustrer et de visualiser graphiquement des concepts clés de la mécanique quantique et ondulatoire (propagation d'ondes, paquets d'ondes, effet tunnel, effet Hartman).

---

## Note sur l'historique du dépôt

> [!IMPORTANT]
> Suite à une perte accidentelle de fichiers locaux et aux manipulations nécessaires pour récupérer le projet, **l'historique des commits précédents a été réinitialisé**. 
> Néanmoins, l'intégralité du travail, des codes source et des algorithmes a été partagée et redistribuée de manière équivoque entre les membres du projet pour garantir la continuité du travail.

---

##  Description des fichiers

Le projet est composé des scripts suivants :

### 1. `PaquetOndes (1).py`
* **Description :** Simulation et animation de l'évolution temporelle d'un paquet d'ondes gaussien quantique libre (relation de dispersion de Schrödinger).
* **Fonctionnalités :** Calcule et affiche la densité de probabilité $|\psi(x,t)|^2$, la partie réelle et la partie imaginaire. Affiche en temps réel la position du maximum, la dispersion $\Delta x$ (étalement du paquet) et vérifie la conservation de la norme.
* **Contributeurs :** P. Akridas (Physique) & Claude AI (Interface graphique/Animation).

### 2. `OndePlane.py` & `OndePlane1d4E.py`
* **Description :** Génération et visualisation d'ondes planes monocromatiques complexes en 1D et étude de leur superposition.
* **Fonctionnalités :** * `OndePlane.py` : Permet de superposer plusieurs ondes planes avec différents nombres d'ondes $k$ pour comprendre la transition vers un paquet d'ondes. Gère les relations de dispersion linéaires et de Schrödinger.
  * `OndePlane1d4E.py` : Un script minimaliste pour observer le déphasage entre la partie réelle et imaginaire d'une onde plane à un instant $t$ donné.

### 3. `Resolution eq sch.py`
* **Description :** Résolution numérique de l'équation de Schrödinger dépendante du temps (TDSE) appliquée à l'**effet tunnel**.
* **Fonctionnalités :** Un paquet d'ondes initial est projeté contre une barrière de potentiel rectangulaire d'une hauteur $V_0 = 5 \text{ eV}$. Le script propose une animation de la transmission et de la réflexion de la densité de probabilité à travers la barrière.

### 4. `temps-caractéristique.py`
* **Description :** Étude théorique et graphique de l'**effet Hartman**.
* **Fonctionnalités :** Compare le temps de traversée classique d'une particule libre face au temps de traversée quantique par effet tunnel en fonction de l'épaisseur de la barrière ($a$). Met en évidence la saturation du temps de traversée pour les barrières épaisses (vitesse de phase quasi-infinie).

---

##  Installation et Dépendances

Pour exécuter ces simulations sur votre machine, vous devez disposer de Python 3 et des bibliothèques scientifiques standards.

1. **Clonez le dépôt :**
   ```bash
   git clone [https://github.com/votre-nom-utilisateur/Physique-Moderne-MI4-K-1.git](https://github.com/votre-nom-utilisateur/Physique-Moderne-MI4-K-1.git)
   cd Physique-Moderne-MI4-K-1
