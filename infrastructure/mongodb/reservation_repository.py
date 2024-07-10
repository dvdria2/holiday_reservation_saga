from infrastructure.mongodb.mongodb_helper import MongoHelper
from shared.abstract_repository import AbstractRepository
from shared.custom_types.collection_name import CollectionName
from shared.entities.entity_base import EntityBase
from shared.custom_types.entity_id import EntityId

class ReservationRepository(AbstractRepository):
    def __init__(self, collection_name: CollectionName) -> None:
        helper = MongoHelper()
        self.mongo_client = helper.mongo_client("mongodb://localhost:27017/")
        self.database = self.mongo_client.get_database("reservations")
        self.collection = self.database[collection_name]
        super().__init__()

    def get_by_id(self, entity_id: EntityId) -> EntityBase:
        return self.collection.find({"_id": entity_id})
    
    def insert(self, entity: EntityBase) -> EntityId:
        return self.collection.insert_one(entity.__dict__).inserted_id

    def update(self, entity: EntityBase) -> EntityBase:
        return self.collection.update_one({"_id", entity.entity_id}, entity.__dict__)

    def delete_by_id(self, entity_id: EntityId) -> None:
        return self.collection.delete_one({"_id": entity_id})