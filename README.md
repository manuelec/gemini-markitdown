# gemini-markitdown

A Python toolkit that combines Google's Gemini 2.0 Flash model with MarkItDown for intelligent document processing and question answering.

## Features

- Document conversion to markdown using MarkItDown
- Integration with Gemini 2.0 Flash for advanced language processing
- Support for multiple document formats (PDF, DOCX, etc.)
- Context-aware question answering

## Installation

pip install -r requirements.txt
text

## Quick Start

1. Set your Gemini API key:
export GEMINI_API_KEY='your-api-key'
text

2. Basic usage:
from src.document_provider import GeminiDocumentProvider
provider = GeminiDocumentProvider()
response = provider.get_grounded_response(
"path/to/document.pdf",
"What are the main points in this document?"
)
print(response)
text

## Supported Models

This implementation uses Gemini 2.0 Flash (`gemini-2.0-flash-exp`), which offers:
- 1M token context window
- Multimodal capabilities
- Fast processing speed
- Support for multiple languages

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
