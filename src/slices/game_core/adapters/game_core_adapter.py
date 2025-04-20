from typing import List, Optional, Tuple

from src.slices.game_core.core.entities.board import Board
from src.slices.game_core.core.entities.cell import CellState
from src.slices.game_core.core.use_cases.apply_next_generation_use_case import (
    ApplyNextGenerationUseCase,
)
from src.slices.game_core.core.use_cases.calculate_next_generation_use_case import (
    CalculateNextGenerationUseCase,
)
from src.slices.game_core.core.use_cases.initialize_board_use_case import (
    InitializeBoardUseCase,
)

# Importar casos de uso para modificación y consulta si se crean
# from src.slices.game_core.core.use_cases.set_cell_state_use_case import SetCellStateUseCase
# from src.slices.game_core.core.use_cases.clear_board_use_case import ClearBoardUseCase
# from src.slices.game_core.core.use_cases.get_board_state_use_case import GetBoardStateUseCase
# from src.slices.game_core.core.use_cases.get_cell_state_use_case import GetCellStateUseCase
from src.slices.game_core.ports.primary_ports.board_initialization_port import (
    IBoardInitializationPort,
)
from src.slices.game_core.ports.primary_ports.board_modification_port import (
    IBoardModificationPort,
)
from src.slices.game_core.ports.primary_ports.board_query_port import IBoardQueryPort
from src.slices.game_core.ports.primary_ports.game_simulation_port import (
    BoardState,  # Importar BoardState desde el puerto
    IGameSimulationPort,
)


class GameCoreAdapter(
    IBoardInitializationPort,
    IGameSimulationPort,
    IBoardQueryPort,
    IBoardModificationPort,
):
    """
    Adaptador que implementa los puertos primarios del slice Game Core
    y delega las llamadas a los casos de uso correspondientes.
    """

    def __init__(
        self,
        initialize_board_use_case: InitializeBoardUseCase,
        calculate_next_generation_use_case: CalculateNextGenerationUseCase,
        apply_next_generation_use_case: ApplyNextGenerationUseCase,
        set_cell_state_use_case,
        clear_board_use_case,
        get_board_state_use_case,
        get_cell_state_use_case,
    ):
        """
        Inicializa el adaptador con las dependencias de casos de uso.
        """
        self._initialize_board_use_case = initialize_board_use_case
        self._calculate_next_generation_use_case = calculate_next_generation_use_case
        self._apply_next_generation_use_case = apply_next_generation_use_case
        self._set_cell_state_use_case = set_cell_state_use_case
        self._clear_board_use_case = clear_board_use_case
        self._get_board_state_use_case = get_board_state_use_case
        self._get_cell_state_use_case = get_cell_state_use_case

    # Implementación de IBoardInitializationPort
    def initialize_board(
        self,
        width: int,
        height: int,
        initial_state: Optional[List[Tuple[int, int]]] = None,
    ) -> Board:
        """
        Delega la inicialización del tablero al caso de uso correspondiente.
        """
        return self._initialize_board_use_case.execute(width, height, initial_state)

    # Implementación de IGameSimulationPort
    def calculate_next_generation(self, board: Board) -> BoardState:
        """
        Delega el cálculo de la próxima generación al caso de uso correspondiente.
        """
        # El caso de uso calcula y almacena en el board._next_grid
        self._calculate_next_generation_use_case.execute(board)
        # Retornar el estado calculado (desde board._next_grid)
        # Necesitamos una forma de obtener el estado del _next_grid
        # Podríamos añadir un método get_next_state() a la entidad Board
        # O el caso de uso podría retornar el estado calculado
        # Por ahora, asumiré que el caso de uso modifica el board in-place
        # y que podemos obtener el estado del _next_grid directamente para el retorno
        # Esto puede requerir ajuste en el diseño de la entidad/caso de uso si se prefiere inmutabilidad
        # Para el prototipo, asumiré que Board tiene un método get_next_state() o similar
        # O que el caso de uso retorna el estado calculado
        # Dado que el caso de uso actual modifica el board in-place,
        # y apply_next_generation usa ese estado, el retorno aquí es un poco ambiguo
        # Si el caso de uso calculate_all_next_states() modifica board._next_grid,
        # entonces necesitamos obtener el estado de board._next_grid para retornarlo.
        # Añadiré un método get_next_state() a Board para esto.
        return board.get_next_state()  # Asumiendo que este método existe en Board

    def apply_next_generation(self, board: Board, next_state: BoardState) -> Board:
        """
        Delega la aplicación de la próxima generación al caso de uso correspondiente.
        """
        # El caso de uso apply_next_state() usa el estado ya calculado en board._next_grid
        # El parámetro next_state aquí es redundante con el diseño actual de Board
        # Si el diseño de Board cambiara para ser inmutable o para que calculate_next_generation
        # retorne el estado sin modificar el board, entonces este parámetro sería útil.
        # Con el diseño actual, simplemente llamamos al caso de uso.
        self._apply_next_generation_use_case.execute(board)
        return board

    # Implementación de IBoardQueryPort
    def get_board_state(self, board: Board) -> BoardState:
        """
        Delega la obtención del estado del tablero.
        """
        return board.get_state()

    def get_cell_state(self, board: Board, x: int, y: int) -> CellState:
        """
        Delega la obtención del estado de una célula.
        """
        return board.get_cell(x, y).state

    # Implementación de IBoardModificationPort
    def set_cell_state(self, board: Board, x: int, y: int, state: CellState) -> Board:
        """
        Delega el establecimiento del estado de una célula.
        """
        board.set_cell(x, y, state)
        return board

    def clear_board(self, board: Board) -> Board:
        """
        Delega la limpieza del tablero.
        """
        board.clear()
        return board


# Nota: La entidad Board necesita un método get_next_state() para que calculate_next_generation funcione como diseñado en el Port.
# Añadiré este método a la clase Board.
