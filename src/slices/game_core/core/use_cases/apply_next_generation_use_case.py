from src.slices.game_core.core.entities.board import Board


class ApplyNextGenerationUseCase:
    """
    Caso de uso para aplicar el próximo estado calculado al tablero.
    """

    def execute(self, board: Board):
        """
        Aplica los estados calculados en el grid temporal del tablero
        al grid principal.

        Args:
            board: La instancia del tablero.
        """
        board.apply_next_state()
