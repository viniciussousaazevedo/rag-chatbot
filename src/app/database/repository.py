from app.errors.bad_request import BadRequestError
from typing import TypeVar, Optional, Generic, Any
from app.util.data_transfer_handler import *
from app.database.extensions import mongo
from app.util.logger import enable_logs
from app.model.entity import Entity

T = TypeVar("T", bound=Entity)

class Repository(Generic[T]):
    def __init__(self, entity_class: type[T]):
        if not issubclass(entity_class, Entity):
            raise ValueError("class provided must be a subclass of app.model.entity.Entity")

        self.entity_class = entity_class
        self.collection = entity_class.__name__.lower()

    @enable_logs
    def find(self, field_name: str, field_value: str) -> Optional[T]:
        raw_entity = mongo.db[self.collection].find_one({field_name: field_value})
        if not raw_entity:
            return None
        return to_object(raw_entity, self.entity_class)

    @enable_logs
    def get(self, field_name: str, field_value: str) -> T:
        if field_name == 'id':
            field_name = '_id'

        entity = self.find(field_name, field_value)
        if not entity:
            raise BadRequestError("entity not found")
        return entity

    @enable_logs
    def exists(self, field_name: str, field_value: str) -> bool:
        return self.find(field_name, field_value) is not None

    @enable_logs
    def save(self, entity: T) -> T:
        raw_entity = to_dict(entity)
        raw_entity["_id"] = str(entity.id)
        if 'id' in raw_entity:
            raw_entity.pop("id")

        mongo.db[self.collection].update_one(
            {"_id": raw_entity["_id"]},
            {"$set": raw_entity},
            upsert=True  # Creates if it does not exist
        )
        return entity
    
    @enable_logs
    def clear(self) -> None:
        mongo.db[self.collection].delete_many({})

    @enable_logs
    def find_all(self, query: Optional[dict[str, Any]] = None) -> list[T]:
        query = query or {}
        cursor = mongo.db[self.collection].find(query)
        return [to_object(d, self.entity_class) for d in cursor]
