from typing import List, Tuple

import numpy as np

from .cell import Cell, CellState


class Board:
    """
    Representa el tablero bidimensional del Juego de la Vida.
    """

    def __init__(self, width: int, height: int):
        """
        Inicializa un nuevo tablero vacío.

        Args:
            width: El ancho del tablero.
            height: El alto del tablero.
        """
        self.width = width
        self.height = height
        # Usamos NumPy para un grid eficiente
        self._grid = np.empty((height, width), dtype=object)
        self._next_grid = np.empty((height, width), dtype=object)
        
        # Inicializar cada célula individualmente
        for y in range(height):
            for x in range(width):
                self._grid[y, x] = Cell(CellState.DEAD)
                self._next_grid[y, x] = Cell(CellState.DEAD)

    def get_cell(self, x: int, y: int) -> Cell:
        """
        Obtiene la célula en una posición específica.

        Args:
            x: Coordenada X.
            y: Coordenada Y.

        Returns:
            La célula en la posición (x, y).
        """
        # Implementar manejo de bordes (toroidal) si es necesario más adelante
        # Por ahora, asumo que las coordenadas están dentro de los límites
        if 0 <= x < self.width and 0 <= y < self.height:
            return self._grid[y, x]
        # Podríamos lanzar una excepción o manejar el borde toroidal
        raise IndexError("Coordenadas fuera de los límites del tablero")

    def set_cell(self, x: int, y: int, state: CellState):
        """
        Establece el estado de la célula en una posición específica.

        Args:
            x: Coordenada X.
            y: Coordenada Y.
            state: El nuevo estado de la célula.
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self._grid[y, x].set_state(state)
        else:
            raise IndexError("Coordenadas fuera de los límites del tablero")

    def get_neighbors(self, x: int, y: int) -> List[Cell]:
        """
        Obtiene las células vecinas de una célula en una posición específica,
        considerando bordes toroidales.

        Args:
            x: Coordenada X de la célula central.
            y: Coordenada Y de la célula central.

        Returns:
            Una lista de las 8 células vecinas.
        """
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue  # No incluir la célula central

                neighbor_x = (x + i) % self.width
                neighbor_y = (y + j) % self.height
                neighbors.append(self._grid[neighbor_y, neighbor_x])
        return neighbors

    def calculate_next_state(self, x: int, y: int) -> CellState:
        """
        Calcula el próximo estado de una célula basándose en sus vecinos
        y las reglas del Juego de la Vida.

        Args:
            x: Coordenada X de la célula.
            y: Coordenada Y de la célula.

        Returns:
            El próximo estado calculado para la célula.
        """
        cell = self.get_cell(x, y)
        neighbors = self.get_neighbors(x, y)
        live_neighbors = sum(1 for neighbor in neighbors if neighbor.is_alive())

        if cell.is_alive():
            # Regla 1: Una célula viva con menos de 2 vecinos vivos muere (subpoblación).
            # Regla 2: Una célula viva con 2 o 3 vecinos vivos sobrevive a la siguiente generación.
            # Regla 3: Una célula viva con más de 3 vecinos vivos muere (sobrepoblación).
            if live_neighbors < 2 or live_neighbors > 3:
                return CellState.DEAD
            else:
                return CellState.ALIVE
        else:
            # Regla 4: Una célula muerta con exactamente 3 vecinos vivos nace.
            if live_neighbors == 3:
                return CellState.ALIVE
            else:
                return CellState.DEAD

    def calculate_all_next_states(self):
        """
        Calcula el próximo estado para todas las células del tablero
        y lo almacena en un grid temporal.
        """
        for y in range(self.height):
            for x in range(self.width):
                next_state = self.calculate_next_state(x, y)
                # Almacenar el próximo estado en el grid temporal
                self._next_grid[y, x] = Cell(next_state)

    def apply_next_state(self):
        """
        Aplica los estados calculados en el grid temporal al grid principal.
        """
        # Copiar los estados del grid temporal al grid principal
        for y in range(self.height):
            for x in range(self.width):
                self._grid[y, x].set_state(self._next_grid[y, x].state)
                self._next_grid[y, x].set_state(CellState.DEAD)

    def get_next_state(self) -> List[List[CellState]]:
        """
        Obtiene el próximo estado calculado del tablero como una lista de listas de CellState.

        Returns:
            Una lista de listas que representa el próximo estado calculado del tablero.
        """
        state = []
        for row in self._next_grid:
            state.append([cell.state for cell in row])
        return state

    def initialize(self, initial_state: List[Tuple[int, int]]):
        """
        Inicializa el tablero con un estado inicial dado por una lista de coordenadas de células vivas.

        Args:
            initial_state: Lista de tuplas (x, y) de células que estarán vivas.
        """
        self.clear()  # Limpiar el tablero actual
        for x, y in initial_state:
            if 0 <= x < self.width and 0 <= y < self.height:
                self.set_cell(x, y, CellState.ALIVE)
            # Podríamos añadir manejo de errores para coordenadas fuera de rango si es necesario

    def clear(self):
        """
        Establece todas las células del tablero a estado muerto.
        """
        self._grid = np.empty((self.height, self.width), dtype=object)
        self._next_grid = np.empty((self.height, self.width), dtype=object)
        
        # Inicializar cada célula individualmente
        for y in range(self.height):
            for x in range(self.width):
                self._grid[y, x] = Cell(CellState.DEAD)
                self._next_grid[y, x] = Cell(CellState.DEAD)

    def get_state(self) -> List[List[CellState]]:
        """
        Obtiene el estado actual del tablero como una lista de listas de CellState.

        Returns:
            Una lista de listas que representa el estado del tablero.
        """
        state = []
        for row in self._grid:
            state.append([cell.state for cell in row])
        return state

    def __repr__(self) -> str:
        """
        Representación de cadena del tablero.
        """
        return "\n".join("".join(str(cell) for cell in row) for row in self._grid)

    def __eq__(self, other):
        """
        Compara dos tableros por su estado.
        """
        if not isinstance(other, Board):
            return NotImplemented
        if self.width != other.width or self.height != other.height:
            return False
        return np.array_equal(self._grid, other._grid)

    def __hash__(self):
        """
        Calcula el hash del tablero basado en su estado.
        """
        return hash(
            self._grid.tobytes()
        )  # Usar tobytes() para un hash basado en el contenido del array
