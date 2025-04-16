# utils/shared_ui.py
import streamlit as st
import pandas as pd
import io

# Import LLM classes - needed for initialize_llm type hints or potential instance checks
# Adjust imports based on your actual file structure if needed
try:
    from models.access.claude import ClaudeLLM
    from models.access.openai import OpenAILLM
    from models.access.gemini import GeminiLLM
except ImportError:
    # Handle cases where running a page directly might mess up relative imports
    st.warning("Could not import LLM classes directly in shared_ui. Might affect initialization if run stand-alone.")
    ClaudeLLM, OpenAILLM, GeminiLLM = None, None, None # Set to None to avoid NameError later


def ensure_session_state():
    """Initializes required session state variables if they don't exist."""
    defaults = {
        "api_keys": {"claude": "", "openai": "", "gemini": ""},
        "current_model_name": "Claude", # Store model name selection
        "current_language": "sotho",
        "current_model": None, # Stores the initialized LLM instance
        "generated_lexicon": pd.DataFrame(columns=["word", "sentiment", "intensity"]),
        "sentiment_analysis_results": pd.DataFrame(),
        "sentiment_input_text": "",
        "single_analysis_result": None,
        "selected_explanation_item": None,
    }
    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value

def display_sidebar():
    """Displays sidebar configuration and returns selected model name and language.
       The appearance is controlled by the global theme set via st.set_page_config."""
    st.sidebar.header("Model Configuration")
    available_models = ["Claude", "OpenAI", "Gemini"]
    # Get current index, default to 0 if state is somehow invalid
    try:
        current_model_index = available_models.index(st.session_state.get("current_model_name", "Claude"))
    except ValueError:
        current_model_index = 0

    model_choice = st.sidebar.selectbox(
        "Select LLM Model",
        available_models,
        index=current_model_index,
        key="model_selector_sidebar" # Add key for potential callbacks later
    )
    st.session_state.current_model_name = model_choice # Update session state

    available_languages = ["sotho", "sepedi", "setswana"]
    try:
        current_language_index = available_languages.index(st.session_state.get("current_language", "sotho"))
    except ValueError:
        current_language_index = 0

    language_choice = st.sidebar.selectbox(
        "Select Language",
        available_languages,
        index=current_language_index,
        key="language_selector_sidebar"
    )
    st.session_state.current_language = language_choice # Update session state

    # Ensure API keys state exists
    if 'api_keys' not in st.session_state:
        st.session_state.api_keys = {"claude": "", "openai": "", "gemini": ""}
    
    # Only show the relevant API key input based on the selected model
    st.sidebar.header("API Key")
    if model_choice == "Claude":
        st.session_state.api_keys["claude"] = st.sidebar.text_input(
            "Claude API Key", type="password", value=st.session_state.api_keys["claude"]
        )
    elif model_choice == "OpenAI":
        st.session_state.api_keys["openai"] = st.sidebar.text_input(
            "OpenAI API Key", type="password", value=st.session_state.api_keys["openai"]
        )
    elif model_choice == "Gemini":
        st.session_state.api_keys["gemini"] = st.sidebar.text_input(
            "Gemini API Key", type="password", value=st.session_state.api_keys["gemini"]
        )

    return model_choice, language_choice


def initialize_llm(model_choice, api_keys):
    """
    Initializes the selected LLM if necessary and returns the instance.
    Reads API keys from the provided dictionary (or session state).
    Updates st.session_state.current_model.
    """
    llm_instance = None
    api_key = None
    error_message = None

    try:
        if model_choice == "Claude":
            api_key = api_keys.get("claude", "")
            if not api_key: error_message = "Claude API key is missing."
            elif ClaudeLLM: llm_instance = ClaudeLLM(api_key=api_key)
        elif model_choice == "OpenAI":
            api_key = api_keys.get("openai", "")
            if not api_key: error_message = "OpenAI API key is missing."
            elif OpenAILLM: llm_instance = OpenAILLM(api_key=api_key) # Pass other params if needed
        elif model_choice == "Gemini":
            api_key = api_keys.get("gemini", "")
            if not api_key: error_message = "Gemini API key is missing."
            elif GeminiLLM: llm_instance = GeminiLLM(api_key=api_key) # Pass other params if needed
        else:
            error_message = f"Model {model_choice} not implemented yet."

        if error_message:
            # Display errors/warnings in the sidebar, they will also adapt to the theme
            st.sidebar.warning(error_message) # Use warning or error as appropriate
            st.session_state.current_model = None
            return None
        else:
            # Check if model actually changed before potentially showing spinner/message
            current_model_instance = st.session_state.get('current_model')
            # Check if model is None OR if the name attribute exists and is different
            model_changed = (current_model_instance is None or
                            (hasattr(current_model_instance, 'name') and current_model_instance.name != model_choice) or
                            # Add checks for other ways model identity might be stored if 'name' isn't reliable
                            type(current_model_instance).__name__.replace("LLM","") != model_choice
                            )

            if model_changed:
                 # Optional: Add spinner if initialization is slow
                 # with st.spinner(f"Initializing {model_choice}..."):
                 #     pass # Initialization happens above
                 st.session_state.current_model = llm_instance
                 if llm_instance:
                     st.sidebar.success(f"{model_choice} model ready.") # Feedback
            # Return the potentially existing or newly initialized model
            return st.session_state.current_model # Return current state regardless of change

    except Exception as e:
        st.sidebar.error(f"Error initializing {model_choice}: {e}")
        st.session_state.current_model = None
        return None

def export_dataframe(df, fmt):
    """Export dataframe to specified format and create a download link"""
    # This function remains the same as before
    try:
        df_export = df.copy()
        # df_export['rating'] = df_export['rating'].fillna('') # Example fillna

        if fmt == "CSV":
            # Use utf-8-sig for better Excel compatibility with non-ASCII chars
            return df_export.to_csv(index=False, encoding='utf-8-sig')
        elif fmt == "Excel":
            output = io.BytesIO()
            # Use xlsxwriter engine for more control if needed later
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df_export.to_excel(writer, index=False, sheet_name='Sheet1')
            # No need to explicitly close writer with 'with' statement
            return output.getvalue()
        elif fmt == "JSON":
            # Ensure non-ASCII characters are preserved
            return df_export.to_json(orient="records", indent=4, force_ascii=False)
    except Exception as e:
        st.error(f"Error exporting data to {fmt}: {e}")
        return None
