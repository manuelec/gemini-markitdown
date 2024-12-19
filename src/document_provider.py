from markitdown import MarkItDown
import google.generativeai as genai
from google.generativeai import GenerativeModel
import os

class GeminiDocumentProvider:
    def __init__(self, api_key=None):
        """
        Initialize the GeminiDocumentProvider with Gemini 2.0 Flash model.
        
        Args:
            api_key (str, optional): Gemini API key. If not provided, reads from environment.
        """
        if api_key is None:
            api_key = os.getenv('GEMINI_API_KEY')
            if api_key is None:
                raise ValueError("API key must be provided or set in GEMINI_API_KEY environment variable")
        
        genai.configure(api_key=api_key)
        self.model = GenerativeModel('gemini-2.0-flash-exp')
        self.md = MarkItDown()
    
    def get_context(self, document_path):
        """Convert document to markdown format."""
        result = self.md.convert(document_path)
        return result.text_content
    
    def get_grounded_response(self, document_path, query):
        """
        Get a response grounded in the document context.
        
        Args:
            document_path (str): Path to the document
            query (str): User query about the document
            
        Returns:
            str: Generated response
        """
        context = self.get_context(document_path)
        
        prompt = f"""Context: {context}
        Question: {query}
        Answer based on the context provided."""
        
        response = self.model.generate_content(prompt)
        return response.text
