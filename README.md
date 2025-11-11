# Keylogger Python (avec `pynput`)

## Description

Ce script est un **keylogger simple** écrit en Python.  
Il enregistre les touches pressées et les stocke dans un fichier texte `log.txt`.

> **Bibliothèque utilisée :** `pynput` — permet d'écouter les événements clavier en temps réel.

---

## Fonctionnalités

- Capture les frappes clavier (lettres, chiffres, symboles).
- Traduit certaines **touches spéciales** (espace, entrée, tab, shift, ctrl, alt, caps lock, backspace, échappement).
- Ajoute chaque frappe au fichier `log.txt`.
- Tourne en continu jusqu'à arrêt manuel.

---

## Installation

1. Place le script (par exemple `keylogger.py`) dans le dossier souhaité.

2. Installe la dépendance :

```bash
pip install pynput
