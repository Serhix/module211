from datetime import datetime

from pydantic import BaseModel, Field, EmailStr, constr

ValidPhone = constr(pattern="^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$")


class ContactModel(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: EmailStr
    phone: ValidPhone
    birthday: datetime
    description: str = Field(max_length=150)
    favorites: bool = False
    created_at: datetime
    updated_at: datetime


class ContactResponse(ContactModel):
    id: int = 1

    class Config:
        from_attributes = True
