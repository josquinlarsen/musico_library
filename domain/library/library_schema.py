from pydantic import BaseModel


# Pydantic schemas
class PieceCreate(BaseModel):
    title: str
    composer: str
    instrumentation: str
    duration: str


class PieceUpdate(BaseModel):
    title: str
    composer: str
    instrumentation: str
    duration: str


class PieceResponse(PieceCreate):
    id: int
