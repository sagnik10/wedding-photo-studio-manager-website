def calculate_score(lead):
    score = 0

    if lead.message:
        score += 5

    if lead.phone:
        score += 5

    if "wedding" in (lead.message or "").lower():
        score += 10

    return score


def score_lead(lead):
    lead.score = calculate_score(lead)
    lead.save()