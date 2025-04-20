import sys
import pygame
import random
import time

from src.slices.simulation.core.entities.simulation_metrics import SimulationMetrics

from src.slices.game_core.core.config import GameConfig
from src.slices.game_core.core.entities.board import Board
from src.slices.game_core.core.entities.cell import CellState

from src.slices.game_core.adapters.game_core_adapter import GameCoreAdapter
from src.slices.game_core.core.use_cases.apply_next_generation_use_case import ApplyNextGenerationUseCase
from src.slices.game_core.core.use_cases.calculate_next_generation_use_case import CalculateNextGenerationUseCase
from src.slices.game_core.core.use_cases.clear_board_use_case import ClearBoardUseCase
from src.slices.game_core.core.use_cases.get_board_state_use_case import GetBoardStateUseCase
from src.slices.game_core.core.use_cases.get_cell_state_use_case import GetCellStateUseCase
from src.slices.game_core.core.use_cases.initialize_board_use_case import InitializeBoardUseCase
from src.slices.game_core.core.use_cases.set_cell_state_use_case import SetCellStateUseCase
from src.slices.game_core.ports.primary_ports.board_initialization_port import IBoardInitializationPort
from src.slices.game_core.ports.primary_ports.board_modification_port import IBoardModificationPort
from src.slices.game_core.ports.primary_ports.board_query_port import IBoardQueryPort
from src.slices.game_core.ports.primary_ports.game_simulation_port import IGameSimulationPort

from src.slices.rendering.adapters.pygame_graphics_adapter import PygameGraphicsAdapter
from src.slices.rendering.adapters.rendering_adapter import RenderingAdapter
from src.slices.rendering.adapters.rendering_query_adapter import RenderingQueryAdapter
from src.slices.rendering.adapters.rendering_query_adapter import RenderingQueryAdapter as UserInteractionRenderingQueryAdapter

from src.slices.rendering.core.rendering_config import RenderingConfig
from src.slices.rendering.core.use_cases.render_board_use_case import RenderBoardUseCase
from src.slices.rendering.core.use_cases.update_rendering_config_use_case import UpdateRenderingConfigUseCase
from src.slices.rendering.ports.primary_ports.rendering_port import IRenderingPort
from src.slices.rendering.ports.primary_ports.rendering_query_port import IRenderingQueryPort
from src.slices.rendering.ports.primary_ports.rendering_query_port import IRenderingQueryPort as IUserInteractionRenderingQueryPort
from src.slices.rendering.ports.secondary_ports.graphics_library_port import IGraphicsLibraryPort
from src.slices.simulation_control.adapters.game_core_modification_adapter import (
    GameCoreModificationAdapter,
)
from src.slices.simulation_control.adapters.game_core_simulation_adapter import (
    GameCoreSimulationAdapter,
)
from src.slices.simulation_control.adapters.simulation_control_adapter import (
    SimulationControlAdapter,
)
from src.slices.simulation_control.adapters.simulation_control_adapter import (
    SimulationControlAdapter as UserInteractionSimulationControlAdapter,  # Renombrar
)

# Simulation Control
from src.slices.simulation_control.core.simulation_state import SimulationState
from src.slices.simulation_control.core.use_cases.clear_board_use_case import (
    ClearBoardUseCase,
)
from src.slices.simulation_control.core.use_cases.pause_simulation_use_case import (
    PauseSimulationUseCase,
)
from src.slices.simulation_control.core.use_cases.start_simulation_use_case import (
    StartSimulationUseCase,
)
from src.slices.simulation_control.core.use_cases.step_simulation_use_case import (
    StepSimulationUseCase,
)
from src.slices.simulation_control.core.use_cases.stop_simulation_use_case import (
    StopSimulationUseCase,
)
from src.slices.simulation_control.ports.primary_ports.simulation_control_port import (
    ISimulationControlPort,
)
from src.slices.simulation_control.ports.primary_ports.simulation_control_port import (
    ISimulationControlPort as IUserInteractionSimulationControlPort,  # Renombrar
)
from src.slices.simulation_control.ports.secondary_ports.game_core_modification_port import (
    IGameCoreModificationPort,
)
from src.slices.simulation_control.ports.secondary_ports.game_core_simulation_port import (
    IGameCoreSimulationPort,
)
from src.slices.statistics.adapters.game_core_query_adapter import (
    GameCoreQueryAdapter as StatisticsGameCoreQueryAdapter,  # Renombrar
)
from src.slices.statistics.adapters.simulation_control_notification_adapter import (
    SimulationControlNotificationAdapter,
)
from src.slices.statistics.adapters.statistics_adapter import StatisticsAdapter
from src.slices.statistics.core.entities.simulation_metrics import SimulationMetrics as StatisticsSimulationMetrics
from src.slices.statistics.core.use_cases.get_statistics_use_case import (
    GetStatisticsUseCase,
)
from src.slices.statistics.core.use_cases.update_statistics_use_case import (
    UpdateStatisticsUseCase,
)
from src.slices.statistics.ports.primary_ports.statistics_query_port import (
    IStatisticsQueryPort,
)
from src.slices.statistics.ports.secondary_ports.simulation_step_notification_port import (
    ISimulationStepNotificationPort,
)
from src.slices.user_interaction.adapters.game_core_modification_adapter import (
    GameCoreModificationAdapter as UserInteractionGameCoreModificationAdapter,  # Renombrar
)
from src.slices.user_interaction.adapters.game_core_query_adapter import (
    GameCoreQueryAdapter as UserInteractionGameCoreQueryAdapter,  # Renombrar
)
from src.slices.user_interaction.adapters.user_interaction_adapter import (
    UserInteractionAdapter,
)
from src.slices.user_interaction.core.use_cases.handle_control_command_use_case import (
    HandleControlCommandUseCase,
)
from src.slices.user_interaction.core.use_cases.modify_cell_state_by_click_use_case import (
    ModifyCellStateByClickUseCase,
)

