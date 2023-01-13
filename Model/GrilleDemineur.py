# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True


def construireGrilleDemineur(li: int, col: int) -> list:
    """Construit une grille de démineur

    :param li: nombre de ligne de la grille
    :type li: int
    :param col: nombre de colonne de la grille
    :type col: int
    :raises TypeError: les arguments ne sont pas du bon type
    :raises ValueError: un des arguments est nulles ou négatif
    :return: grille sous forme de tableau 2D
    :rtype: list
    """
    if type(li) != int or type(col) != int:
        raise TypeError(
            f"construireGrilleDemineur : Le nombre delignes ({li}) ou de colonnes ({col})) n’est pas un entier.")
    if li < 1 or col < 1:
        raise ValueError(
            f"construireGrilleDemineur : Le nombre de lignes ({li}) ou de colonnes ({col}) est négatif ou nul.")
    grille = []
    for y in range(li):
        ligne = []
        for x in range(col):
            ligne.append(construireCellule())
        grille.append(ligne)
    return grille


def getNbLignesGrilleDemineur(grille: list) -> int:
    """Calcul du nombre de ligne d'une grille

    :param grille: grille de la partie
    :type grille: list
    :raises TypeError: le paramètre liste n'est pas une grille
    :return: nombre de ligne de la grille
    :rtype: int
    """
    if not type_grille_demineur(grille):
        raise TypeError(
            "getNbLignesGrilleDemineur : Le paramètre n'est pas une grille")
    else:
        return len(grille)


def getNbColonnesGrilleDemineur(grille: list) -> int:
    """Calcul du nombre de colonne d'une grille

    :param grille: grille de la partie
    :type grille: list
    :raises TypeError: le paramètre liste n'est pas une grille
    :return: nombre de colonne de la grille
    :rtype: int
    """
    if not type_grille_demineur(grille):
        raise TypeError(
            "getNbColonneGrilleDemineur : Le paramètre n'est pas une grille")
    else:
        return len(grille[0])


def isCoordonneeCorrecte(grille: list, coord: tuple) -> bool:
    """_summary_

    :param grille: grille de la partie
    :type grille: list
    :param coord: coordonnées à vérifier
    :type coord: tuple
    :raises TypeError: les coordonées ne sont pas de bon type
    :return: True si les coordonnées sont contenus dans la grille, False sinon
    :rtype: bool
    """
    if type(coord) != tuple or type(grille) != list or not type_grille_demineur(grille) \
            or len(coord) != 2 or type(coord[0]) != int or type(coord[1]) != int:
        raise TypeError(
            "isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    else:
        return getNbLignesGrilleDemineur(grille) > coord[0] and getNbColonnesGrilleDemineur(grille) > coord[1]


def getCelluleGrilleDemineur(grille: list, coord: tuple) -> dict:
    """Retourne la cellule à partir de ces coordonnées dans la grille

    :param grille: grille de la partie
    :type grille: list
    :param coord: coordonnées de la cellule
    :type coord: tuple
    :raises TypeError: les paramètres ne correspondent pas à leur type
    :raises IndexError: les coordonnées ne se trouve pas dans la grille
    :return: cellule correspondant aux coordonnées 
    :rtype: dict
    """
    if type(coord) != tuple or type(grille) != list or not type_grille_demineur(grille):
        raise TypeError(
            "getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    elif not isCoordonneeCorrecte(grille, coord):
        raise IndexError(
            "getCelluleGrilleDemineur : coordonnée non contenue dans la grille.")
    else:
        return grille[coord[0]][coord[1]]


def getContenuGrilleDemineur(grille: list, coord: tuple) -> int:
    """Retourne le contenu d'une cellule à partir de coordonnées dans une grille

    :param grille: grille de la partie
    :type grille: list
    :param coord: coordonnées de la cellule
    :type coord: tuple
    :return: contenu
    :rtype: int
    """
    return getContenuCellule(getCelluleGrilleDemineur(grille, coord))


def setContenuGrilleDemineur(grille: list, coord: tuple, contenu: int) -> None:
    """Modifie le contenu d'une cellule à partir de ces coordonnées

    :param grille: grille de la partie
    :type grille: list
    :param coord: coordonnées de la cellule
    :type coord: tuple
    :param contenu: nouveau contenu de la cellule
    :type contenu: int
    """

    setContenuCellule(getCelluleGrilleDemineur(grille, coord), contenu)
    return None


def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    """Retourne la visibilité d'une cellule à partir de ces coordonnées dans une grille

    :param grille: grille de la partie
    :type grille: list
    :param coord: coordonnées de la cellule
    :type coord: tuple
    :return: visibilité de la cellule
    :rtype: bool
    """
    return isVisibleCellule(getCelluleGrilleDemineur(grille, coord))


def setVisibleGrilleDemineur(grille: list, coord: tuple, visible: bool) -> None:
    """_summary_

    :param grille: Modifie la visibilité d'une cellule à partir de ces coordonnées
    :type grille: list
    :param coord: coordonnées de la cellule
    :type coord: tuple
    :param visible: nouvelle visibilité de la cellule
    :type visible: bool
    """

    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), visible)


