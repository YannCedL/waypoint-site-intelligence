# modeles pour representer les parcelles cadastrales francaises
from typing import Optional
from pydantic import BaseModel, Field

class ParcelInfo(BaseModel):
    parcel_id: str = Field(..., description="Identifiant unique de la parcelle (ex: 751010000A0001)")
    section: Optional[str] = Field(None, description="Section cadastrale (ex: A, BD)")
    numero: Optional[str] = Field(None, description="Numero de parcelle")
    area_m2: Optional[float] = Field(None, description="Contenance / Surface en m2")
    commune: Optional[str] = Field(None, description="Nom ou code INSEE de la commune")
    code_insee: Optional[str] = Field(None, description="Code INSEE")
    owner_type: Optional[str] = Field(default="privé", description="Type de propriete")
