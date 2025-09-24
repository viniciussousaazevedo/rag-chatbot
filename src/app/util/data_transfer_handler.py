from enum import Enum
from flask import jsonify
from pydantic import BaseModel
    
# ---------- Response ----------
def response(obj, target_class=None):
    """
    Converts a Python object to a Flask JSON response, optionally mapping it to another Pydantic class first.
    Args:
        obj: The object to serialize in the response.
        target_class: Optional. If provided, attempts to cast `obj` into this Pydantic class before serialization.
    Returns:
        A Flask `Response` object containing JSON data.
    """
    if target_class:
        if isinstance(obj, list):
            obj = [target_class.model_validate(to_dict(item)) for item in obj]
        else:
            obj = target_class.model_validate(to_dict(obj))
    return jsonify(to_dict(obj))

# ---------- Model Mapping ----------
def to_object(raw_obj, pydantic_class):
    """
    Converts a dictionary into an instance of the specified Pydantic class.
    Args:
        obj_dict: A dictionary containing the data to populate the Pydantic model.
        pydantic_class: The Pydantic model class to instantiate.
    Returns:
        An instance of `pydantic_class` populated with `obj_dict` data.
    """
    if "_id" in raw_obj:
        raw_obj["id"] = raw_obj["_id"]
        raw_obj.pop("_id", None)
    if isinstance(raw_obj, list):
        return [to_object(item, pydantic_class) for item in raw_obj]
    return pydantic_class(**raw_obj)

def to_dict(obj):
    """
    Converts an object into a dictionary suitable for JSON serialization.
    Args:
        obj: The object to convert. Can be a Pydantic model, dict, list, or plain object.
    Returns:
        A dictionary or list of dictionaries representing the object(s), ready to be serialized to JSON.
    """
    if isinstance(obj, BaseModel):
        raw_obj = obj.model_dump()
        for k, v in raw_obj.items():
            if isinstance(v, Enum):
                raw_obj[k] = v.value
        return raw_obj
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, list):
        return [to_dict(c) for c in obj]
    return obj.__dict__
    