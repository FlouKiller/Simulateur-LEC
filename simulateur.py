from objets import *
from random import randint

def match(e1, e2):
  total = e1.score_equipe() + e2.score_equipe()
  pourcentage = e1.score_equipe()/total*100
  gagnant = randint(1, 100)

  if pourcentage >= gagnant:
##    print("C'est " +  e1.nom  + " qui gagne le match contre " + e2.nom)
    return e1, e2
  else:
##    print("C'est " +  e2.nom  + " qui gagne le match contre " + e1.nom)
    return e2, e1

def tournois(equipes):
    for equipe in equipes:
        equipe.points = 0
        
    for a in range(len(equipes)):
        for b in range(len(equipes)):
            if equipes[a] != equipes[b]:
                gagnant = match(equipes[a], equipes[b])[0]
                gagnant.ajouter_point()
                

def classement(equipes):
    tournois(equipes)
    bienTrie = False
    while (bienTrie == False):
        bienTrie = True
        for i in range(0, len(equipes)-1):
            if equipes[i].points < equipes[i+1].points:
                temp = equipes[i]
                equipes[i] = equipes[i+1]
                equipes[i+1] = temp
                bienTrie = False
    top6 = []
    for a in range(6):
        top6.append(equipes[a])
    #for i in range(len(equipes)):
    #    print(str(i+1) + "e place: " + equipes[i].nom + " -> " + str(equipes[i].points) + " points")
    #print("")
    return top6


def match_bo5(e1, e2):
    e1.points = 0
    e2.points = 0
    while e1.points != 3 and e2.points != 3:
        gagnant = match(e1, e2)[0]
        gagnant.ajouter_point()
    if e1.points == 3:
        return e1, e2
    else:
        return e2, e1


def phase_finale(top6):
  finale = []
  demifinales_1 = []
  demifinales_2 = []
  round2 = []
  round3 = []

  r1_1 = match_bo5(top6[0], top6[3])
  r1_2 = match_bo5(top6[1], top6[2])
  r1_3 = match_bo5(top6[4], top6[5])
  #print("   -Winner bracket:")
  #print("Premier match:", top6[0].nom, "VS", top6[3].nom, "->", r1_1[0].nom + " l'emporte " + str(r1_1[0].points) + "-" + str(r1_1[1].points))
  #print("Deuxieme match:", top6[1].nom, "VS", top6[2].nom, "->", r1_2[0].nom + " l'emporte " + str(r1_2[0].points) + "-" + str(r1_2[1].points))
  #print("")
  #print("   -Loser bracket:")
  #print("Premier match:", top6[4].nom, "VS", top6[5].nom, "->", r1_3[0].nom + " l'emporte " + str(r1_3[0].points) + "-" + str(r1_3[1].points))

  demifinales_1.append(r1_1[0])
  demifinales_1.append(r1_2[0])
  round2.append(r1_3[0])
  round2.append(r1_2[1])

  r2_1 = match_bo5(round2[0], round2[1])
  #print("Deuxième match:", round2[0].nom, "VS", round2[1].nom, "->", r2_1[0].nom + " l'emporte " + str(r2_1[0].points) + "-" + str(r2_1[1].points))

  round3.append(r2_1[0])
  round3.append(r1_1[1])

  r3_1 = match_bo5(round3[0], round3[1])
  #print("Troisème match:", round3[0].nom, "VS", round3[1].nom, "->", r3_1[0].nom + " l'emporte " + str(r3_1[0].points) + "-" + str(r3_1[1].points))
  #print("")

  demifinales_2.append(r3_1[0])

  d1 = match_bo5(demifinales_1[0], demifinales_1[1])
  #print("   -Demi-finales:")
  #print("Premier match:", demifinales_1[0].nom, "VS", demifinales_1[1].nom, "->", d1[0].nom + " l'emporte " + str(d1[0].points) + "-" + str(d1[1].points))

  demifinales_2.append(d1[1])

  d2 = match_bo5(demifinales_2[0], demifinales_2[1])
  #print("Deuxième match:", demifinales_2[0].nom, "VS", demifinales_2[1].nom, "->", d2[0].nom + " l'emporte " + str(d2[0].points) + "-" + str(d2[1].points))
  #print("")

  finale.append(d1[0])
  finale.append(d2[0])

  f = match_bo5(finale[0], finale[1])
  #print("   -La finale opposera:")
  #print(finale[0].nom, "VS", finale[1].nom)
  #print("C'est " + f[0].nom + " qui remporte le tournois ! (" + str(f[0].points) + "-" + str(f[1].points) + ")")
  
  return f[0]


equipes = [Mad, Fnc, Rge, G2, Msf, Vit, Ast, Ex, Sk, S04]

mad = 0
fnc = 0
rge = 0
g2 = 0
msf = 0
vit = 0
ast = 0
ex = 0
sk = 0
s04 = 0
nb_test = 1000

for i in range(nb_test):
    
    top6 = classement(equipes)
    gagnant = phase_finale(top6)
    
    if gagnant == Mad:
        mad += 1
    elif gagnant == Fnc:
        fnc += 1
    elif gagnant == Rge:
        rge += 1
    elif gagnant == G2:
        g2 += 1
    elif gagnant == Msf:
        msf += 1
    elif gagnant == Vit:
        vit += 1
    elif gagnant == Ast:
        ast += 1
    elif gagnant == Ex:
        ex += 1
    elif gagnant == Sk:
        sk += 1
    elif gagnant == S04:
        s04 += 1

print()
print("Simulation sur", nb_test, "tournois :")
print()
print("Winrate G2 Esport --------", round(g2/nb_test*100, 2), "%")
print("Winrate MAD Lions --------", round(mad/nb_test*100, 2), "%")
print("Winrate Fnatic -----------", round(fnc/nb_test*100, 2), "%")
print("Winrate Rogue ------------", round(rge/nb_test*100, 2), "%")
print("Winrate Misfits Gaming ---", round(msf/nb_test*100, 2), "%")
print("Winrate Vitality ---------", round(vit/nb_test*100, 2), "%")
print("Winrate Astralis ---------", round(ast/nb_test*100, 2), "%")
print("Winrate Excel ------------", round(ex/nb_test*100, 2), "%")
print("Winrate Sk Gaming --------", round(sk/nb_test*100, 2), "%")
print("Winrate Shalke 04 --------", round(s04/nb_test*100, 2), "%")