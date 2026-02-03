from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class CreateUserSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=20)

class UpdateUserSchema(BaseModel):
    name:Optional[str] = Field(None, min_length=3, max_length=50)
    password: Optional[str] = Field(None, min_length=8, max_length=20)