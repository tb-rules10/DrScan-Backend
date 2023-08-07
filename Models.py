from typing import Type
from pydantic import BaseModel

class PatientModel(BaseModel):
    name: str
    age: int
    height: float
    weight: float
    gender: str
    smoker: str
    smokerType: str
    alcoholConsumer: str
    hasExpectoration: str
    hasBreathShortness: str
    hasDiabetes: str
    mMRCgrade: str
    fev1PreBD: float
    fev1FVCPostBD: float
    goldGrade: int = None