def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    """Vérfie si une cellule contient une bombe à partir de ces coordonnées

    :param grille: grille de la partie
    :type grille: list
    :param coord: coordonnées de la cellule
    :type coord: tuple
    :return: True si la cellule contient une bombe, False sinon
    :rtype: bool
    """
    return contientMineCellule(getCelluleGrilleDemineur(grille, coord))


def getCoordonneeVoisinsGrilleDemineur(grille: list, coord: tuple) -> list:
    """Récupère les coordonnées des cellules voisines à une autre (principale)

    :param grille: grille de la partie
    :type grille: list
    :param coord: coordonnées de la cellule principale
    :type coord: tuple
    :raises TypeError: les paramètre ne sont pas de bon type
    :raises IndexError: les coordonnées ne sont pas dans la grille
    :return: coordonnées des voisins de la cellule principale
    :rtype: list
    """
    if not isinstance(grille, list) or not isinstance(coord, tuple):
        raise TypeError(
            "getCoordonneeVoisinsGrilleDemineur : un des paramètres n’est pas du bon type.")
    elif not isCoordonneeCorrecte(grille, coord):
        raise IndexError(
            "getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille.")
    else:
        voisins = []
        if coord[0] == 0:
            minLigneVoisin = coord[0]
            maxLigneVoisin = coord[0] + 1
        elif coord[0] == getNbLignesGrilleDemineur(grille) - 1:
            maxLigneVoisin = coord[0]
            minLigneVoisin = coord[0] - 1
        else:
            minLigneVoisin = coord[0] - 1
            maxLigneVoisin = coord[0] + 1

        if coord[1] == 0:
            minColonneVoisin = coord[1]
            maxColonneVoisin = coord[1] + 1
        elif coord[1] == getNbColonnesGrilleDemineur(grille) - 1:
            minColonneVoisin = coord[1] - 1
            maxColonneVoisin = coord[1]
        else:
            minColonneVoisin = coord[1] - 1
            maxColonneVoisin = coord[1] + 1

        for i in range(minLigneVoisin, maxLigneVoisin + 1):
            for j in range(minColonneVoisin, maxColonneVoisin + 1):
                if (i, j) != coord:
                    voisins.append((i, j))
        return voisins


