from credit import calculate_risk


def test_high_risk():
    result = calculate_risk(1000, 700, 30)
    assert result == "HIGH"


def test_medium_risk():
    result = calculate_risk(1000, 400, 30)
    assert result == "MEDIUM"


def test_low_risk():
    result = calculate_risk(1000, 100, 30)
    assert result == "LOW"


def test_zero_income():
    assert calculate_risk(0, 500, 30) == -1


def test_negative_income():
    assert calculate_risk(-1000, 500, 30) == -1


def test_zero_debt():
    assert calculate_risk(1000, 0, 30) == "LOW"


def test_ratio_exactly_0_3():
    # ratio = 0.3 : la condition est "> 0.3", donc 0.3 n'est pas MEDIUM
    assert calculate_risk(1000, 300, 30) == "LOW"


def test_ratio_exactly_0_6():
    # ratio = 0.6 : la condition est "> 0.6", donc 0.6 n'est pas HIGH
    assert calculate_risk(1000, 600, 30) == "MEDIUM"