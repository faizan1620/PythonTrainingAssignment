from pydantic import BaseModel, validator

class Titanic(BaseModel):
    Age: int
    Fare: float
    TravelAlone: bool
    Pclass_1: bool
    Pclass_2: bool
    Embarked_C: bool
    Embarked_S: bool
    Sex_male: bool
    IsMinor: bool
    class Config:
        schema_extra = {
            "example": {
                "Age": 25,
                "Fare": 7.1,
                "TravelAlone": 1,
                "Pclass_1": 1,
                "Pclass_2": 0,
                "Embarked_C": 0,
                "Embarked_S": 1,
                "Sex_male": 1,
                "IsMinor": 1
            }
        }
    @validator('Age')
    def validate_age(cls, v):
        try:
            if v < 1 or v > 100:
                raise ValueError('Invalid age provided, provide valid age')
            return v
        except Exception:
            raise ValueError('Invalid age provided, provide valid age')