class Equipe:
    def __init__ (self, nom, joueurs):
        self.nom = nom
        self.joueurs = joueurs
        self.points = 0

    def score_equipe(self):
        score = 0
        if not len(self.joueurs) == 5:
            return "Il n'y a pas assez de joueurs !"
        else:
            for player in self.joueurs:
                score += player.score_joueur()
            score = score / len(self.joueurs)
        return score

    def ajouter_joueur(self, a):
        self.joueurs.append(a)
        return a

    def retirer_joueur(self):
        self.remove(self.joueurs)

    def ajouter_point(self):
        self.points += 1

    def __str__(self):
        texteAffichage = self.nom + ":" + "\n"
        for player in self.joueurs:
            texteAffichage += "Lane: " + str(player.lane) + ' -> ' + str(player.pseudo) + "\n"
        texteAffichage += "Score de l'équipe: " + str(self.score_equipe()) + "\n"
        texteAffichage += "Points de l'équipes: " + str(self.points) + "\n"
        texteAffichage += "-------------------------------"
        return texteAffichage


class Joueur:
    def __init__ (self, nom, pseudo, prenom, lane, attaque, defense):
        self.nom = nom
        self.pseudo = pseudo
        self.prenom = prenom
        self.lane = lane
        self.attaque = attaque
        self.defense = defense


    def score_joueur(self):
        score = self.attaque + self.defense
        return score


    def __str__(self):
        texteAffichage = str(self.nom) + ' "' + str(self.pseudo) + '" ' + str(self.prenom) + "\n"
        texteAffichage += "Lane: " + str(self.lane) + "\n"
        texteAffichage += "Attaque / Défense: " + str(self.attaque) + "/" + str(self.defense) + "\n"
        texteAffichage += "Score du joueur : " + str(self.score_joueur()) + "\n"
        return texteAffichage
            

Armut = Joueur('Tükek', 'Armut', 'İrfan', 'Top', 32, 30)
Elyoya = Joueur('Prades Batalla', 'Elyoya', 'Javier', 'Jungle', 33, 38)
Humanoid = Joueur('Brázda', 'Humanoid', 'Marek', 'Mid', 41, 38)
Carzzy = Joueur('Orság', 'Carzzy', 'Matyáš', 'Adc', 43, 36)
Kaiser = Joueur('Kaiser', 'Kaiser', 'Norman', 'Support', 36, 41)

Adam = Joueur('Maanane', 'Adam', 'Adam', 'Top', 35, 25)
Bwipo = Joueur('Rau', 'Bwipo', 'Gabriël', 'Jungle', 35, 28)
Nisqy = Joueur('Dinçer', 'Nisqy', 'Yasin ', 'Mid', 35, 31)
Upset = Joueur('Lipp', 'Upset', 'Elias', 'Adc', 42, 35)
Hylisang = Joueur('Iliev Galabov', 'Hylisang', 'Zdravets ', 'Support', 40, 20)

Odoamne = Joueur('Pascu', 'Odoamne', 'Andrei', 'Top', 34, 34)
Inspired = Joueur('Słoma', 'Inspired', 'Kacper', 'Jungle', 40, 42)
Larssen = Joueur('Larsson', 'Larssen', 'Emil', 'Mid', 20, 23)
Hanssama = Joueur('Liv', 'HansSama', 'Steven', 'Adc', 46, 42)
Trymbi = Joueur('Trybus', 'Trymbi', 'Adrian', 'Support', 33, 40)

Wunder = Joueur('Nordahl Hansen', 'Wunder', 'Martin', 'Top', 15, 20)
Jankos = Joueur('Jankowski', 'Jankos', 'Marcin', 'Jungle', 35, 30)
Caps = Joueur('Borregaard Winther', 'Caps', 'Rasmus', 'Mid', 38, 39)
Rekkles = Joueur('Larsson', 'Rekkles', 'Martin', 'Adc', 31, 47)
Mikyx = Joueur('Mehle', 'Mikyx', 'Mihael', 'Support', 34, 37)

