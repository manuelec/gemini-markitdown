import os
from dotenv import load_dotenv
from src.document_provider import GeminiDocumentProvider

def main():
    # Load environment variables
    load_dotenv()
    
    # Initialize provider
    provider = GeminiDocumentProvider()
    
    # Example usage
    document_path = "path/to/your/document.pdf"
    query = "What are the main points in this document?"
    
    try:
        response = provider.get_grounded_response(document_path, query)
        print("Response:", response)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
