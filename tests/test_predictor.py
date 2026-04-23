from clinical_deterioration_ai import predict_risk

def test_high_risk():
    assert predict_risk(0.82) == "High Risk"

def test_medium_risk():
    assert predict_risk(0.55) == "Medium Risk"

def test_low_risk():
    assert predict_risk(0.12) == "Low Risk"