# Import model classes directly from the models directory
from models.access.claude import ClaudeLLM
from models.access.openai import OpenAILLM
from models.access.gemini import GeminiLLM

# Function to initialize all LLMs
def initialize_llms(claude_api_key=None, openai_api_key=None, gemini_api_key=None):
    """
    Initialize multiple LLM instances with provided API keys.
    
    Args:
        claude_api_key (str): API key for Claude
        openai_api_key (str): API key for OpenAI
        gemini_api_key (str): API key for Gemini
        
    Returns:
        dict: Dictionary containing initialized LLM instances
    """
    llms = {}
    
    # Initialize Claude if API key is provided
    if claude_api_key:
        claude = ClaudeLLM(
            api_key=claude_api_key,
            temperature=0.0
        )
        claude.setup_client()
        llms["claude"] = claude
    
    # Initialize OpenAI if API key is provided
    if openai_api_key:
        openai_llm = OpenAILLM(
            api_key=openai_api_key,
            temperature=0.0
        )
        openai_llm.setup_client()
        llms["openai"] = openai_llm
    
    # Initialize Gemini if API key is provided
    if gemini_api_key:
        gemini = GeminiLLM(
            api_key=gemini_api_key,
            temperature=0.0
        )
        gemini.setup_client()
        llms["gemini"] = gemini
    
    return llms
