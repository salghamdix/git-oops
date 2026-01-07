from app import get_greeting

def test_greeting():
    assert get_greeting("GitHub") == "Hello, GitHub! Welcome to GitOps."
