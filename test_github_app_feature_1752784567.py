# Tests for GitHub App Authentication Feature
import pytest
from github_app_feature_1752784567 import github_app_greeting, get_timestamp

def test_github_app_greeting():
    """Test the GitHub App greeting function."""
    result = github_app_greeting("Test User")
    assert "Hello from GitHub App, Test User!" in result
    assert "1752784567" in result

def test_get_timestamp():
    """Test the timestamp function."""
    assert get_timestamp() == "1752784567"

def test_greeting_with_special_characters():
    """Test greeting with special characters."""
    result = github_app_greeting("Test@User.com")
    assert "Hello from GitHub App, Test@User.com!" in result
