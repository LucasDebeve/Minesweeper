view.Canvas
===========

    Classe permettant de créer et gérer une fenêtre.

    Exemple d'utilisation :

    .. code-block:: python

        from view.Canvas import Canvas

        # Création de la fenêtre
        cv = Canvas( (640, 480) )
        # Afficher/mettre à jour la fenêtre
        cv.display()

.. autoclass:: view.Canvas.Canvas
   :members:

.. NOTE::

    Fonction attachée à la fenêtre

.. autofunction:: view.Canvas.waitClick
.. autofunction:: view.Canvas.pause
