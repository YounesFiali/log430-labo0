"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    welcome_message = my_calculator.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message

def test_init():
    my_calculator = Calculator()
    assert my_calculator is not None

def test_addition():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 5

def test_subtraction():
    my_calculator = Calculator()
    assert my_calculator.subtraction(5, 2) == 3

def test_multiplication():
    my_calculator = Calculator()
    assert my_calculator.multiplication(4, 3) == 12

def test_division():
    my_calculator = Calculator()
    assert my_calculator.division(10, 2) == 5

def test_division_by_zero():
    my_calculator = Calculator()
    assert my_calculator.division(10, 0) == "Erreur : division par zéro"
    assert my_calculator.last_result == "Error"