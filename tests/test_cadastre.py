from waypoint_site_intelligence import query_parcel

def test_query_parcel():
    c = query_parcel(48.8566, 2.3522)
    assert "parcel" in c.result
    assert c.confidence > 0.9
