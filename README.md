# Explore LangChain

A collection of projects exploring LangChain capabilities and integrations.

## Projects

### [Text Translator](./text-translator/)

A Python application that translates text from English to French using LangChain and Google Gemini AI.

**Features:**
- Interactive text translation from English to French
- Powered by Google Gemini 1.5 Flash model
- Environment variable support for API key management
- Simple command-line interface

**Quick Start:**
```bash
cd text-translator
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp env.example .env
# Edit .env with your Google Gemini API key
python text-translator.py
```

## Getting Started

Each subproject contains its own documentation and setup instructions. Navigate to the specific project directory for detailed information.

## Prerequisites

- Python 3.8 or higher
- Git

## Project Structure

```
explore-langchain/
├── README.md              # This file
├── .gitignore            # Git ignore rules
├── text-translator/       # Text translation project
│   ├── README.md         # Project-specific documentation
│   ├── requirements.txt  # Python dependencies
│   ├── text-translator.py # Main application
│   └── env.example      # Environment variables template
└── .venv/               # Virtual environment (if created)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License. 