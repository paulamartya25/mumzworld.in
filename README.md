# 👶 Mumzworld AI Assistant

A smart parenting companion powered by AI that helps parents discover essential baby products based on their specific needs.

## Features ✨

- **AI-Powered Recommendations** - Uses Llama 3.3 70B via Groq API to provide personalized product suggestions
- **Multilingual Support** - English & Arabic translations
- **Baby Health Advice** - Includes medicine recommendations and product suggestions
- **Beautiful UI** - Pink-themed, animated interface designed for parents
- **Free to Use** - No paid APIs required (uses Groq's free tier)
- **Responsive Design** - Works seamlessly on desktop and tablet

## Tech Stack 🛠️

- **Frontend**: Streamlit (Python web framework)
- **AI Model**: Llama 3.3 70B Versatile (via Groq API)
- **Language**: Python 3.x
- **Styling**: Custom CSS with HTML/Markdown

## Installation 📦

### Prerequisites
- Python 3.8+
- Groq API key (free from https://console.groq.com)

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/mumzworld-ai.git
cd mumzworld-ai
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create a .env file**
```bash
echo "GROQ_API_KEY=your_api_key_here" > .env
```

5. **Run the app**
```bash
streamlit run app.py
```

6. **Open in browser**
Navigate to `http://localhost:8501`

## Usage 🎯

1. **Describe Your Situation** - Tell us about your baby's current stage or any concerns
   - Example: "My 6-month-old is starting to eat solid foods. What equipment do I need?"
   - Example: "My baby has a fever. What should I do?"

2. **Get Recommendations** - Click "Get Product Recommendations 🚀" button

3. **View Results** - See personalized product categories and health advice

4. **Translate** - Check "Also display the response in Arabic" for bilingual output

## Project Structure 📁

```
mumzworld-ai/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # API keys (not in repo)
├── .gitignore            # Git ignore rules
├── DOCUMENTATION.md      # Complete technical documentation
└── README.md             # This file
```

## Key Features Explained 💡

### Smart Recommendations
- Analyzes parent's query using advanced AI
- Provides warm, empathetic responses
- Lists 3-5 targeted product categories
- Includes medicine recommendations for health issues

### Multilingual Support
- Displays recommendations in English first
- Optional Arabic translation with RTL formatting
- Both versions side-by-side

### Beautiful Animations
- Smooth fade-in effects
- Loading spinners with pulsing text
- Slide-in animations for recommendations
- Hover effects on interactive elements

### Pink Baby-Themed Design
- Vibrant pink background (#FFB6D9)
- Black text for maximum readability
- Cute emojis and rotating slogans
- Professional yet playful interface

## API Configuration 🔑

### Getting Groq API Key
1. Visit https://console.groq.com
2. Sign up for a free account
3. Generate API key
4. Add to `.env` file:
```
GROQ_API_KEY=your_key_here
```

The free tier provides generous rate limits - perfect for testing and development!

## Project Requirements Met ✅

| Requirement | Status |
|-------------|--------|
| Estimated Effort: 5 Hours | ✅ |
| Free Tools (No Paid API) | ✅ Groq Free Tier |
| Own Data (No Web Scraping) | ✅ AI-Generated |
| Multilingual (English & Arabic) | ✅ |
| Transparent Documentation | ✅ DOCUMENTATION.md |

## Troubleshooting 🔧

**Issue**: "API Key not found"
- **Solution**: Create `.env` file with `GROQ_API_KEY=your_key`

**Issue**: Page not loading
- **Solution**: Clear browser cache and refresh

**Issue**: Translation not working
- **Solution**: Ensure Arabic checkbox is selected before clicking recommendations

## Future Enhancements 🚀

- [ ] Add more languages (French, Spanish, etc.)
- [ ] Save favorite recommendations
- [ ] Link products directly to Mumzworld catalog
- [ ] Chat history for returning users
- [ ] Baby age-based personalization
- [ ] Video tutorials on product usage

## Security & Privacy 🔐

- API keys stored in `.env` (never committed to repo)
- User queries sent only to Groq API
- No data persistence or tracking
- Stateless conversation model

## License 📝

MIT License - feel free to use and modify

## Support & Contact 💬

For issues, questions, or feature requests:
1. Open an issue on GitHub
2. Check DOCUMENTATION.md for technical details
3. Review Groq API docs: https://console.groq.com

## Credits 👏

- **AI Model**: Meta's Llama 3.3 70B
- **API Provider**: Groq
- **Framework**: Streamlit
- **Design**: Custom CSS/HTML

---

**Made with ❤️ for parents and babies everywhere** 👶💕

*"Every baby deserves the best, and every parent deserves support!"*
