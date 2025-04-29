import json
import os

def make_api_config(name, description, model, handler, response_schema=None):
    desc = description.strip()
    INCLUDE_RESPONSE_SCHEMA = os.getenv("INCLUDE_RESPONSE_SCHEMA")
    if INCLUDE_RESPONSE_SCHEMA == "true" and response_schema:
        desc += f"\nReturns response following this schema:\n{json.dumps(response_schema, indent=2)}"
    return {
        "name": name,
        "description": desc,
        "model": model,
        "schema": model.model_json_schema(),
        "handler": handler,
    }
