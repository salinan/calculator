def optellen(a: float, b: float) -> float:
    """Telt twee getallen bij elkaar op en geeft het resultaat terug."""
    return a + b


def aftrekken(a: float, b: float) -> float:
    """Trekt het tweede getal af van het eerste en geeft het resultaat terug."""
    return a - b


def vermenigvuldigen(a: float, b: float) -> float:
    """Vermenigvuldigt twee getallen en geeft het resultaat terug."""
    return a * b


def delen(a: float, b: float) -> float:
    """Deelt het eerste getal door het tweede en geeft het resultaat terug.

    Raises:
        ValueError: Als de deler nul is.
    """
    if b == 0:
        raise ValueError("Deler mag niet nul zijn.")
    return a / b
