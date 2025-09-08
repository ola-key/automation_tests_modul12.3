import pytest
from modules.api.clients.github import GitHub # Імпорт для фікстури github_api

class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Ola'
        self.second_name = 'Kliuch'
    
    def remove(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()

import pytest
from modules.api.clients.github import GitHub # Імпорт для фікстури github_api
@pytest.fixture
def github_api():
    return GitHub()

  