# Text Translator

A Python application that translates text from English to French using LangChain and Google Gemini AI.

## Features

- Interactive text translation from English to French
- Powered by Google Gemini 1.5 Flash model
- Environment variable support for API key management
- Simple command-line interface

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key

### Getting a Google Gemini API Key

1. Visit the [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the API key for use in this application

## Installation

1. **Clone or download this project**
   ```bash
   # If using git
   git clone <repository-url>
   cd <repository-root-dir>
   ```

2. **Create a Python virtual environment**
   ```bash
   # On macOS/Linux
   python3 -m venv .venv
   
   # On Windows
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   ```bash
   # On macOS/Linux
   source .venv/bin/activate
   
   # On Windows
   .venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r text-translator/requirements.txt
   ```

## Configuration

### Option 1: Environment File (Recommended)

1. Copy the example environment file:
   ```bash
   cp env.example .env
   ```

2. Edit the `.env` file and replace `your_api_key_here` with your actual Google Gemini API key:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

### Option 2: Interactive Prompt

If you don't set up the `.env` file, the application will prompt you to enter your API key when you run it.

## Usage

1. **Ensure your virtual environment is activated**
   ```bash
   source .venv/bin/activate  # macOS/Linux
   # or
   .venv\Scripts\activate     # Windows
   ```

2. **Run the text translator**
   ```bash
   python text-translator/text-translator.py
   ```

3. **Enter text to translate**
   - Type any English text and press Enter
   - The application will translate it to French
   - Type `exit` to quit the application

### Example Session

```
Enter the text to translate (or 'exit' to quit): Hello, how are you?
Bonjour, comment allez-vous ?

Enter the text to translate (or 'exit' to quit): The weather is beautiful today.
Le temps est magnifique aujourd'hui.

Enter the text to translate (or 'exit' to quit): exit
```

## Project Structure

```
explore-langchain
├── env.example               # Example environment variables
├── .env                      # Environment variables (create from env.example)
├── .gitignore                # Ignore list for Git source control
└── text-translator/
    ├── README.md             # This file
    ├── requirements.txt      # Python dependencies
    └── text-translator.py    # Main application
```

## Dependencies

- `python-dotenv` - Environment variable management
- `langchain` - Core LangChain functionality
- `langchain-core` - Core LangChain components
- `langchain-community` - Community integrations
- `langchain-google-genai` - Google Gemini integration

## Troubleshooting

### Common Issues

1. **Import Error for dotenv**
   - Make sure you've installed the requirements: `pip install -r text-translator/requirements.txt`

2. **API Key Issues**
   - Verify your Google Gemini API key is correct
   - Ensure the API key has the necessary permissions
   - Check that the `.env` file is in the correct location

3. **Model Loading Errors**
   - Ensure you have a stable internet connection
   - Verify your API key has access to the Gemini 1.5 Flash model

### Getting Help

If you encounter issues:
1. Check that all dependencies are installed correctly
2. Verify your API key is valid and has proper permissions
3. Ensure you're using Python 3.8 or higher

## License

This project is open source and available under the MIT License. 