import json
FICHIER = "depenses.json"
def charger():
       try:
             with open(FICHIER, "r", encoding="utf-8") as f:
                    return json.load(f)
       except FileNotFoundError:
              return []
def sauvegarder():
       with open(FICHIER, "w", encoding="utf-8") as f:
              json.dump(depenses, f , ensure_ascii=False, indent=2)
depenses = charger()

def ajouter (montant, devise, categorie):
        depense ={"montant" : montant, "devise" : devise, "categorie" : categorie}
        depenses.append(depense)
        sauvegarder()

while True :
        print("n\1. Ajouter une depense ")
        print("2. Voir les depenses")
        print("0. Quitter")
        choix = input("Ton choix : ")

        if choix == "1" :
            montant = float(input("Montant : "))
            devise = input("Devise (ex : CDF, USD, EUR) : ").upper()
            categorie = input("Categorie :  ")
            ajouter(montant, devise, categorie)
            print("Depense ajoutee")
        elif choix == "2" :
               for d in depenses:
                      print(d["montant"], d["devise"], d["categorie"])
        elif choix == "0" :
               print("Au revoir !")
               break
        else:
               print ("Choix invalide.")                      


        





    
        

