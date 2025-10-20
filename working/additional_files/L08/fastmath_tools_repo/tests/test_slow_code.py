from fastmath_tools.slow_code import profile_demo

def test_speedup():
    result = profile_demo(100000)
    assert result["speedup ratio"] > 5
    #assert result["diff"] < 1e-10
