
import src.exercise


def test_double_it():
    assert 8 == src.exercise.main(4)
    assert 0 == src.exercise.main(0)
    assert -2 == src.exercise.main(-1)
