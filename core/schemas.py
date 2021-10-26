from typing import List, Optional

from pydantic import BaseModel


class DocumentBase(BaseModel):
    text: str


class DocumentCreate(DocumentBase):
    class Config:
        orm_mode = True


class Document(DocumentBase):
    id: int

    class Config:
        orm_mode = True
