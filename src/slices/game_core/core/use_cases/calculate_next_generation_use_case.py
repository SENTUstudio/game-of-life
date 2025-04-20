from src.slices.game_core.core.entities.board import Board


class CalculateNextGenerationUseCase:
    """
    Caso de uso para calcular el próximo estado del tablero.
    """

    def execute(self, board: Board):
        """
        Calcula el próximo estado para todas las células del tablero
        y lo almacena internamente en el tablero.

        Args:
            board: La instancia del tablero actual.
        """
        board.calculate_all_next_states()
