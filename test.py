tableau = [5,1,2,3]
def tri_shaker(tableau):
    permutation,sens,en_cours = True,1,0
    debut,fin = 0,len(tableau)-2
    while permutation == True:
        permutation = False
        while (en_cours<fin and sens==1) or \
        (en_cours>debut and sens==-1) :
            # Test si echange
            if tableau[en_cours] > tableau[en_cours + 1]:
                permutation = True
                # On echange les deux elements
                tableau[en_cours], tableau[en_cours + 1] = \
                tableau[en_cours + 1],tableau[en_cours]
            en_cours = en_cours + sens
        # On change le sens du parcours
        if sens==1:
            fin = fin - 1
        else:
            debut = debut + 1
        sens = -sens
    return tableau
print(tableau)