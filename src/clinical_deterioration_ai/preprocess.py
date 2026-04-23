def clean_age(age):
    return max(age, 0)

def normalize_score(score):
    return min(max(score, 0), 1)