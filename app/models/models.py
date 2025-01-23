from sqlmodel import Field, SQLModel


class Pet(SQLModel, table=True):
    id: int = Field(primary_key=True)  # UUID if necessary
    name: str = Field(description="pet name")
    breed: str = Field(description="pet breed")
    age: int = Field(description="pet age")


class Owner(SQLModel, table=True):
    id: int = Field(primary_key=True)  # UUID if necessary
    name: str = Field(description="owner name")
    contact_info: dict = Field(description="phone, email, etc.")
