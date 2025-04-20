from abc import ABC, abstractmethod

from src.slices.user_interaction.core.input_event import InputEvent


class IInputEventPort(ABC):
    """
    Interfaz para recibir eventos de entrada del usuario.
    """

    @abstractmethod
    def process_event(self, event: InputEvent):
        """
        Procesa un evento de entrada del usuario.

        Args:
            event: El evento de entrada a procesar.
        """
        pass