def placerMinesGrilleDemineur(grille: list, nb: int, coord: tuple) -> None:
    """Place des mines aléatoirement dans une grille en excluant une cellule de coordonnées données

    :param grille: grille de la partie
    :type grille: list
    :param nb: nombre de mine à placer
    :type nb: int
    :param coord: coordonnées de la cellule à exclure
    :type coord: tuple
    :raises IndexError: les coordonnées ne sont pas dans la grille
    :raises ValueError: nombre de mines à placer incorrect
    """
    h, w = getNbLignesGrilleDemineur(
        grille), getNbColonnesGrilleDemineur(grille)
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError(
            "placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille")
    elif nb < 0 or nb >= (w * h):
        raise ValueError(
            "placerMinesGrilleDemineur : Nombre de bombes à placer incorrect")
    else:
        while nb > 0:
            i, j = coord
            while (i, j) == coord:
                i = randint(0, h - 1)
                j = randint(0, w - 1)
            cellule = getCelluleGrilleDemineur(grille, (i, j))
            if not contientMineCellule(cellule):
                setContenuCellule(cellule, const.ID_MINE)
                nb -= 1

    compterMinesVoisinesGrilleDemineur(grille)
    return None


def compterMinesVoisinesGrilleDemineur(grille: list) -> None:
    """_summary_

    :param grille: grille de la partie
    :type grille: list
    """
    h, w = getNbLignesGrilleDemineur(
        grille), getNbColonnesGrilleDemineur(grille)
    for i in range(h):
        for j in range(w):
            cellule = getCelluleGrilleDemineur(
                grille, (i, j))  # On récupère la cellule
            if contientMineCellule(cellule):  # Si elle contient une mine
                # On parcourt ces voisins
                for voisin in getCoordonneeVoisinsGrilleDemineur(grille, (i, j)):
                    if not contientMineGrilleDemineur(grille, voisin):
                        # On récupère la cellule voisine
                        mines = getContenuGrilleDemineur(grille, voisin) + 1
                        setContenuGrilleDemineur(grille, voisin, mines)
    return None


def getNbMinesGrilleDemineur(grille: list) -> int:
    """Compte le nombre de mines présentes dans une grille

    :param grille: grille de la partie
    :type grille: list
    :raises ValueError: le paramètre n'est pas une grille
    :return: nombre de mines
    :rtype: int
    """
    if not type_grille_demineur(grille):
        raise ValueError(
            "getNbMinesGrilleDemineur : le paramètre n’est pas une grille.")
    else:
        nbMine = 0
        h, w = getNbLignesGrilleDemineur(
            grille), getNbColonnesGrilleDemineur(grille)
        for i in range(h):
            for j in range(w):
                if contientMineGrilleDemineur(grille, (i, j)):
                    nbMine += 1
        return nbMine


def getAnnotationGrilleDemineur(grille: list, coord: tuple) -> str:
    """Retourne l'annotation d'une cellule à partir de ces coordonnées

    :param grille: grille de la partie
    :type grille: list
    :param coord: coordonnées de la cellule
    :type coord: tuple
    :return: annotation de la cellule
    :rtype: str
    """
    return getAnnotationCellule(getCelluleGrilleDemineur(grille, coord))


def getMinesRestantesGrilleDemineur(grille: list) -> int:
    """Compte le nombre de mines non trouvées dans une grille

    :param grille: grille de la partie
    :type grille: list
    :return: nombre de mine
    :rtype: int
    """
    h, w = getNbLignesGrilleDemineur(
        grille), getNbColonnesGrilleDemineur(grille)
    nb = 0
    for i in range(h):
        for j in range(w):
            if getAnnotationGrilleDemineur(grille, (i, j)) == const.FLAG:
                nb += 1
    return getNbMinesGrilleDemineur(grille) - nb


def showGrid(grille: list) -> None:
    """Permet un meilleur debugage : montre le contenu des cellules de la grille

    :param grille: grille de la partie
    :type grille: list
    """
    for i in range(len(grille)):
        line = [getContenuGrilleDemineur(grille, (i, j)) for j in range(
            getNbColonnesGrilleDemineur(grille))]
        print(line)
    return None


