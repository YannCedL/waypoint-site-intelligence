# test du moteur de parcelles cadastrales IGN
from waypoint_site_intelligence.cadastre import query_parcel

def test_query_parcel():
    contract = query_parcel(48.8566, 2.3522)
    assert contract is not None
    assert contract.result["parcel"]["parcel_id"] is not None
    assert len(contract.evidence) >= 1
