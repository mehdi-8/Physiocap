"""
.. module:: test
   :synopsis: premier module

.. moduleauthor:: Micropole


"""

__docformat__ = 'restructuredtext'

from docutils import utils
from docutils.utils.error_reporting import ErrorOutput

def print_string(str):
    """
        Fonction qui retourne une chaine.

        Parameters:

        - `str`: la chaine à imprimer.
    """
    print(str)

def hello_world_modif4():
    """
        Fonction qui imprime un truc.

        utilise la fonction `print_string(str)` pour la sortie écran
    """
    print_string('yalla!!')
