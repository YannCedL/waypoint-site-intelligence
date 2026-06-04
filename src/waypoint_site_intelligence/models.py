from typing import Optional
from pydantic import BaseModel, Field

class ParcelInfo(BaseModel):
    parcel_id: str
    area_m2: Optional[float] = None
    commune: Optional[str] = None
    owner_type: Optional[str] = None
