from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from uuid import uuid4

class Entity(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    
    id: str = Field(default_factory=lambda: str(uuid4()))
    created_at: datetime = Field(default_factory=datetime.now)