from pydantic import BaseModel, Field, field_validator

# product validation models
class Product(BaseModel):
    name: str = Field(description="product name", min_length=3, max_length=50)
    price: float = Field(description="product price")
    description: str = Field(description="product description", min_length=15, max_length=150)
    imageUrl: str = Field(description="product image url")

    @field_validator("price")
    @classmethod
    def validate_price(cls, v):
        if v < 0:
            raise ValueError("Price must be grater thaan 0")
        return v