# ✋🖥️ Projet de Détection de la Main & Annotation Vidéo avec OpenCV + cvzone

Ce projet combine deux modules principaux :

1. **Interaction en temps réel avec la main via webcam**
2. **Annotation automatique d’une vidéo avec un modèle de détection (YOLO ou autre)**

## 🎯 Objectifs

* Suivre la main avec la webcam en utilisant `cvzone`
* Contrôler dynamiquement une boîte colorée à l’écran avec les mouvements de la main
* Calculer la distance entre les doigts pour déclencher des actions
* Lire une vidéo et l’annoter automatiquement avec un modèle de détection
* Afficher les résultats en temps réel

---

## 🛠️ Technologies utilisées

* **Python 3**
* **OpenCV**
* **cvzone**
* **HandTrackingModule**
* **Un modèle de détection compatible avec `.predict()`** (ex : YOLOv8)

---

## 📦 Installation

Installe les dépendances nécessaires :

```bash
pip install opencv-python cvzone
```

> Assure-toi également que ton modèle de détection est correctement chargé et possède une méthode `.predict()`.

---

## 📁 Structure du projet

```
projet-main-video/
│
├── main.py               # Script principal
├── input_video/          # Dossier contenant la vidéo d’entrée
├── README.md
└── requirements.txt      # (optionnel)
```

---

## ▶️ Utilisation

### 🎮 Mode Interaction Main (Webcam)

Lance la webcam et interagis avec un rectangle à l’écran. Si tu rapproches les doigts (index & majeur), tu peux **déplacer le rectangle**.

```bash
python main.py
```

* Appuie sur `a` pour quitter la webcam.

### 🎥 Mode Lecture & Annotation de Vidéo

À la fin du script, une vidéo est lue depuis le chemin :

```python
video_path = 'input_video/test2.mp4'
```

Le modèle détecte les objets frame par frame, affiche les résultats annotés, et accélère le traitement avec un **frame skip** pour plus de fluidité.

---

## 📌 Fonctionnalités

* ✅ Suivi du doigt (landmark n°8) via HandTrackingModule
* ✅ Détection de la distance entre les doigts
* ✅ Déplacement d’un rectangle si les doigts sont assez éloignés
* ✅ Affichage dynamique de la couleur du rectangle selon l’interaction
* ✅ Annotation d’une vidéo avec prédictions visuelles
* ✅ Lecture accélérée des vidéos

---

## 🖼️ Exemple visuel

*Rectangle contrôlé par la main (webcam) + résultats de détection sur vidéo*

<img src="assets/exemple_interaction.png" width="400"/>  
<img src="assets/exemple_video.png" width="400"/>

---

## 👤 Auteur

**Mohamed Amine Jemni**
Étudiant à Sup’Com | Passionné par la vision par ordinateur

