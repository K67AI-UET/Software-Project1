from .base import BaseController

from src.repositories import KeyRepository
from src.models import Key


class KeyController(BaseController[Key]):
    def __init__(self, repository: KeyRepository):
        super().__init__(model=Key, repository=KeyRepository)
        self.repository = repository

    def get_by_userId(self, userId: str) -> Key | None:
        return self.repository.get_one({"userId": userId})
