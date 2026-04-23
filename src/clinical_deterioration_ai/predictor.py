def predict_risk(score: float) -> str:
    if score >= 0.7:
        return "High Risk"
    elif score >= 0.4:
        return "Medium Risk"
    return "Low Risk"