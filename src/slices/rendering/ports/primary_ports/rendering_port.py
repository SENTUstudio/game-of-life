from abc import ABC, abstractmethod

from src.slices.game_core.core.entities.board import (  # Usar importación absoluta
    Board,  # Necesitamos la instancia del tablero
)


class IRenderingPort(ABC):
    """
    Interfaz para interactuar con la lógica de visualización.
    """

    @abstractmethod
    def render(self, board: Board) -> None:
        """
        Solicita renderizar el tablero dado.

        Args:
            board: La instancia del tablero a renderizar.
        """
        pass

    @abstractmethod
    def update_config(self, **kwargs):
        """
        Actualiza la configuración de visualización con los valores proporcionados.

        Args:
            **kwargs: Argumentos clave-valor para actualizar la configuración.
        """
        pass
