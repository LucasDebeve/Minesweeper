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
    """
    Détermine si le paramètre représente une grille d'un démineur.

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

    Args:
        li (int): nombre de ligne de la grille
        col (int): nombre de colonne de la grille

    Raises:
        TypeError: les arguments ne sont pas du bon type
        ValueError: un des arguments est nulles ou négatif

    Returns:
        list: grille sous forme de tableau 2D
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

    Args:
        grille (list): grille

    Raises:
        TypeError: Le paramètre liste n'est pas une grille

    Returns:
        int: nombre de ligne d'une grille
    """
    if not type_grille_demineur(grille):
        raise TypeError(
            "getNbLignesGrilleDemineur : Le paramètre n'est pas une grille")
    else:
        return len(grille)


def getNbColonnesGrilleDemineur(grille: list) -> int:
    """Calcul du nombre de colonne d'une grille

    Args:
        grille (list): grille

    Raises:
        TypeError: le paramètre liste n'est pas une grille

    Returns:
        int: nombre de colonne
    """
    if not type_grille_demineur(grille):
        raise TypeError(
            "getNbColonneGrilleDemineur : Le paramètre n'est pas une grille")
    else:
        return len(grille[0])


def isCoordonneeCorrecte(grille: list, coord: tuple) -> bool:
    """Vérifie que les coordonnées passées en paramètre correspondent à des coordonnées de la grille

    Args:
        grille (list): grille
        coord (tuple): coordonnées à vérifier

    Raises:
        TypeError: les coordonées ne sont pas de bon type

    Returns:
        bool: True si les coordonnées sont contenus dans la grille, False sinon
    """
    if type(coord) != tuple or type(grille) != list or not type_grille_demineur(grille) \
            or len(coord) != 2 or type(coord[0]) != int or type(coord[1]) != int:
        raise TypeError(
            "isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    else:
        return getNbLignesGrilleDemineur(grille) > coord[0] and getNbColonnesGrilleDemineur(grille) > coord[1]


def getCelluleGrilleDemineur(grille: list, coord: tuple) -> dict:
    """Retourne la cellule à partir de ces coordonnées dans la grille

    Args:
        grille (list): grille
        coord (tuple): coordonnées de la cellule

    Raises:
        TypeError: les paramètres ne correspondent pas à leur type
        IndexError: les coordonnées ne se trouve pas dans la grille

    Returns:
        dict: cellule correspondant aux coordonnées 
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

    Args:
        grille (list): grille
        coord (tuple): coordonnées de la cellule

    Returns:
        int: Contenu
    """
    return getContenuCellule(getCelluleGrilleDemineur(grille, coord))


def setContenuGrilleDemineur(grille: list, coord: tuple, contenu: int) -> None:
    """Modifie le contenu d'une cellule à partir de ces coordonnées

    Args:
        grille (list): grille
        coord (tuple): coordonnées de la cellule
        contenu (int): nouveau contenu de la cellule
    """
    setContenuCellule(getCelluleGrilleDemineur(grille, coord), contenu)
    return None


def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    """Retourne la visibilité d'une cellule à partir de ces coordonnées dans une grille

    Args:
        grille (list): grille
        coord (tuple): coordonnées de la cellule

    Returns:
        bool: visibilité de la cellule
    """
    return isVisibleCellule(getCelluleGrilleDemineur(grille, coord))


def setVisibleGrilleDemineur(grille: list, coord: tuple, visible: bool) -> None:
    """Modifie la visibilité d'une cellule à partir de ces coordonnées

    Args:
        grille (list): _description_
        coord (tuple): _description_
        visible (bool): _description_
    """
    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), visible)


def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    """Vérfie si une cellule contient une bombe à partir de ces coordonnées

    Args:
        grille (list): grille
        coord (tuple): coorsonnées de la cellule

    Returns:
        bool: True si la cellule contient une bombe, False sinon
    """
    return contientMineCellule(getCelluleGrilleDemineur(grille, coord))


