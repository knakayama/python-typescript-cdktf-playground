from controllers.api import ApiController
from drivers.user_creation import UserCreationDriver
from modules.constants import table_name
from services.user_creation import UserCreationService
from use_cases.user_creation import UserCreationUseCase

controller = ApiController(
    UserCreationUseCase(UserCreationService(UserCreationDriver(table_name)))
)

handler = controller.handle
