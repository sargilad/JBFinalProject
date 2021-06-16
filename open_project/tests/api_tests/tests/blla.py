import pytest


@pytest.mark.runme2
def test_div():
    with pytest.raises(ZeroDivisionError):
        1/2