Hirit = Joueur('Tae-min', 'HiRit', 'Shin', 'Top', 31, 31)
Razork = Joueur('Martín Díaz', 'Razork', 'Iván', 'Jungle', 32, 28)
Vetheo = Joueur('Berrié', 'Vetheo', 'Vincent', 'Mid', 45, 42)
Kobbe = Joueur('Kobberup', 'Kobbe', 'Kasper', 'Adc', 32, 35)
Vander = Joueur('Bogdan', 'Vander', 'Oskar', 'Support', 20, 19)

Szygenda = Joueur('Jensen', 'Szygenda', 'Mathias', 'Top', 29, 32)
Selfmade = Joueur('Boderek', 'Selfmade', 'Oskar', 'Jungle', 36, 24)
Lider = Joueur('Ilyasov', 'LIDER', 'Adam', 'Mid', 25, 28)
Comp = Joueur('Stamkopoulos', 'Comp', 'Markos', 'Adc', 23, 26)
Labrov = Joueur('Papoutsakis', 'Labrov', 'Labros', 'Support', 29, 24)

Whiteknight = Joueur('Sormunen', 'WhiteKnight', 'Matti', 'Top', 34, 32)
Zanzarah = Joueur('Akatov', 'Zanzarah', 'Nikolay', 'Jungle', 30, 29)
Magifelix = Joueur('Boström', 'MagiFelix', 'Carl Felix', 'Mid', 28, 26)
Jeskla = Joueur('Klarin Strömberg', 'Jeskla', 'Jesper', 'Adc', 26, 25)
Promisq = Joueur('Abrahamsson', 'Promisq', 'Hampus Mikael', 'Support', 22, 26)

Kryze = Joueur('Hellström', 'Kryze', 'Felix', 'Top', 25, 25)
Dan = Joueur('Hockley', 'Dan', 'Daniel', 'Jungle', 25, 25)
Nukeduck = Joueur('Holm', 'Nukeduck', 'Erlend', 'Mid', 31, 35)
Patrik = Joueur('Jírů', 'Patrik', 'Patrik', 'Adc', 34, 23)
Denyk = Joueur('Haramach', 'Denyk', 'Petr', 'Support', 32, 31)

Jenax = Joueur('Bartels', 'Jenax', 'Janik', 'Top', 30, 26)
Trick = Joueur('Gang-yun', 'Trick', 'Kim', 'Jungle', 24, 28)
Blue = Joueur('Gören', 'Blue', 'Ersin', 'Mid', 28, 28)
Jezu = Joueur('Massol', 'Jezu', 'Jean', 'Adc', 32, 36)
Lilipp = Joueur('Englert', 'Lilipp', 'Philipp Samuel', 'Support', 25, 26)

Brokenblade = Joueur('Çelik', 'Broken Blade', 'Sergen', 'Top', 41, 38)
Kirei = Joueur('Yuen', 'Kirei', 'Thomas', 'Jungle', 24, 21)
Nuclearint = Joueur('Bizriken', 'NUCLEARINT', 'Ilias', 'Mid', 32, 26)
Neon = Joueur('Jakubčík', 'Neon', 'Matúš', 'Adc', 21, 23)
Limit = Joueur('Tot', 'LIMIT', 'Dino', 'Support', 21, 26)


##Équipes:
Mad = Equipe('MAD Lions', [Armut, Elyoya, Humanoid, Carzzy, Kaiser])
Fnc = Equipe('Fnatic', [Adam, Bwipo, Nisqy, Upset, Hylisang])
Rge = Equipe('Rogue' , [Odoamne, Inspired, Larssen, Hanssama, Trymbi])
G2 = Equipe('G2 Esport' , [Wunder, Jankos, Caps, Rekkles, Mikyx])
Msf = Equipe('Misfits Gaming' , [Hirit, Razork, Vetheo, Kobbe, Vander])
Vit = Equipe('Vitality' , [Szygenda, Selfmade, Lider, Comp, Labrov])
Ast = Equipe('Astralis' , [Whiteknight, Zanzarah, Magifelix, Jeskla, Promisq])
Ex = Equipe('EXCEL' , [Kryze, Dan, Nukeduck, Patrik, Denyk])
Sk = Equipe('SK Gaming' , [Jenax, Trick, Blue, Jezu, Lilipp])
S04 = Equipe('Shalke 04' , [Brokenblade, Kirei, Nuclearint, Neon, Limit])