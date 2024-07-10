import abc
from dataclasses import dataclass
from shared.custom_types.entity_id import EntityId

@dataclass
class EntityBase:
    entity_id: EntityId