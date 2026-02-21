import pytest

from calculator import aftrekken, delen, optellen, vermenigvuldigen


def test_optellen_positieve_getallen():
    """Test optellen met twee positieve getallen."""
    assert optellen(3, 4) == 7


def test_optellen_negatief_getal():
    """Test optellen met een negatief getal."""
    assert optellen(-2, 5) == 3


def test_optellen_nul():
    """Test optellen waarbij een operand nul is."""
    assert optellen(0, 9) == 9


def test_aftrekken_positieve_getallen():
    """Test aftrekken met twee positieve getallen."""
    assert aftrekken(10, 4) == 6


def test_aftrekken_negatief_resultaat():
    """Test aftrekken waarbij het resultaat negatief is."""
    assert aftrekken(3, 7) == -4


def test_aftrekken_nul():
    """Test aftrekken waarbij de aftrekker nul is."""
    assert aftrekken(5, 0) == 5


def test_vermenigvuldigen_positieve_getallen():
    """Test vermenigvuldigen met twee positieve getallen."""
    assert vermenigvuldigen(3, 4) == 12


def test_vermenigvuldigen_met_nul():
    """Test vermenigvuldigen waarbij een factor nul is."""
    assert vermenigvuldigen(7, 0) == 0


def test_vermenigvuldigen_negatieve_getallen():
    """Test vermenigvuldigen met twee negatieve getallen geeft positief resultaat."""
    assert vermenigvuldigen(-3, -4) == 12


def test_delen_positieve_getallen():
    """Test delen met twee positieve getallen."""
    assert delen(10, 2) == 5


def test_delen_kommagetal():
    """Test delen waarbij het resultaat een kommagetal is."""
    assert delen(7, 2) == 3.5


def test_delen_door_nul():
    """Test dat delen door nul een ValueError gooit."""
    with pytest.raises(ValueError, match="Deler mag niet nul zijn."):
        delen(5, 0)
