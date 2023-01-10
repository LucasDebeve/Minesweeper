# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :type coord: tuple
    :return: True, si le paramètre correspond à une coordonnée, False sinon.
    :rtype: bool
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0


def construireCoordonnee(y: int, x: int) -> tuple:
    """_summary_

    :param y: coordonnée y, index de ligne
    :type y: int
    :param x: coordonnée x, index de colonne
    :type x: int
    :raises TypeError: les paramètres ne sont pas du bon type
    :raises ValueError: les paramètres ne sont pas positifs
    :return: coordonnées
    :rtype: tuple
    """
    if type(x) != int or type(y) != int:
        raise TypeError(f"ConstruireCoordonnee : Le numéro de ligne {type(y)} ou le numéro de colonne {type(x)} ne sont pas des entiers")
    elif x < 0 or y < 0:
        raise ValueError(f"construireCoordonnee : Le numéro de ligne ({y}) ou de colonne ({x}) ne sont pas positif")
    else:
        return y, x


def getLigneCoordonnee(coord: tuple) -> int:
    """Extrait la coordonnée y d'un tuple coordonnée

    :param coord: coordonnées
    :type coord: tuple
    :raises TypeError: le paramètre n'est pas une coordonnée
    :return: coordonnée y
    :rtype: int
    """
    if not type_coordonnee(coord):
        raise TypeError("getLigneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coord[0]


def getColonneCoordonnee(coord: tuple) -> int:
    """Extrait la coordonnée x d'un tuple coordonnée

    :param coord: coordonnées
    :type coord: tuple
    :raises TypeError: le paramètre n'est pas une coordonnée
    :return: coordonnée x
    :rtype: int
    """
    if not type_coordonnee(coord):
        raise TypeError("getLigneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coord[1]