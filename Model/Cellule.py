# Model/Cellule.py
#

from Model.Constantes import *
import const


#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
           and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
           and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect(n: int) -> bool:
    return n == const.ID_MINE or 8 >= n >= 0 if type(n) == int else False


def construireCellule(content: int = 0, visibility: bool = False) -> dict:
    if not isContenuCorrect(content):
        raise ValueError(f"construireCellule : le contenu {content} n'est pas correct")
    if type(visibility) != bool:
        raise TypeError(f"cconstruireCellule : le second paramètre ({type(visibility)})n'est pas un booléen")
    return {const.CONTENU: content, const.VISIBLE: visibility}


