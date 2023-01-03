# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0


def construireCoordonnee(y: int, x: int) -> tuple:
    if type(x) != type(int()) or type(y) != type(int()):
        raise TypeError(f"ConstruireCoordonnee : Le numéro de ligne {type(y)} ou le numéro de colonne {type(x)} ne sont pas des entiers")
    elif x < 0 or y < 0:
        raise ValueError(f"construireCoordonnee : Le numéro de ligne ({y}) ou de colonne ({x}) ne sont pas positif")
    else:
        return y, x


def getLigneCoordonnee(coord: tuple) -> int:
    if not type_coordonnee(coord):
        raise TypeError("getLigneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coord[0]


def getColonneCoordonnee(coord: tuple) -> int:
    if not type_coordonnee(coord):
        raise TypeError("getLigneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coord[1]