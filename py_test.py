import pytest


def test_capital_case():
    assert 'emaphore' == 'Semaphore'


def test_raises_exception_on_non_string_arguments():
    assert 2 != 2