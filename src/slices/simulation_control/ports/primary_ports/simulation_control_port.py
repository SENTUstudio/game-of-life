from abc import ABC, abstractmethod

from src.slices.game_core.core.entities.board import (  # Usar importación absoluta
    Board,  # Necesitamos la instancia del tablero
)


class ISimulationControlPort(ABC):
    """
    Interfaz para controlar el flujo de la simulación.
    """

    @abstractmethod
    def start_simulation(self, board: Board):
        """
        Inicia la simulación automática.

        Args:
            board: La instancia del tablero actual.
        """
        pass

    @abstractmethod
    def pause_simulation(self):
        """
        Pausa la simulación automática.
        """
        pass

    @abstractmethod
    def stop_simulation(self, board: Board, clear_board: bool = True):
        """
        Detiene la simulación y opcionalmente limpia el tablero.

        Args:
            board: La instancia del tablero actual.
            clear_board: Si es True, limpia el tablero al detener la simulación.
        """
        pass

    @abstractmethod
    def step_simulation(self, board: Board) -> Board:
        """
        Ejecuta un solo paso de la simulación.

        Args:
            board: La instancia del tablero actual.

        Returns:
            La instancia del tablero actualizada después del paso.
        """
        pass

    @abstractmethod
    def clear_board(self, board: Board):
        """
        Establece todas las células del tablero a estado muerto.

        Args:
            board: La instancia del tablero actual.
        """
        pass
