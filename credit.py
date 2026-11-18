HIGH_THRESHOLD = 0.6
MEDIUM_THRESHOLD = 0.3


def calculate_risk(income, debt, age=None):
    """Retourne le niveau de risque : HIGH, MEDIUM, LOW, ou -1 si revenu invalide.

    age est conservé pour compatibilité mais n'intervient pas dans le calcul.
    """
    if income <= 0:
        return -1

    ratio = debt / income

    if ratio > HIGH_THRESHOLD:
        return "HIGH"
    if ratio > MEDIUM_THRESHOLD:
        return "MEDIUM"
    return "LOW"