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
    if type(li) != int or type(col) != int:
        raise TypeError(f"construireGrilleDemineur : Le nombre delignes ({li}) ou de colonnes ({col})) n’est pas un entier.")
    if li < 1 or col < 1:
        raise ValueError(f"construireGrilleDemineur : Le nombre de lignes ({li}) ou de colonnes ({col}) est négatif ou nul.")
    grille = []
    for y in range(li):
        ligne = []
        for x in range(col):
            ligne.append(construireCellule())
        grille.append(ligne)
    return grille


def getNbLignesGrilleDemineur(grille: list) -> int:
    if not type_grille_demineur(grille):
        raise TypeError("getNbLignesGrilleDemineur : Le paramètre n'est pas une grille")
    else:
        return len(grille)


def getNbColonnesGrilleDemineur(grille: list) -> int:
    if not type_grille_demineur(grille):
        raise TypeError("getNbColonneGrilleDemineur : Le paramètre n'est pas une grille")
    else:
        return len(grille[0])


def isCoordonneeCorrecte(grille: list, coord: tuple) -> bool:
    if type(coord) != tuple or type(grille) != list or not type_grille_demineur(grille)\
            or len(coord) != 2 or type(coord[0]) != int or type(coord[1]) != int:
        raise TypeError("isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    else:
        return getNbLignesGrilleDemineur(grille) > coord[0] and getNbColonnesGrilleDemineur(grille) > coord[1]


def getCelluleGrilleDemineur(grille: list, coord: tuple) -> dict:
    if type(coord) != tuple or type(grille) != list or not type_grille_demineur(grille):
        raise TypeError("getCelluleGrilleDemineur : un des paramètres n’est pas du bon type.")
    elif not isCoordonneeCorrecte(grille, coord):
        raise IndexError("getCelluleGrilleDemineur : coordonnée non contenue dans la grille.")
    else:
        return grille[coord[0]][coord[1]]


def getContenuGrilleDemineur(grille: list, coord: tuple) -> int:
    return getContenuCellule(getCelluleGrilleDemineur(grille, coord))


def setContenuGrilleDemineur(grille: list, coord: tuple, contenu: int) -> None:
    setContenuCellule(getCelluleGrilleDemineur(grille, coord), contenu)
    return None


def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    return isVisibleCellule(getCelluleGrilleDemineur(grille, coord))


def setVisibleGrilleDemineur(grille: list, coord: tuple, visible: bool) -> None:
    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), visible)


def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    return contientMineCellule(getCelluleGrilleDemineur(grille, coord))


def getCoordonneeVoisinsGrilleDemineur(grille: list, coord: tuple) -> list:
    voisins = []
    minLigneVoisin, maxLigneVoisin, minColonneVoisin, maxColonneVoisin = (0,0,0,0)
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

    for i in range(minLigneVoisin, maxLigneVoisin+1):
        for j in range(minColonneVoisin, maxColonneVoisin+1):
            if (i, j) != coord:
                voisins.append((i, j))
    return voisins


def placerMinesGrilleDemineur(grille: list, nb: int, coord: tuple) -> None:
    w, h = getNbLignesGrilleDemineur(grille), getNbColonnesGrilleDemineur(grille)
    if not isCoordonneeCorrecte(grille, coord):
        raise IndexError("placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille")
    elif nb < 0 or nb >= (w*h):
        raise ValueError("placerMinesGrilleDemineur : Nombre de bombes à placer incorrect")
    else:
        while nb > 0:
            i, j = coord
            while (i, j) == coord:
                i = randint(0, w-1)
                j = randint(0, h-1)
            cellule = getCelluleGrilleDemineur(grille, (i, j))
            if not contientMineCellule(cellule):
                setContenuCellule(cellule, const.ID_MINE)
                nb -= 1
    return None

