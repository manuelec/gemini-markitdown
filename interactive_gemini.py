from src.document_provider import GeminiDocumentProvider
from dotenv import load_dotenv
import os

def main():
    # Load environment variables
    dotenv_path = 'gemini_api.env'
    load_dotenv(dotenv_path)

    # Initialize the provider
    provider = GeminiDocumentProvider()

    print("Welcome to Gemini MarkItDown Interactive!")
    print("----------------------------------------")
    
    # Get document path from user
    while True:
        document_path = input("\nEnter the path to your document (or 'quit' to exit): ")
        if document_path.lower() == 'quit':
            break
            
        if not os.path.exists(document_path):
            print("Error: File not found. Please check the path and try again.")
            continue
            
        # Enter query loop for the current document
        while True:
            print("\nDocument loaded. You can now ask questions about it.")
            query = input("Enter your question (or 'new' for different document, 'quit' to exit): ")
            
            if query.lower() == 'quit':
                return
            if query.lower() == 'new':
                break
                
            try:
                print("\nProcessing your query...")
                response = provider.get_grounded_response(document_path, query)
                print("\nGemini's Response:")
                print("------------------")
                print(response)
                print("\n------------------")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
