import pytest

@pytest.fixture
def dumpster():
    import dumpster_fire
    return dumpster_fire.DumpsterFire("Me")

def test_dims(dumpster):
    dumpster.win_height = 100
    dumpster.win_width = 100
    dumpster.dumpster_width = 50
    dumpster.dumpster_height = 10

    # The dumpster width start and width end should be centered along the
    # width of the window.
    (width_start, width_end, dumpster_top) = dumpster.calc_dumpster_dims()
    assert width_start == 25
    assert width_end == 75
    assert dumpster_top == 90
