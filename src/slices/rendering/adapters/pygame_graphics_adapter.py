from typing import List, Tuple

import pygame

from src.slices.game_core.core.entities.cell import CellState
from src.slices.game_core.core.entities.board import Board  # Usar importación absoluta
from src.slices.rendering.core.rendering_config import (
    RenderingConfig,  # Usar importación absoluta
)
from src.slices.rendering.ports.secondary_ports.graphics_library_port import (
    IGraphicsLibraryPort,
)

# Definimos un tipo para el estado del tablero para mayor claridad
BoardState = List[List[CellState]]


class PygameGraphicsAdapter(IGraphicsLibraryPort):
    """
    Adaptador que implementa el puerto secundario IGraphicsLibraryPort
    utilizando la biblioteca Pygame.
    """

    def __init__(self, config: RenderingConfig):
        """
        Inicializa el adaptador de Pygame.
        """
        pygame.init()
        pygame.font.init()
        self.config = config
        self.status_height = 30  # Altura de la barra de estado
        window_width = config.grid_width * config.cell_size
        window_height = config.grid_height * config.cell_size + self.status_height
        self.screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Game of Life")
        self._clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 24)  # Fuente para el texto
        self.show_help = False  # Controla si se muestra la ventana de ayuda

    def initialize(self, width: int, height: int):
        """
        Inicializa Pygame y crea la ventana de visualización.

        Args:
            width: Ancho de la ventana.
            height: Alto de la ventana.
        """
        pass

    def clear_screen(self):
        """Limpia la pantalla"""
        self.screen.fill(self.config.background_color)

    def get_screen(self):
        """
        Obtiene la pantalla.
        """
        return self.screen

    def draw_board(self, board, config=None, stats=None):
        """Dibuja el tablero completo"""
        self.draw_cells(board)
        self.draw_grid(board)
        if stats:
            self.draw_status_bar(stats)
        if self.show_help:
            self.draw_help_window()
        self.update_display()

    def draw_cell(self, x: int, y: int, state: bool):
        """Dibuja una celda individual"""
        if state:
            pygame.draw.rect(
                self.screen,
                self.config.cell_color,
                (x * self.config.cell_size, y * self.config.cell_size,
                 self.config.cell_size - 1 if self.config.show_grid else self.config.cell_size,
                 self.config.cell_size - 1 if self.config.show_grid else self.config.cell_size)
            )

    def draw_cells(self, board):
        """
        Dibuja las células del tablero.

        Args:
            board: La instancia del tablero.
        """
        cell_size = self.config.cell_size
        cell_size_inner = cell_size - 1 if self.config.show_grid else cell_size

        # Dibujar el fondo primero
        self.screen.fill(self.config.background_color)

        # Luego dibujar solo las células vivas
        for y in range(board.height):
            for x in range(board.width):
                cell_state = board.get_cell(x, y).state
                if cell_state == CellState.ALIVE:
                    pygame.draw.rect(
                        self.screen,
                        self.config.cell_color,
                        (x * cell_size, y * cell_size, cell_size_inner, cell_size_inner)
                    )

    def draw_grid(self, board):
        """
        Dibuja el grid del tablero.

        Args:
            board: La instancia del tablero.
        """
        if self.config.show_grid:
            for x in range(0, board.width * self.config.cell_size, self.config.cell_size):
                pygame.draw.line(self.screen, self.config.grid_color, (x, 0),
                                 (x, board.height * self.config.cell_size))
            for y in range(0, board.height * self.config.cell_size, self.config.cell_size):
                pygame.draw.line(self.screen, self.config.grid_color, (0, y),
                                 (board.width * self.config.cell_size, y))

    def update_display(self):
        """
        Actualiza la pantalla para mostrar lo que se ha dibujado.
        """
        pygame.display.flip()

    def quit(self):
        """
        Cierra Pygame.
        """
        pygame.quit()

    def draw_status_bar(self, stats):
        """
        Dibuja la barra de estado con las estadísticas.

        Args:
            stats: Objeto SimulationMetrics con las estadísticas actuales.
        """
        # Crear el fondo de la barra de estado
        status_rect = pygame.Rect(0, self.config.grid_height * self.config.cell_size,
                                self.config.grid_width * self.config.cell_size, self.status_height)
        pygame.draw.rect(self.screen, (50, 50, 50), status_rect)

        # Crear el texto con las estadísticas
        status_text = f"Gen: {stats.generation} | Vivas: {stats.alive} | Tiempo: {stats.step_time:.2f}ms | H para ayuda"
        text_surface = self.font.render(status_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(status_rect.centerx, status_rect.centery))
        self.screen.blit(text_surface, text_rect)

    def draw_help_window(self):
        """
        Dibuja la ventana de ayuda con los atajos de teclado.
        """
        # Crear una superficie semitransparente
        help_surface = pygame.Surface((400, 300))
        help_surface.fill((30, 30, 30))
        help_surface.set_alpha(230)

        # Posicionar la ventana en el centro
        help_rect = help_surface.get_rect(center=(self.screen.get_width() // 2,
                                                self.screen.get_height() // 2))

        # Lista de atajos
        shortcuts = [
            "Atajos de Teclado:",
            "",
            "ESPACIO - Pausar/Reanudar",
            "C - Limpiar tablero",
            "R - Reiniciar con patrón aleatorio",
            "H - Mostrar/Ocultar ayuda",
            "ESC - Salir",
            "",
            "Click - Cambiar estado de célula"
        ]

        # Dibujar el fondo
        self.screen.blit(help_surface, help_rect)

        # Dibujar el texto
        for i, line in enumerate(shortcuts):
            text_surface = self.font.render(line, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(help_rect.centerx,
                                                    help_rect.top + 30 + i * 30))
            self.screen.blit(text_surface, text_rect)

    def get_cell_coords_from_mouse_pos(
        self, mouse_pos: Tuple[int, int]
    ) -> Tuple[int, int]:
        """
        Convierte la posición del ratón en coordenadas de celda del tablero.

        Args:
            mouse_pos: La posición (x, y) del ratón en píxeles.

        Returns:
            Las coordenadas (x, y) de la celda correspondiente.
        """
        cell_x = mouse_pos[0] // self.config.cell_size
        # Ajustar la coordenada Y para tener en cuenta la barra de estado
        cell_y = mouse_pos[1] // self.config.cell_size
        if cell_y >= self.config.grid_height:
            cell_y = self.config.grid_height - 1
        return cell_x, cell_y
