from enum import Enum


class EventType(Enum):
    """
    Representa los diferentes tipos de eventos de entrada del usuario.
    """

    MOUSE_CLICK = 0
    KEY_PRESS = 1
    QUIT = 2
    # Otros tipos de eventos relevantes (ej. MOUSE_MOTION, RESIZE)