def gagneGrilleDemineur(grille: list) -> bool:
    """Determine si une partie est gagnée

    :param grille: grille de la partie
    :type grille: list
    :return: True si la partie est gagnée, False sinon
    :rtype: bool
    """
    h, w = getNbLignesGrilleDemineur(
        grille), getNbColonnesGrilleDemineur(grille)
    gagner = True
    i, j = 0, 0
    while gagner and i < h:
        while gagner and j < w:
            if (contientMineGrilleDemineur(grille, (i, j)) and isVisibleGrilleDemineur(grille, (
                    i, j)) and getAnnotationGrilleDemineur(grille, (i, j)) == const.FLAG) or (
                    not contientMineGrilleDemineur(grille, (i, j))) and (not isVisibleGrilleDemineur(grille, (i, j))):
                gagner = False
            j += 1
        j = 0
        i += 1
    return gagner


def perduGrilleDemineur(grille) -> bool:
    """Détermine si une partie est perdue

    :param grille: grille de la partie
    :type grille: _type_
    :return: True si la partie est perdu, False sinon
    :rtype: bool
    """
    h, w = getNbLignesGrilleDemineur(
        grille), getNbColonnesGrilleDemineur(grille)
    perdu = True
    i, j = 0, 0
    while perdu and i < h:
        while perdu and j < w:
            if contientMineGrilleDemineur(grille, (i, j)) and isVisibleGrilleDemineur(grille, (i, j)):
                perdu = False
            j += 1
        j = 0
        i += 1
    return not perdu


def reinitialiserGrilleDemineur(grille: list) -> None:
    """Réinitialise toutes les cellules d'une grille

    :param grille: grille
    :type grille: list
    """
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbLignesGrilleDemineur(grille)):
            reinitiliserCellule(getCelluleGrilleDemineur(grille, (i, j)))
    return None


def decouvrirGrilleDemineur(grille: list, coord: tuple) -> set:
    """Découvre (rend visible) la cellule ainsi que ces voisines si elle n'est pas voisiné par une mine

    :param grille: grille de la partie
    :type grille: list
    :param coord: coordonnée de la première cellule à découvrir
    :type coord: tuple
    :return: coordonnées des cellules rendus visible
    :rtype: set
    """
    cellulesDecouvertes = set()
    cellulesADecouvrir = [coord]

    while len(cellulesADecouvrir) != 0:
        currentCoord = cellulesADecouvrir.pop()
        if currentCoord not in cellulesDecouvertes:
            setVisibleGrilleDemineur(grille, currentCoord, True)
            cellulesDecouvertes.add(currentCoord)
            if getContenuGrilleDemineur(grille, currentCoord) == 0:
                voisins = getCoordonneeVoisinsGrilleDemineur(
                    grille, currentCoord)
                cellulesADecouvrir.extend(voisins)
    return cellulesDecouvertes


def simplifierGrilleDemineur(grille: list, coord: tuple) -> set:
    """Decourvre les cellules voisines lorsque le nombre de drapeau correspond au contenu d'une cellule

    :param grille: grille de la partie
    :type grille: list
    :param coord: coordonnées de la cellule
    :type coord: tuple
    :return: coordonnées des cellules rendus visible
    :rtype: set
    """
    if not isVisibleGrilleDemineur(grille, coord):
        return set()
    else:
        cellulesDecouvertes = set()
        cellulesADecouvrir = [coord]
        while len(cellulesADecouvrir) != 0:
            currentCoord = cellulesADecouvrir.pop()
            if currentCoord not in cellulesDecouvertes:
                voisins = getCoordonneeVoisinsGrilleDemineur(
                    grille, currentCoord)
                # Compte les drapeaux au voisinnage
                nbFlag = 0
                for voisin in voisins:
                    if getAnnotationGrilleDemineur(grille, voisin) == const.FLAG:
                        nbFlag += 1
                # Compare le nombre de drapeau et les voisins non visible
                if nbFlag == getContenuGrilleDemineur(grille, currentCoord):
                    for voisin in voisins:
                        if not isVisibleGrilleDemineur(grille, voisin) and not getAnnotationGrilleDemineur(grille, voisin) == const.FLAG:
                            setVisibleGrilleDemineur(grille, voisin, True)
                            cellulesADecouvrir.append(voisin)
                cellulesDecouvertes.add(currentCoord)
        return cellulesDecouvertes


