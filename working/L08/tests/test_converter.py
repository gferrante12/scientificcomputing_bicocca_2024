from myexamplepkg.converter import joules_to_calories, calories_to_joules

def test_energy_conversions():
    assert abs(joules_to_calories(4184) - 1000) < 1e-6
    assert abs(calories_to_joules(1000) - 4184) < 1e-6