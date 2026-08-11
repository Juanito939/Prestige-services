# Prestige Services — site multi-services (Cameroun)

Site statique, léger, mobile-first. Aucune dépendance payante, aucun serveur nécessaire.

## Structure

```
index.html                    Accueil
services.html                 Liste des 7 services avec tarifs
comment-ca-marche.html        Les 4 étapes du processus
paiement.html                 Numéros Mobile Money + politique de réassurance
contact.html                  WhatsApp + email
services/*.html                Une page par service, avec formulaire de commande
assets/style.css              Toute la mise en forme (un seul fichier, pas de police externe)
assets/script.js              Menu mobile, copie des numéros, envoi des formulaires
generate.py                   Script Python qui a généré les pages (utile si vous voulez
                               modifier un texte partout d'un coup : header, footer, tarifs…)
```

## 1. Mettre le site en ligne gratuitement (GitHub Pages)

1. Créez un compte GitHub (gratuit) si vous n'en avez pas.
2. Créez un nouveau dépôt, par exemple `prestige-services`.
3. Déposez-y tout le contenu de ce dossier (glisser-déposer les fichiers sur github.com,
   ou via `git push` si vous êtes à l'aise avec git).
4. Dans le dépôt : **Settings → Pages → Build and deployment → Source : Deploy from a branch**,
   puis choisissez la branche `main` et le dossier `/ (root)`.
5. Après 1 à 2 minutes, votre site est accessible à une adresse du type
   `https://votre-nom.github.io/prestige-services/`.

Aucune commande, aucun hébergement payant.

## 2. Enregistrer automatiquement les commandes dans Google Sheets

Le site fonctionne déjà sans rien configurer : chaque formulaire ouvre WhatsApp avec
le récapitulatif de la commande. Pour **en plus** garder une trace automatique dans
un Google Sheet, suivez ces 5 étapes (gratuites) :

1. Créez un nouveau Google Sheet, par exemple nommé `Commandes Prestige Services`.
2. Dans ce Sheet : **Extensions → Apps Script**.
3. Supprimez le contenu par défaut et collez ceci :

   ```javascript
   function doPost(e) {
     var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
     var data = JSON.parse(e.postData.contents);
     var headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];

     // Si la feuille est vide, on écrit les en-têtes à partir des clés reçues
     if (sheet.getLastRow() === 0) {
       var keys = Object.keys(data);
       sheet.appendRow(keys);
       headers = keys;
     }

     var row = headers.map(function(h) { return data[h] || ""; });
     sheet.appendRow(row);
     return ContentService.createTextOutput("OK");
   }
   ```

4. Cliquez sur **Déployer → Nouveau déploiement → Type : Application Web**.
   - Exécuter en tant que : **Moi**
   - Qui a accès : **Tout le monde**
   - Cliquez sur **Déployer**, autorisez l'accès, puis copiez l'URL fournie
     (elle ressemble à `https://script.google.com/macros/s/AKfycb.../exec`).
5. Ouvrez `assets/script.js` et collez cette URL ici :

   ```javascript
   window.CONFIG = {
     SHEETS_WEBHOOK_URL: "COLLEZ_VOTRE_URL_ICI",
     WHATSAPP_NUMBER: "237696477138"
   };
   ```

   Republiez le site (ou remplacez le fichier sur GitHub) : chaque commande s'ajoutera
   désormais automatiquement comme une nouvelle ligne dans votre Google Sheet, en plus
   d'ouvrir WhatsApp.

## 3. Ce qu'il faut probablement ajuster

- **Tarifs** : les prix affichés (`generate.py`, variable `SERVICES`, champ `"price"`)
  sont indicatifs — à remplacer par vos vrais tarifs, puis relancer `python3 generate.py`
  pour régénérer toutes les pages.
- **Numéros et email** : déjà en place partout (Orange Money 696 477 138, MTN 680 021 646,
  WhatsApp 696 477 138, claudebell732@gmail.com). Pour les changer, modifiez les variables
  en haut de `generate.py` (`WHATSAPP_NUMBER`, `EMAIL`) et dans `assets/script.js`, puis
  régénérez.
- **Nom du site** : actuellement « Prestige Services » — à personnaliser si besoin
  (rechercher/remplacer dans `generate.py` puis régénérer).

## 4. Modifier le contenu plus tard

Le plus simple est d'éditer `generate.py` (textes, services, champs de formulaire) puis
de relancer :

```bash
python3 generate.py
```

Cela régénère toutes les pages HTML à l'identique, avec vos modifications appliquées
partout d'un coup (plus fiable que d'éditer chaque page HTML à la main).