def getCoordonneeVoisinsGrilleDemineur(grille: list, coord: tuple) -> list:
    """Récupère les coordonnées des cellules voisines à une autre (principale)

    Args:
        grille (list): grille
        coord (tuple): coordonnées de la cellule principale

    Raises:
        TypeError: les paramètre ne sont pas de bon type
        IndexError: les coordonnées ne sont pas dans la grille

    Returns:
        list: coordonnées des voisins de la cellule principale
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

    Args:
        grille (list): grille
        nb (int): nombre de mine à placer
        coord (tuple): coordonnées de la cellule à exclure

    Raises:
        IndexError: les coordonnées ne sont pas dans la grille
        ValueError: nombre de mines à placer incorrect
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
    """Compte le nombre de mines voisines à chaque cellule d'une grille et remplie son contenu

    Args:
        grille (list): grille
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

    Args:
        grille (list): grille

    Raises:
        ValueError: le paramètre n'est pas une grille

    Returns:
        int: nombre de mines
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

    Args:
        grille (list): grille
        coord (tuple): coordonnées de la cellule

    Returns:
        str: annotation de la cellule
    """
    return getAnnotationCellule(getCelluleGrilleDemineur(grille, coord))


def getMinesRestantesGrilleDemineur(grille: list) -> int:
    """Compte le nombre de mines non trouvées dans une grille

    Args:
        grille (list): grille

    Returns:
        int: nombre de mine
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

    Args:
        grille (list): grille
    """
    for i in range(len(grille)):
        line = [getContenuGrilleDemineur(grille, (i, j)) for j in range(
            getNbColonnesGrilleDemineur(grille))]
        print(line)
    return None


def gagneGrilleDemineur(grille: list) -> bool:
    """Determine si une partie est gagnée

    Args:
        grille (list): grille de la partie

    Returns:
        bool: True si la partie est gagné, False sinon
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

    Args:
        grille (_type_): grille de la partie

    Returns:
        bool: True si la partie est perdu, False sinon
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

    Args:
        grille (list): grille
    """
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbLignesGrilleDemineur(grille)):
            reinitiliserCellule(getCelluleGrilleDemineur(grille, (i, j)))
    return None


def decouvrirGrilleDemineur(grille: list, coord: tuple) -> set:
    """Découvre (rend visible) la cellule ainsi que ces voisines si elle n'est pas voisiné par une mine

    Args:
        grille (list): grille de la partie
        coord (tuple): coordonnée de la première cellule à découvrir

    Returns:
        set: coordonnées des cellules rendus visible
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

    Args:
        grille (list): grille de la partie
        coord (tuple): coordonnées de la cellule

    Returns:
        set: coordonnées des cellules rendus visible
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
                # 
                if nbFlag == getContenuGrilleDemineur(grille, currentCoord):
                    for voisin in voisins:
                        if not getAnnotationGrilleDemineur(grille, voisin) == const.FLAG:
                            setVisibleGrilleDemineur(grille, voisin, True)
                            cellulesADecouvrir.append(voisin)
                cellulesDecouvertes.add(currentCoord)
        return cellulesDecouvertes


def ajouterFlagsGrilleDemineur(grille: list, coord: tuple) -> set:
    """Place les drapeaux lorsque le nombre de voisins correpond au contenu de la cellule

    Args:
        grille (list): grille de la partie
        coord (tuple): coordonnées de la cellule

    Returns:
        set: coordonnées des cellules marqués d'un drapeau
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


def simplifierToutGrilleDemineur(grille: list) -> tuple:
    """Aide à la résolution : simplifie la grille

    Args:
        grille (list): grille de la partie

    Returns:
        tuple: coordonnées des cellules découvertes et coordonnées des cellules marqués d'un drapeau
    """
    isModifie = True
    simplifie = set()
    ajoute = set()
    while isModifie:
        isModifie = False
        for i in range(getNbLignesGrilleDemineur(grille)):
            for j in range(getNbColonnesGrilleDemineur(grille)):
                cell = getCelluleGrilleDemineur(grille, (i, j))
                if cell[const.VISIBLE] and cell[const.RESOLU] != 0:
                    a = ajouterFlagsGrilleDemineur(grille, (i, j))
                    s = simplifierGrilleDemineur(grille, (i, j))
                    if len(s) != 0 or len(a) != 0:
                        print(f"on peut decouvrir : {s}")
                        print(f"on peut flag : {a}")
                        isModifie = True if not isModifie else None
                        cell[const.RESOLU] = 1
                        simplifie = simplifie.union(s)
                        ajoute = ajoute.union(a)
                        """Problème : Que signifie résolu ? Quand la valeur associé à const.RESOLU doit être 'Résolu' """
    #print(simplifie, ajoute)
    return (simplifie, ajoute)
