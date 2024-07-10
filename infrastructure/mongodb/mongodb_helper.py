
from shared.abstract_repository import AbstractRepository
from shared.custom_types.entity_id import EntityId
from shared.custom_types.database_name import DatabaseName
from shared.custom_types.collection_name import CollectionName
from shared.entities.entity_base import EntityBase
import pymongo
from dependency_injector import containers, providers


class MongoClient:
    # "mongodb://localhost:27017/"
    def __init__(self, database_connection_string : str) -> None:
       self.client =  pymongo.MongoClient(database_connection_string)

    def get_database(self, database_name: DatabaseName):
        return self.client[database_name]
    

class MongoHelper(containers.DeclarativeContainer):
    mongo_client = providers.Singleton(MongoClient)