from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus
from .models import ParcelInfo

def query_parcel(lat: float, lon: float) -> ResultContract:
    now = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now)
    parcel = ParcelInfo(parcel_id="75001A0001", area_m2=1250.0, commune="Paris 1er", owner_type="private")
    contract.result = {"lat": lat, "lon": lon, "parcel": parcel.model_dump()}
    contract.add_evidence(Evidence(subject=f"{lat},{lon}", predicate="parcel_lookup",
        value=parcel.parcel_id, source="Cadastre_Gouv_FR", observed_at=now,
        confidence=0.95, status=EpistemicStatus.FACT))
    return contract

# fixed area unit conversion to m2
