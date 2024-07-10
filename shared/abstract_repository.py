import abc

from shared.custom_types.entity_id import EntityId
from shared.entities.entity_base import EntityBase


class AbstractRepository(abc.ABC):
    
    @abc.abstractmethod
    def get_by_id(self, entity_id: EntityId) -> EntityBase:
        raise NotImplementedError
    
    @abc.abstractmethod
    def insert(self, entity: EntityBase) -> EntityId:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, entity: EntityBase) -> EntityBase:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_by_id(self, entity_id: EntityId) -> None:
        raise NotImplementedError