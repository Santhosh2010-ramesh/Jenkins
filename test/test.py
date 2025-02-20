# tests/test_example.py

from app import greet

def test_greet():
    assert greet("Jenkins") == "Hello, Jenkins!"
