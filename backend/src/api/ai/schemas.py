from pydantic import BaseModel


class EmailMessageSchema(BaseModel):
    subject: str
    content: str
    invalid_request: bool = False