def ajouterFlagsGrilleDemineur(grille: list, coord: tuple) -> set:
    """
    Place les drapeaux lorsque le nombre de voisins correpond au contenu de la cellule

    :param grille: grille de la partie
    :type grille: list
    :param coord: coordonnées de la cellule
    :type coord: tuple
    :return: coordonnées des cellules marqués d'un drapeau
    :rtype: set
    """
    # Liste les cellules voisines non visible
    voisinsNonDecouverts = []
    for voisin in getCoordonneeVoisinsGrilleDemineur(grille, coord):
        if not isVisibleGrilleDemineur(grille, voisin):
            voisinsNonDecouverts.append(voisin)
    # Le contenu de la cellule est-il égale au nombre de voisin non visible
    if getContenuGrilleDemineur(grille, coord) == len(voisinsNonDecouverts):
        for voisin in voisinsNonDecouverts:
            if not getAnnotationGrilleDemineur(grille, voisin):
                getCelluleGrilleDemineur(grille, voisin)[
                    const.ANNOTATION] = const.FLAG
    return set(voisinsNonDecouverts)


def isResoluGrilleDemineur(grille: list, coord: tuple) -> bool:
    """Détermine si une cellule est résolue ou non

    :param grille: grille de la partie
    :type grille: list
    :param coord: coordonnées de la cellule à vérifier
    :type coord: tuple
    :return: True, si la cellule est résolue, False sinon
    :rtype: bool
    """
    return grille[coord[0]][coord[1]][const.RESOLU]


def actualiseResolu(grille: list, coord: tuple) -> None:
    countVoisinResolu = 0
    voisins = getCoordonneeVoisinsGrilleDemineur(grille, coord)
    for voisin in voisins:
        if isVisibleGrilleDemineur(grille, voisin) or (not isVisibleGrilleDemineur(grille, voisin) and getAnnotationGrilleDemineur(grille, voisin) == const.FLAG):
            countVoisinResolu += 1
    if countVoisinResolu == len(voisins):
        grille[coord[0]][coord[1]][const.RESOLU] = True
    else:
        grille[coord[0]][coord[1]][const.RESOLU] = False
    return None

def simplifierToutGrilleDemineur(grille: list) -> tuple:
    """Aide à la résolution

    Simplifie si possible chaque cellule de la grille.
    Ajoute les drapeaux lorsque c'est évident de chaque cellule de la grille.

    :param grille: grille de la partie
    :type grille: list
    :return: l'ensemble des cellules rendus visibles, l'ensemble des cellules marqué d'un drapeau
    :rtype: tuple
    """
    simplifie = set()
    ajoute = set()
    isModified = True
    while isModified:

        prevSimplifie = simplifie.copy()
        prevAjoute = ajoute.copy()
        print(prevSimplifie)
        # On parcours toutes les cellules
        for i in range(getNbLignesGrilleDemineur(grille)):
            for j in range(getNbColonnesGrilleDemineur(grille)):
                # Si elle est visible et qu'une (ou plus) mine(s) la voisine
                actualiseResolu(grille, (i, j))
                if isVisibleGrilleDemineur(grille, (i, j)) and getContenuGrilleDemineur(grille, (i, j)) != 0 and not isResoluGrilleDemineur(grille, (i, j)):
                    simplifie.update(simplifierGrilleDemineur(grille, (i, j)))
                    ajoute.update(ajouterFlagsGrilleDemineur(grille, (i, j)))
        print(prevSimplifie)
        print(prevAjoute)
        # Mise à jour de isModified
        if prevSimplifie == simplifie and prevAjoute == ajoute:
            isModified = False

    return simplifie, ajoute
