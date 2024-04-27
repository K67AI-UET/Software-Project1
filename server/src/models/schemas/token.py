from pydantic import BaseModel


class Token(BaseModel):
    id: str
    access_token: str
    refresh_token: str


class RefreshToken(BaseModel):
    id: str
    refresh_token: str
