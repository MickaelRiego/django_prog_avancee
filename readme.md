# Journal de développement

## 02/09/2025
- **TD1 terminé** : Toutes les fonctionnalités sont opérationnelles
  - Pages : `home/`, `home/<param>`, `about_us`, `contact_us`

---

## 04/09/2025
- **Modélisation des entités** :
  - Ajout des modèles : **Produit**, **Rayon**, **Catégorie**
  - Migration 002 : Ajout de l’entité **Rayon**
  - Migration 003/004 : Ajout de la table **Contenir** (relation Many-To-Many)
  - Migration 004/005 : Ajout d’une **date de fabrication** pour les produits
  - Migration 005/006 : Ajout de l’entité **Statut** (id, libellé)
  - Migration 006/007 : Ajout d’un **statut** pour chaque produit
- **Problème rencontré** :
  - Difficulté avec les commandes shell pour le **Statut** : la clé étrangère (FK) n’est pas reconnue dans **Produit**

---

## 09/09/2025
- **TP 1 terminé**
- **TD2 commencé** :
  - Premier produit ajouté via la page **admin**

---

## 11/09/2025
- **TD2 terminé** :
  - Tout fonctionne correctement, sans difficulté particulière
- **TP2** :
  - Avancement : page 9
  - Template pour la **liste des produits** créée

---

## 16/09/2025
- **TP2** :
  - **Bootstrap** intégré et fonctionnel
  - TP2 **terminé**

---

## 18/09/2025
- **TD3** :
  - Avancement : page 8
  - Implémentation de :
    - `produitListView`
    - `produitDetailView`
  - **TODO** : `listView` et `detailView` pour les **catégories**

---

## 23/09/2025
- **TODO terminé** :
  - Toutes les vues (`listView`, `detailView`) pour les catégories implémentées
- **Authentification** mise en place
- **Modification de `ContactView`**
- **Prochaine étape** :
  - Page 18 : Finalisation de l’envoi d’**emails** (`email-sent`)

## 25/09/2025
- **TD3 finis**
- **Formlaire création produit** avec validation coté client
- **Vue générique** page 6
- **TO DO** page 7

## 30/09/2025
- **TP3 finis**
- create/delete/change fait pour produit, categorie et rayons
