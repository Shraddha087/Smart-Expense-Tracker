# Smart Expense Tracker with AI Insights

A Flask-based web application for tracking expenses with AI-generated insights.

## Features
- 💰 Add and track expenses by category
- 📊 View category-wise spending summary
- 🧠 AI-powered spending insights and recommendations
- 💾 Data persisted in CSV format

## Tech Stack
- **Backend**: Flask (Python)
- **Data**: Pandas, CSV
- **Frontend**: HTML, CSS
- **Database**: CSV file

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup
1. Clone the repository
```bash
git clone https://github.com/yourusername/Smart-Expense-Tracker.git
cd Smart-Expense-Tracker
```

2. Install dependencies
```bash
pip install flask pandas
```

3. Run the application
```bash
python app.py
```

4. Open your browser and go to `http://127.0.0.1:5000`

## Project Structure
```
Smart-Expense-Tracker/
├── app.py                 # Main Flask application
├── expenses.csv          # Expense data storage
├── templates/
│   └── index.html        # HTML template
├── static/
│   └── style.css         # Stylesheet
├── .gitignore
└── README.md
```

## How to Use
1. **Add Expense**: Fill in category, amount, and description
2. **View Summary**: See total expenses and category breakdown
3. **Get Insights**: AI analyzes your spending patterns

## License
MIT License

## Author
Your Name
