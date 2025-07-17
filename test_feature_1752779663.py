import pytest
from feature_1752779663 import greet

def test_greet():
    """Test the greet function."""
    result = greet("Test")
    assert "Hello, Test!" in result
    assert "1752779663" in result

def test_greet_empty():
    """Test greet with empty string."""
    result = greet("")
    assert "Hello, !" in result
