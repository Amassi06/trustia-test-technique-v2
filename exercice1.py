MAX_WIDTH = 100

phrases = {
    "bloc1": [
        {"texte": "Le code propre facilite la maintenance", "actif": True}
    ],
    "bloc2": [
        {"texte": "Tester souvent évite beaucoup d erreurs", "actif": True},
        {"texte": "Cette phrase ne doit pas s afficher", "actif": False}
    ],
    "bloc3": [
        {"texte": "Cette phrase ne doit pas s afficher", "actif": False},
        {"texte": "Un bon code doit rester simple et clair", "actif": False},
        {"texte": "La simplicité améliore la qualité du code", "actif": True},
        {"texte": "Refactoriser améliore la compréhension", "actif": True}
    ]
}

def afficher_blocs(donnees, largeur):
    bordure = "-" * largeur
    
    mot = False 
    
    for bloc in donnees.values():
        lignes_visibles = []
        for ligne in bloc:
            if ligne["actif"] == True:
                lignes_visibles.append(ligne["texte"].lower()) 
        
        if lignes_visibles:
            mot = True 
            
            print(bordure)
            for texte in lignes_visibles:
                espace = largeur - 2
                print(f"|{texte.rjust(espace)}|")
                
    if mot == True:
        print(bordure)

if __name__ == "__main__":
    afficher_blocs(phrases, MAX_WIDTH)