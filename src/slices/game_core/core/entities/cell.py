from enum import Enum


class CellState(Enum):
    """
    Representa el estado de una célula en el Juego de la Vida.
    """

    DEAD = 0
    ALIVE = 1


class Cell:
    """
    Representa una célula individual en el tablero del Juego de la Vida.
    """

    def __init__(self, state: CellState):
        """
        Inicializa una nueva célula.

        Args:
            state: El estado inicial de la célula (ALIVE o DEAD).
        """
        self.state = state

    def is_alive(self) -> bool:
        """
        Verifica si la célula está viva.

        Returns:
            True si la célula está viva, False en caso contrario.
        """
        return self.state == CellState.ALIVE

    def set_state(self, state: CellState):
        """
        Establece el estado de la célula.

        Args:
            state: El nuevo estado de la célula.
        """
        self.state = state

    def __repr__(self) -> str:
        """
        Representación de cadena de la célula.
        """
        return "X" if self.is_alive() else "."

    def __eq__(self, other):
        """
        Compara dos células por su estado.
        """
        if not isinstance(other, Cell):
            return NotImplemented
        return self.state == other.state

    def __hash__(self):
        """
        Calcula el hash de la célula basado en su estado.
        """
        return hash(self.state)
