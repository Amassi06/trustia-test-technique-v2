menu = {
    "entrées": [
        {"nom": "Salade César", "prix": 8, "disponible": True},
        {"nom": "Soupe du jour", "prix": 6, "disponible": False}
    ],
    "plats": [
        {"nom": "Steak frites", "prix": 15, "disponible": True},
        {"nom": "Poisson grillé", "prix": 14, "disponible": True},
        {"nom": "Plat du chef", "prix": 18, "disponible": False}
    ],
    "desserts": [
        {"nom": "Tiramisu", "prix": 7, "disponible": True},
        {"nom": "Glace", "prix": 5, "disponible": True},
        {"nom": "Dessert mystère", "prix": 9, "disponible": False}
    ]
}

def afficher_menu(donnees):
    for categorie, plats in donnees.items():
        plats_visibles = [p for p in plats if p["disponible"]]
        
        if plats_visibles:
            print(f"--- {categorie.lower()} ---")
            for plat in plats_visibles:
                nom = plat["nom"].lower()
                print(f"{nom} - {plat['prix']}€")
            print()
            

if __name__ == "__main__":
    afficher_menu(menu)