from src.slices.user_interaction.core.input_event import InputEvent
from src.slices.user_interaction.core.use_cases.process_input_event_use_case import (
    ProcessInputEventUseCase,
)
from src.slices.user_interaction.ports.primary_ports.input_event_port import (
    IInputEventPort,
)

# from src.slices.system.ports.primary_ports.application_control_port import IApplicationControlPort # Para notificar eventos de salida


class UserInteractionAdapter(IInputEventPort):
    """
    Adaptador que implementa el puerto primario IInputEventPort
    y delega el procesamiento de eventos al caso de uso correspondiente.
    """

    def __init__(
        self,
        process_input_event_use_case: ProcessInputEventUseCase,
        # application_control_port: IApplicationControlPort = None # Inyectar puerto de control de aplicación
    ):
        """
        Inicializa el adaptador con las dependencias de casos de uso y puertos.
        """
        self._process_input_event_use_case = process_input_event_use_case
        # self._application_control_port = application_control_port

    # Implementación de IInputEventPort
    def process_event(self, event: InputEvent):
        """
        Delega el procesamiento del evento de entrada al caso de uso correspondiente.
        """
        self._process_input_event_use_case.execute(event)
