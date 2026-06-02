from pydantic import BaseModel, Field, EmailStr, field_validator

class Cliente(BaseModel):
    nome : str = Field(min_length=2)
    cidade : str = Field(min_length=3)
    email : EmailStr

    @field_validator('nome')
    def nome_sem_espaco(cls, value : str) -> str :
        if " " not in value:
            raise ValueError("O nome deve conter ao menos um espaço")
        return value