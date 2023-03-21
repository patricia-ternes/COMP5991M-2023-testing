import src.functions as fc
import pytest

"""
Function name: dice_simulator()
Number of sides: 6
is it fair: True

Return
- type: int
- min: 1
- max: 6
- distribution: 
    1/6: 1
    1/6: 2
    1/6: 3
    1/6: 4
    1/6: 5
    1/6: 6
"""


@pytest.fixture
def N():
    return 1_000_000


@pytest.fixture
def faces(N):
    faces = []
    for _ in range(N):
        faces.append(fc.dice_simulator())
    # faces = [fc.dice_simulator() for _ in range(N)]
    return faces


@pytest.fixture
def probalities(N, faces):
    p = []
    for i in range(6):
        p.append(faces.count(i + 1) / N)
    # p = [faces.count(i+1)/N for i in range(6)]
    return p


def test_type():
    assert isinstance(fc.dice_simulator(), int)


def test_min(faces):
    assert min(faces) == 1


def test_max(faces):
    assert max(faces) == 6


def test_distribution(probalities):
    for p in probalities:
        # assert p - 1/6 < 0.001
        assert pytest.approx(p) == 1 / 6
