# Web Scraping and Django Dashboard Project

A Python-based web scraping project that extracts quotes from [quotes.toscrape.com](https://quotes.toscrape.com/) and displays them in a Django web dashboard.

## image
<img width="1920" height="1080" alt="Dashboard " src="https://github.com/user-attachments/assets/e5c4e939-4d19-411c-be30-0c89cc25c222" />

## Project Structure
```
Webscrapy/
├── manage.py
├── scraper.py              # Web scraping script
├── quotes.csv              # Scraped data in CSV format
├── quotes.db               # SQLite database with scraped data
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── quotesproject/         # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── quotesapp/             # Django application
    ├── models.py
    ├── views.py
    ├── templates/
    └── ...
```

## Features

- ✅ Scrapes quotes from minimum 10 pages with pagination
- ✅ Extracts quote text, author name, tags, and author profile URL
- ✅ Saves data to CSV file
- ✅ Stores data in SQLite database with duplicate prevention
- ✅ Django web application displays all scraped quotes
- ✅ Clean and responsive UI

## Requirements

- Python 3.8 or higher
- pip (Python package manager)

## Installation & Setup

### 1. Clone or Download the Project
```bash
cd path/to/Webscrapy
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage

### Running the Web Scraper

To scrape quotes and save to CSV and database:
```bash
python scraper.py
```

**Output:**
- `quotes.csv` - CSV file with all scraped quotes
- `quotes.db` - SQLite database with all scraped quotes

**Note:** Running the scraper multiple times will skip duplicate quotes automatically.

### Running the Django Web Application

1. **Start the Django development server:**
```bash
python manage.py runserver
```

2. **Open your browser and visit:**
```
http://127.0.0.1:8000/
```

3. **You should see a dashboard displaying all scraped quotes with:**
   - Quote text
   - Author name
   - Associated tags
   - Link to author profile

## Project Components

### 1. Web Scraper (`scraper.py`)

- Uses `requests` and `BeautifulSoup` for web scraping
- Implements pagination to scrape multiple pages
- Saves data to both CSV and SQLite database
- Prevents duplicate entries using UNIQUE constraint

### 2. Database Schema

**Table: quotes**

| Column          | Type    | Description                    |
|-----------------|---------|--------------------------------|
| id              | INTEGER | Primary key (auto-increment)   |
| quote           | TEXT    | Quote text (unique)            |
| author          | TEXT    | Author name                    |
| tags            | TEXT    | Comma-separated tags           |
| author_profile  | TEXT    | Author profile URL path        |

### 3. Django Application

- **Model:** Defines Quote model matching database schema
- **View:** Retrieves quotes from database and prepares data
- **Template:** Responsive HTML page with styled table display

## Technologies Used

- **Python 3.12**
- **Beautiful Soup 4** - HTML parsing
- **Requests** - HTTP requests
- **Django 6.0.1** - Web framework
- **SQLite3** - Database

## Troubleshooting

### Issue: "Module not found" error

**Solution:** Make sure virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: Django shows "no such table: quotes"

**Solution:** Run the scraper first to create the database:
```bash
python scraper.py
```

### Issue: No quotes showing in web application

**Solution:** 
1. Verify `quotes.db` exists in the project root
2. Check database has data:
```bash
python -c "import sqlite3; conn = sqlite3.connect('quotes.db'); cursor = conn.cursor(); cursor.execute('SELECT COUNT(*) FROM quotes'); print(f'Quotes: {cursor.fetchone()[0]}'); conn.close()"
```

## Development Notes

- Database uses `managed = False` in Django model to preserve existing schema
- CSV and database files are in project root for easy access
- Scraper uses absolute paths to ensure files save in correct location

## Author

Om Bhosle

## Date

January 9, 2026
