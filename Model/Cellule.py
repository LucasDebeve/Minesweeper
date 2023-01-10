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
    """Vérifie que le contenu est correcte

    La fonction vérifie que le contenu coorespond à l'une des entiers suivantes : const.ID_MINE, 0, 1, 2, 3, 4, 5, 6, 7, 8

    :param n: contenu de la cellule
    :type n: int
    :return: True, si le contenu est correcte, False sinon
    :rtype: bool
    """
    return n == const.ID_MINE or 8 >= n >= 0 if type(n) == int else False


def construireCellule(contenu: int = 0, visible: bool = False) -> dict:
    """Construit une cellule

    :param contenu: contenu de la nouvelle cellule. Defaults to 0., defaults to 0
    :type contenu: int, optional
    :param visible: visibilité de la nouvelle cellule. Defaults to False., defaults to False
    :type visible: bool, optional
    :raises ValueError: contenu incorrecte
    :raises TypeError: visibilité incorrecte
    :return: cellule
    :rtype: dict
    """
    if not isContenuCorrect(contenu):
        raise ValueError(f"construireCellule : le contenu {contenu} n'est pas correct")
    if type(visible) != bool:
        raise TypeError(f"cconstruireCellule : le second paramètre ({type(visible)})n'est pas un booléen")
    return {const.CONTENU: contenu, const.VISIBLE: visible, const.ANNOTATION: None, const.RESOLU: ""}


def getContenuCellule(cell: dict) -> int:
    """Récupère le contenu d'une cellule

    :param cell: cellule
    :type cell: dict
    :raises TypeError: le paramètre n'est pas une cellule
    :return: contenu de la cellule
    :rtype: int
    """
    if not type_cellule(cell):
        raise TypeError("getContenuCellule : Le paramètre n'est pas une cellule")
    return cell.get(const.CONTENU)


def isVisibleCellule(cell: dict) -> bool:
    """Récupère la visibilité d'une cellule

    :param cell: cellule
    :type cell: dict
    :raises TypeError: le paramètre n'est pas une cellule
    :return: visibilité de la cellule
    :rtype: bool
    """
    if not type_cellule(cell):
        raise TypeError("isVisibleCellule : Le paramètre n'est pas une cellule")
    return cell.get(const.VISIBLE)


def setContenuCellule(cell: dict, contenu: int) -> None:
    """Modifie le contenu d'une cellule

    :param cell: cellule à modifier
    :type cell: dict
    :param contenu: nouveau contenu de la cellule
    :type contenu: int
    :raises TypeError: le premier paramètre n'est pas une cellule
    :raises TypeError: le second paramètre n'est pas un entier
    :raises ValueError: le contenu n'est pas correcte
    """
    if not type_cellule(cell):
        raise TypeError("setContenuCellule : Le premier paramètre n'est pas une cellule")
    if type(contenu) != int:
        raise TypeError("setContenuCellule : Le second paramètre n'est pas un entier")
    elif not isContenuCorrect(contenu):
        raise ValueError(f"setContenuCellule : la valeur du contenu ({contenu}) n,'est pas correcte")
    cell[const.CONTENU] = contenu
    return None


def setVisibleCellule(cell: dict, visible: bool) -> None:
    """Modifie la visibilité d'une cellule

    :param cell: cellule à modifier
    :type cell: dict
    :param visible: nouvelle visibilité de la cellule
    :type visible: bool
    :raises TypeError: le premier paramètre n'est pas une cellule
    :raises TypeError: le second paramètre n'est pas de bon type
    """
    if not type_cellule(cell):
        raise TypeError("setVisibleCellule : Le premier paramètre n'est pas une cellule")
    if type(visible) != bool:
        raise TypeError("setVisibleCellule : Le second paramètre n'est pas un entier")
    cell[const.VISIBLE] = visible
    return None


def contientMineCellule(cell: dict) -> bool:
    """Vérifie si une cellule contient une mine

    :param cell: cellule à vérifier
    :type cell: dict
    :raises TypeError: le paramètre n'est pas une cellule
    :return: True, si la cellule contient une mine, False sinon
    :rtype: bool
    """
    if not type_cellule(cell):
        raise TypeError("contientMineCellule: Le  paramètre n'est pas une cellule")
    return getContenuCellule(cell) == const.ID_MINE


def isAnnotationCorrecte(annotation: str) -> bool:
    """Vérifie que l'annotation est correcte

    La fonction vérifie que la valeur de l'annotation est l'une des valeurs suivantes : const.DOUTE, const.FLAG, None

    :param annotation: annotation à vérifier
    :type annotation: str
    :return: True, si l'annotation est correcte, False sinon
    :rtype: bool
    """
    return annotation == const.DOUTE or annotation == const.FLAG or annotation == None


def getAnnotationCellule(cell: dict) -> str:
    """Récupère l'annotation d'une cellule

    :param cell: cellule
    :type cell: dict
    :raises TypeError: le paramètre n'est pas une cellule
    :return: annotation de la cellule
    :rtype: str
    """
    if not type_cellule(cell):
        raise TypeError(f"getAnnotationCellule : le paramètre {cell} n'est pas une cellule")
    return cell.get(const.ANNOTATION, None)


def changeAnnotationCellule(cell: dict) -> None:
    """Modifie l'annotation d'une cellule

    Le changement suit l'ordre suivant :
    None -> const.FLAG -> const.DOUTE
    et reviens au départ ensuite

    :param cell: cellule à modifier
    :type cell: dict
    :raises TypeError: le paramètre n'est pas une cellule
    """
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


def reinitiliserCellule(cell: dict) -> None:
    """Réinistialiser une cellule

    Une cellule réinitialisée est égale à : {const.CONTENU: 0, const.VISIBLE: False, const.ANNOTATION: None, const.RESOLU: False}

    :param cell: cellule à réinitialiser
    :type cell: dict
    """
    cell[const.CONTENU] = 0
    cell[const.VISIBLE] = False
    cell[const.ANNOTATION] = None
    cell[const.RESOLU] = False

    return None
