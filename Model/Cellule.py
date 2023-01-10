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

    Args:
        n (int): contenu de la cellule

    Returns:
        bool: True, si le contenu est correcte, False sinon
    """
    return n == const.ID_MINE or 8 >= n >= 0 if type(n) == int else False


def construireCellule(contenu: int = 0, visible: bool = False) -> dict:
    """Construit une cellule

    Args:
        contenu (int, optional): contenu de la nouvelle cellule. Defaults to 0.
        visible (bool, optional): visibilité de la nouvelle cellule. Defaults to False.

    Raises:
        ValueError: contenu incorrecte
        TypeError: visibilité incorrecte

    Returns:
        dict: cellule
    """
    if not isContenuCorrect(contenu):
        raise ValueError(f"construireCellule : le contenu {contenu} n'est pas correct")
    if type(visible) != bool:
        raise TypeError(f"cconstruireCellule : le second paramètre ({type(visible)})n'est pas un booléen")
    return {const.CONTENU: contenu, const.VISIBLE: visible, const.ANNOTATION: None, const.RESOLU: ""}


def getContenuCellule(cell: dict) -> int:
    """Récupère le contenu d'une cellule

    Args:
        cell (dict): cellule

    Raises:
        TypeError: le paramètre n'est pas une cellule

    Returns:
        int: contenu de la cellule
    """
    if not type_cellule(cell):
        raise TypeError("getContenuCellule : Le paramètre n'est pas une cellule")
    return cell.get(const.CONTENU)


def isVisibleCellule(cell: dict) -> bool:
    """Récupère la visibilité d'une cellule

    Args:
        cell (dict): cellule

    Raises:
        TypeError: le paramètre n'est pas une cellule

    Returns:
        bool: visibilité de la cellule
    """
    if not type_cellule(cell):
        raise TypeError("isVisibleCellule : Le paramètre n'est pas une cellule")
    return cell.get(const.VISIBLE)


def setContenuCellule(cell: dict, contenu: int) -> None:
    """Modifie le contenu d'une cellule

    Args:
        cell (dict): cellule à modifier
        contenu (int): nouveau contenu de la cellule

    Raises:
        TypeError: le premier paramètre n'est pas une cellule
        TypeError: le second paramètre n'est pas un entier
        ValueError: le contenu n'est pas correcte
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

    Args:
        cell (dict): cellule à modifier
        visible (bool): nouvelle visibilité de la cellule

    Raises:
        TypeError: le premier paramètre n'est pas une cellule
        TypeError: le second paramètre n'est pas de bon type

    Returns:
        _type_: _description_
    """
    if not type_cellule(cell):
        raise TypeError("setVisibleCellule : Le premier paramètre n'est pas une cellule")
    if type(visible) != bool:
        raise TypeError("setVisibleCellule : Le second paramètre n'est pas un entier")
    cell[const.VISIBLE] = visible
    return None


def contientMineCellule(cell: dict) -> bool:
    """Vérifie si une cellule contient une mine

    Args:
        cell (dict): cellule à vérifier

    Raises:
        TypeError: le paramètre n'est pas une cellule

    Returns:
        bool: True, si la cellule contient une mine, False sinon
    """
    if not type_cellule(cell):
        raise TypeError("contientMineCellule: Le  paramètre n'est pas une cellule")
    return getContenuCellule(cell) == const.ID_MINE


def isAnnotationCorrecte(annotation: str) -> bool:
    """Vérifie que l'annotation est correcte

    La fonction vérifie que la valeur de l'annotation est l'une des valeurs suivantes : const.DOUTE, const.FLAG, None

    Args:
        annotation (str): annotation à vérifier

    Returns:
        bool: True, si l'annotation est correcte, False sinon
    """
    return annotation == const.DOUTE or annotation == const.FLAG or annotation == None


def getAnnotationCellule(cell: dict) -> str:
    """Récupère l'annotation d'une cellule

    Args:
        cell (dict): cellule

    Raises:
        TypeError: le paramètre n'est pas une cellule

    Returns:
        str: annotation de la cellule
    """
    if not type_cellule(cell):
        raise TypeError(f"getAnnotationCellule : le paramètre {cell} n'est pas une cellule")
    return cell.get(const.ANNOTATION, None)


def changeAnnotationCellule(cell: dict) -> None:
    """Modifie l'annotation d'une cellule

    Le changement suit l'ordre suivant :
    None -> const.FLAG -> const.DOUTE
    et reviens au départ ensuite

    Args:
        cell (dict): cellule à modifier

    Raises:
        TypeError: le paramètre n'est pas une cellule
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

    Args:
        cell (dict): cellule à réinitialiser
    """
    cell[const.CONTENU] = 0
    cell[const.VISIBLE] = False
    cell[const.ANNOTATION] = None
    cell[const.RESOLU] = False

    return None
