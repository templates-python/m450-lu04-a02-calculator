"""Unit Tests für den Taschenrechner."""
import sys

import pytest

from calculator import divide


def test_success():
    """Zwei Zahlen werden korrekt dividiert."""
    result = divide(6, 4)
    assert result == pytest.approx(1.5)


@pytest.mark.xfail(raises=TypeError, reason='divide prüft die Eingaben nicht')
def test_invalid():
    """Buchstaben statt Zahlen."""
    divide('a', 2)


def test_zero_division():
    """Division durch 0 löst einen ZeroDivisionError aus."""
    with pytest.raises(ZeroDivisionError):
        divide(6, 0)


@pytest.mark.skip(reason='Dieser Test wird absichtlich übersprungen')
def test_mark_skip():
    """Wird immer übersprungen."""
    assert False


@pytest.mark.skipif(sys.version_info > (3, 8), reason='nur für Python 3.8 und älter')
def test_mark_skip_conditional():
    """Wird ab Python 3.9 übersprungen."""
    assert False


def test_pytest_skip():
    """Wird innerhalb der Funktion übersprungen."""
    if True:  # pylint: disable=using-constant-test
        pytest.skip('Die Bedingung ist erfüllt, der Test wird übersprungen')
    assert False