# User Interaction
from src.slices.user_interaction.core.use_cases.process_input_event_use_case import (
    ProcessInputEventUseCase,
)
from src.slices.user_interaction.ports.primary_ports.input_event_port import (
    IInputEventPort,
)
from src.slices.user_interaction.ports.secondary_ports.board_modification_port import (
    IUserInteractionBoardModificationPort as IUserInteractionBoardModificationPort,  # Renombrar para evitar conflicto
)
from src.slices.user_interaction.ports.secondary_ports.board_query_port import (
    IUserInteractionBoardQueryPort as IUserInteractionBoardQueryPort,  # Renombrar
)


def main():
    # --- Dependency Injection Setup ---

    # Game Core Slice
    game_config = GameConfig()
    board = Board(game_config.grid_width, game_config.grid_height)  # Create initial empty board

    # Instanciar casos de uso
    initialize_board_use_case = InitializeBoardUseCase()
    calculate_next_generation_use_case = CalculateNextGenerationUseCase()
    apply_next_generation_use_case = ApplyNextGenerationUseCase()

    # Crear adaptador de Game Core
    game_core_adapter = GameCoreAdapter(
        initialize_board_use_case,
        calculate_next_generation_use_case,
        apply_next_generation_use_case,
        None,  # Placeholder para set_cell_state_use_case
        None,  # Placeholder para clear_board_use_case
        None,  # Placeholder para get_board_state_use_case
        None,  # Placeholder para get_cell_state_use_case,
    )

    # Instanciar casos de uso que dependen del adaptador
    set_cell_state_use_case = SetCellStateUseCase(game_core_adapter)
    clear_board_use_case = ClearBoardUseCase(game_core_adapter)
    get_board_state_use_case = GetBoardStateUseCase(game_core_adapter)
    get_cell_state_use_case = GetCellStateUseCase(game_core_adapter)

    # Actualizar el adaptador con los casos de uso
    game_core_adapter._set_cell_state_use_case = set_cell_state_use_case
    game_core_adapter._clear_board_use_case = clear_board_use_case
    game_core_adapter._get_board_state_use_case = get_board_state_use_case
    game_core_adapter._get_cell_state_use_case = get_cell_state_use_case

    # Asegurar que el adaptador implementa todos los puertos requeridos
    game_core_adapter: (
        IBoardInitializationPort
        & IBoardCalculationPort
        & IBoardModificationPort
        & IBoardQueryPort
    ) = game_core_adapter

    # Statistics Slice
    simulation_metrics = StatisticsSimulationMetrics()
    # Need GameCoreQueryAdapter for Statistics
    statistics_game_core_query_adapter = StatisticsGameCoreQueryAdapter(
        game_core_query_port=game_core_adapter  # Inject GameCoreAdapter as IBoardQueryPort
    )
    update_statistics_use_case = UpdateStatisticsUseCase(
        simulation_metrics=simulation_metrics,
        board_query_port=statistics_game_core_query_adapter,  # Inject adapter as IBoardQueryPort
    )
    get_statistics_use_case = GetStatisticsUseCase(
        simulation_metrics=simulation_metrics
    )
    statistics_adapter: IStatisticsQueryPort = StatisticsAdapter(
        get_statistics_use_case=get_statistics_use_case
    )
    simulation_control_notification_adapter: ISimulationStepNotificationPort = (
        SimulationControlNotificationAdapter(
            update_statistics_use_case=update_statistics_use_case
        )
    )

    # Simulation Control Slice
    simulation_state = SimulationState.STOPPED  # Initial state
    # Need GameCoreSimulationAdapter and GameCoreModificationAdapter for Simulation Control
    sc_game_core_simulation_adapter: IGameCoreSimulationPort = GameCoreSimulationAdapter(
        game_core_simulation_port=game_core_adapter  # Inject GameCoreAdapter as IGameSimulationPort
    )
    sc_game_core_modification_adapter: IGameCoreModificationPort = GameCoreModificationAdapter(
        game_core_modification_port=game_core_adapter  # Inject GameCoreAdapter as IBoardModificationPort
    )
    # Need SimulationStepNotificationPort for StepSimulationUseCase
    # Inject simulation_control_notification_adapter from Statistics slice
    step_simulation_use_case = StepSimulationUseCase(
        game_simulation_port=sc_game_core_simulation_adapter,  # Inject adapter as IGameCoreSimulationPort
        # simulation_step_notification_port=simulation_control_notification_adapter # Inject adapter as ISimulationStepNotificationPort
    )
    start_simulation_use_case = StartSimulationUseCase(
        simulation_state=simulation_state  # Inject the state instance
    )
    pause_simulation_use_case = PauseSimulationUseCase(
        simulation_state=simulation_state  # Inject the state instance
    )
    stop_simulation_use_case = StopSimulationUseCase(
        simulation_state=simulation_state,  # Inject the state instance
        board_modification_port=sc_game_core_modification_adapter,  # Inject adapter as IGameCoreModificationPort
    )
    clear_board_use_case = ClearBoardUseCase(
        board_modification_port=sc_game_core_modification_adapter  # Inject adapter as IGameCoreModificationPort
    )
    simulation_control_adapter: ISimulationControlPort = SimulationControlAdapter(
        start_simulation_use_case=start_simulation_use_case,
        pause_simulation_use_case=pause_simulation_use_case,
        stop_simulation_use_case=stop_simulation_use_case,
        step_simulation_use_case=step_simulation_use_case,
        clear_board_use_case=clear_board_use_case,
    )

    # Rendering Slice
    rendering_config = RenderingConfig(
        cell_size=game_config.cell_size,
        grid_width=game_config.grid_width,
        grid_height=game_config.grid_height
    )
    pygame_graphics_adapter: IGraphicsLibraryPort = (
        PygameGraphicsAdapter(rendering_config)
    )  # Concrete Pygame adapter
    # Need BoardQueryPort for RenderBoardUseCase
    rendering_game_core_query_adapter: IBoardQueryPort = UserInteractionGameCoreQueryAdapter(  # Usar el adaptador del slice User Interaction
        game_core_query_port=game_core_adapter  # Inject GameCoreAdapter as IBoardQueryPort
    )
    render_board_use_case = RenderBoardUseCase(
        graphics_library_port=pygame_graphics_adapter,  # Inject Pygame adapter as IGraphicsLibraryPort
        # board_query_port=rendering_game_core_query_adapter # Inject adapter as IBoardQueryPort
    )
    update_rendering_config_use_case = UpdateRenderingConfigUseCase(
        rendering_config=rendering_config  # Inject the config instance
    )
    rendering_adapter: IRenderingPort = RenderingAdapter(
        render_board_use_case=render_board_use_case,
        update_rendering_config_use_case=update_rendering_config_use_case,
        rendering_config=rendering_config,  # Inject the config instance
    )
    rendering_query_adapter: IRenderingQueryPort = RenderingQueryAdapter(
        rendering_config=rendering_config,  # Inject the config instance
        graphics_library_port=pygame_graphics_adapter,  # Inject Pygame adapter as IGraphicsLibraryPort
    )

    # User Interaction Slice
    # Need BoardModificationPort, BoardQueryPort, SimulationControlPort, RenderingQueryPort
    ui_game_core_modification_adapter: IUserInteractionBoardModificationPort = UserInteractionGameCoreModificationAdapter(
        game_core_modification_port=game_core_adapter  # Inject GameCoreAdapter as IBoardModificationPort
    )
    ui_game_core_query_adapter: IUserInteractionBoardQueryPort = UserInteractionGameCoreQueryAdapter(
        game_core_query_port=game_core_adapter  # Inject GameCoreAdapter as IBoardQueryPort
    )
    # Crear estado de simulación compartido
    simulation_state = SimulationState.STOPPED

    # Crear adaptadores de puertos secundarios
    game_core_modification_adapter = GameCoreModificationAdapter(game_core_adapter)
    game_core_simulation_adapter = GameCoreSimulationAdapter(game_core_adapter)

    # Crear casos de uso para el control de simulación
    start_simulation_use_case = StartSimulationUseCase(simulation_state)
    pause_simulation_use_case = PauseSimulationUseCase(simulation_state)
    stop_simulation_use_case = StopSimulationUseCase(simulation_state, game_core_modification_adapter)
    step_simulation_use_case = StepSimulationUseCase(game_core_simulation_adapter)
    clear_board_use_case = ClearBoardUseCase(game_core_modification_adapter)

    # Crear el adaptador de control de simulación
    simulation_control_adapter = SimulationControlAdapter(
        start_simulation_use_case=start_simulation_use_case,
        pause_simulation_use_case=pause_simulation_use_case,
        stop_simulation_use_case=stop_simulation_use_case,
        step_simulation_use_case=step_simulation_use_case,
        clear_board_use_case=clear_board_use_case
    )

    ui_simulation_control_adapter = simulation_control_adapter
    ui_rendering_query_adapter: IUserInteractionRenderingQueryPort = UserInteractionRenderingQueryAdapter(
        rendering_config=rendering_config,  # Inject the config instance
        graphics_library_port=pygame_graphics_adapter,  # Inject Pygame adapter as IGraphicsLibraryPort
    )

    modify_cell_state_by_click_use_case = ModifyCellStateByClickUseCase(
        board_modification_port=ui_game_core_modification_adapter,  # Inject adapter as IBoardModificationPort
        board_query_port=ui_game_core_query_adapter,  # Inject adapter as IBoardQueryPort
        graphics_library_port=pygame_graphics_adapter,  # Inject Pygame adapter as IGraphicsLibraryPort
        # rendering_query_port=ui_rendering_query_adapter # Inject adapter as IRenderingQueryPort
    )
    handle_control_command_use_case = HandleControlCommandUseCase(
        simulation_control_port=ui_simulation_control_adapter  # Inject adapter as ISimulationControlPort
    )
    # Need ApplicationControlPort for ProcessInputEventUseCase (for QUIT event)
    # For now, we'll handle QUIT directly in the main loop.
    process_input_event_use_case = ProcessInputEventUseCase(
        # modify_cell_state_by_click_use_case=modify_cell_state_by_click_use_case, # Inject case of use
        # handle_control_command_use_case=handle_control_command_use_case, # Inject case of use
    )

    # --- Application Setup ---
    board_width = 50
    board_height = 50
    cell_size = 10
    window_width = board_width * cell_size
    window_height = board_height * cell_size

    pygame_graphics_adapter.initialize(window_width, window_height)
    # Inicializar tablero con un planeador
    glider = [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]
    board = game_core_adapter.initialize_board(
        width=board_width,
        height=board_height,
        initial_state=glider
    )

    # Inicializar métricas
    simulation_metrics = SimulationMetrics()
    simulation_metrics.update(0, sum(1 for row in board.get_state() for cell in row if cell == CellState.ALIVE), 0.0)

    running = True
    last_step_time = time.time()
    font = pygame.font.Font(None, 36)

    paused = False

    # --- Main Application Loop ---
    while running:
        current_time = time.time()
        dt = current_time - last_step_time

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_c:
                    board = game_core_adapter.clear_board(board)
                    simulation_metrics.update(0, 0, 0.0)  # Reiniciar estadísticas
                elif event.key == pygame.K_r:
                    # Reiniciar con un patrón aleatorio
                    board = game_core_adapter.initialize_board(
                        width=game_config.grid_width,
                        height=game_config.grid_height,
                        initial_state=[(x, y) for x in range(game_config.grid_width) for y in range(game_config.grid_height) if random.random() < 0.3]
                    )
                    # Reiniciar estadísticas
                    alive_cells = sum(1 for row in board.get_state() for cell in row if cell == CellState.ALIVE)
                    simulation_metrics.update(0, alive_cells, 0.0)
                elif event.key == pygame.K_h:
                    pygame_graphics_adapter.show_help = not pygame_graphics_adapter.show_help
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Delegar al caso de uso de modificación por clic
                modify_cell_state_by_click_use_case.execute(
                    board, pygame.mouse.get_pos()
                )
                # Actualizar estadísticas manteniendo la generación actual
                alive_cells = sum(1 for row in board.get_state() for cell in row if cell == CellState.ALIVE)
                simulation_metrics.update(
                    simulation_metrics.generation,
                    alive_cells,
                    simulation_metrics.step_time
                )

        # Actualizar simulación si no está pausada
        if not paused and dt > 1 / game_config.simulation_speed:
            last_step_time = current_time
            start_time = time.time()
            
            # Calcular siguiente generación
            next_state = game_core_adapter.calculate_next_generation(board)
            board = game_core_adapter.apply_next_generation(board, next_state)
            
            # Actualizar estadísticas
            step_time = (time.time() - start_time) * 1000
            alive_cells = sum(1 for row in board.get_state() for cell in row if cell == CellState.ALIVE)
            simulation_metrics.update(
                simulation_metrics.generation + 1,
                alive_cells,
                step_time
            )

        # Renderizar
        pygame_graphics_adapter.draw_board(board, stats=simulation_metrics)

    # --- Cleanup ---
    pygame_graphics_adapter.quit()
    sys.exit()


if __name__ == "__main__":
    main()
