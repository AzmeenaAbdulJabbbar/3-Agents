# 3-Agents Project

This repository contains three different AI agent applications:

1. **Career Advisor** - AI-powered career guidance and job recommendations
2. **Game Changer** - Interactive storytelling and game development
3. **Traveler Designer** - AI travel planning and booking assistance

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Environment Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AzmeenaAbdulJabbbar/3-Agents.git
   cd 3-Agents
   ```

2. **Set up environment variables:**
   
   For each project directory, create a `.env` file with your OpenAI API key:
   
   ```bash
   # career_advisor/.env
   OPENAI_API_KEY=your_openai_api_key_here
   
   # game_changer/.env
   OPENAI_API_KEY=your_openai_api_key_here
   
   # tavler-designer/.env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

   **Important:** Never commit your `.env` files to version control. They are already included in `.gitignore`.

3. **Install dependencies for each project:**
   
   ```bash
   # Career Advisor
   cd career_advisor
   pip install -e .
   
   # Game Changer
   cd ../game_changer
   pip install -r requirements.txt
   
   # Traveler Designer
   cd ../tavler-designer
   pip install -r requirements.txt
   ```

## Running the Applications

### Career Advisor
```bash
cd career_advisor
chainlit run main.py
```

### Game Changer
```bash
cd game_changer
python main.py
```

### Traveler Designer
```bash
cd tavler-designer
chainlit run main.py
```

## Security Notes

- **Never commit API keys or sensitive credentials to version control**
- The `.env` files are automatically ignored by git
- Use environment variables for all sensitive configuration
- Regularly rotate your API keys

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure no sensitive data is committed
5. Submit a pull request

## License

This project is licensed under the MIT License. 