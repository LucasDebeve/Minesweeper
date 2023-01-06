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


def construireCellule(contenu: int = 0, visible: bool = False) -> dict:
    if not isContenuCorrect(contenu):
        raise ValueError(f"construireCellule : le contenu {contenu} n'est pas correct")
    if type(visible) != bool:
        raise TypeError(f"cconstruireCellule : le second paramètre ({type(visible)})n'est pas un booléen")
    return {const.CONTENU: contenu, const.VISIBLE: visible, const.ANNOTATION: None}


def getContenuCellule(cell: dict) -> int:
    if not type_cellule(cell):
        raise TypeError("getContenuCellule : Le paramètre n'est pas une cellule")
    return cell.get(const.CONTENU)


def isVisibleCellule(cell: dict) -> bool:
    if not type_cellule(cell):
        raise TypeError("isVisibleCellule : Le paramètre n'est pas une cellule")
    return cell.get(const.VISIBLE)


def setContenuCellule(cell: dict, contenu: int) -> None:
    if not type_cellule(cell):
        raise TypeError("setContenuCellule : Le premier paramètre n'est pas une cellule")
    if type(contenu) != int:
        raise TypeError("setContenuCellule : Le second paramètre n'est pas un entier")
    elif not isContenuCorrect(contenu):
        raise ValueError(f"setContenuCellule : la valeur du contenu ({contenu}) n,'est pas correcte")
    cell[const.CONTENU] = contenu
    return None


def setVisibleCellule(cell: dict, visible: bool) -> None:
    if not type_cellule(cell):
        raise TypeError("setVisibleCellule : Le premier paramètre n'est pas une cellule")
    if type(visible) != bool:
        raise TypeError("setVisibleCellule : Le second paramètre n'est pas un entier")
    cell[const.VISIBLE] = visible
    return None


def contientMineCellule(cell: dict) -> bool:
    if not type_cellule(cell):
        raise TypeError("contientMineCellule: Le  paramètre n'est pas une cellule")
    return getContenuCellule(cell) == const.ID_MINE


def isAnnotationCorrecte(annotation: str) -> bool:
    return annotation == const.DOUTE or annotation == const.FLAG or annotation == None


def getAnnotationCellule(cell: dict) -> str:
    if not type_cellule(cell):
        raise TypeError(f"getAnnotationCellule : le paramètre {cell} n'est pas une cellule")
    return cell.get(const.ANNOTATION, None)


def changeAnnotationCellule(cell: dict) -> None:
    if not type_cellule(cell):
        raise TypeError("changeAnnotationCellule : le paramètre n'est pas une cellule")
    else:
        currentAnnotation = getAnnotationCellule(cell)
        if currentAnnotation == None:
            cell[const.ANNOTATION] = const.FLAG
        elif currentAnnotation == const.FLAG:
            cell[const.ANNOTATION] = const.DOUTE
        else:
            cell[const.ANNOTATION] = None
        return None

