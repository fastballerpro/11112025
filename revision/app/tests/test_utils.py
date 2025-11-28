from utils import is_valid_email, avg, uah_to_usd
import pytest

def test_strong_password():
    password = "sdfhvdhfivdhfsvfds"

def test_valid_email():
    assert is_valid_email("user@example.com") is True


def test_email_multiple_at():
    assert is_valid_email("a@b@c.com") is False


def test_email_no_dot_in_domain():
    assert is_valid_email("user@examplecom") is False


def test_email_empty_string():
    assert is_valid_email("") is False

def test_avg_normal_list():

    assert avg([1, 2, 3, 4]) == 2.5


def test_avg_one_element():
    assert avg([10]) == 10


def test_avg_negative_numbers():
    assert avg([-2, -4, -6]) == -4


def test_avg_empty_list_raises():
    with pytest.raises(ValueError):
        avg([])

def test_uah_to_usd_normal_case():
    assert uah_to_usd(1000, 40) == 25


def test_uah_to_usd_invalid_rate():
    with pytest.raises(ValueError):
        uah_to_usd(1000, 0)


def test_uah_to_usd_invalid_amount():
    with pytest.raises(ValueError):
        uah_to_usd(0, 35)


def test_uah_to_usd_large_values():
    assert uah_to_usd(1_000_000, 40) == 25000


def test_uah_to_usd_float_precision():
    assert abs(uah_to_usd(99.99, 36.6) - (99.99 / 36.6)) < 1e-9
import utils

def test_strong_password():
    password = "sdfhvdhfivdhfsvfds"
