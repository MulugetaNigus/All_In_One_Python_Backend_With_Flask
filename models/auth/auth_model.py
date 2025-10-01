from multiprocessing import Value
from pydantic import BaseModel, EmailStr, Field, field_validator
import re

# user regstration filed validations
class User(BaseModel):
    email: EmailStr = Field(description="user email")
    password: str = Field(description="user password", 
                          min_length=8, max_length=54
                          )

    # validate password field
    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
      if not re.search(r'[a-z]', v):
          raise ValueError("password must contain at least one lowercase letter")
      if not re.search(r'[A-Z]', v):
          raise ValueError("password must contain at least one uppercase letter")
      if not re.search(r'[0-9]', v):
          raise ValueError("password must contain at least one digit")
      if not re.search(r'[!@#$%^&*()_+\-=\[\]{}|\\;:\'",./<>?]', v):
          raise ValueError("password must contain at least one special character")
      return v