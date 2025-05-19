from pydantic import BaseModel, Field

class URLPOSTschames(BaseModel):
    url_target: str


class URLGETschemas(URLPOSTschames):
    url_key: str