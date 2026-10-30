from pydantic import BaseModel, Field
from typing import Literal


class PatientCreate(BaseModel):
    name: str = Field(..., min_length=2)
    city: str
    age: int = Field(..., gt=0, lt=120)
    gender: Literal["Male", "Female", "Other"]
    height: float = Field(..., gt=0)
    weight: float = Field(..., gt=0)


class PatientUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2)
    city: str | None = None
    age: int | None = Field(default=None, gt=0, lt=120)
    gender: Literal["Male", "Female", "Other"] | None = None
    height: float | None = Field(default=None, gt=0)
    weight: float | None = Field(default=None, gt=0)


class PatientResponse(PatientCreate):
    id: int