from pydantic import BaseModel, field_validator


class Task(BaseModel):
    x: int
    y: int
    oper: str

    @field_validator('oper')
    @classmethod
    def validate_oper(cls, v: str) -> str:
        if v not in '+-/*':
            raise ValueError('значение должно быть одним из "-, *, +, /"')
        return v


class Tasks(BaseModel):
    id: int
    status: str
