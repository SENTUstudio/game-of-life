from typing import Any, Tuple

from .event_type import EventType


class InputEvent:
    """
    Representa un evento de entrada del usuario.
    """

    def __init__(
        self,
        type: EventType,
        position: Tuple[int, int] = None,
        button_or_key: Any = None,
    ):
        """
        Inicializa un nuevo evento de entrada.

        Args:
            type: El tipo de evento.
            position: La posición asociada al evento (ej. coordenadas del ratón). Opcional.
            button_or_key: Detalle específico del evento (ej. botón del ratón, tecla presionada). Opcional.
        """
        self.type = type
        self.position = position
        self.button_or_key = button_or_key

    def __repr__(self) -> str:
        """
        Representación de cadena del evento de entrada.
        """
        return f"InputEvent(type={self.type}, position={self.position}, button_or_key={self.button_or_key})"
