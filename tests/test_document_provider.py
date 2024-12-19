import pytest
import os
from src.document_provider import GeminiDocumentProvider

def test_provider_initialization():
    """Test if provider initializes with environment variable"""
    os.environ['GEMINI_API_KEY'] = 'dummy_key'
    provider = GeminiDocumentProvider()
    assert provider is not None

def test_provider_initialization_with_key():
    """Test if provider initializes with explicit key"""
    provider = GeminiDocumentProvider(api_key='dummy_key')
    assert provider is not None

def test_provider_initialization_fails_without_key():
    """Test if provider raises error without API key"""
    if 'GEMINI_API_KEY' in os.environ:
        del os.environ['GEMINI_API_KEY']
    with pytest.raises(ValueError):
        provider = GeminiDocumentProvider()

def test_get_context_method_exists():
    """Test if get_context method exists"""
    provider = GeminiDocumentProvider(api_key='dummy_key')
    assert hasattr(provider, 'get_context')
    assert callable(getattr(provider, 'get_context'))

def test_get_grounded_response_method_exists():
    """Test if get_grounded_response method exists"""
    provider = GeminiDocumentProvider(api_key='dummy_key')
    assert hasattr(provider, 'get_grounded_response')
    assert callable(getattr(provider, 'get_grounded_response'))
