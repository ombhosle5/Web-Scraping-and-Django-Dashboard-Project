import requests
from bs4 import BeautifulSoup
import csv
import sqlite3
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, 'quotes.csv')
DB_FILE = os.path.join(BASE_DIR, 'quotes.db')


def setup_database():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS quotes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  quote TEXT UNIQUE,
                  author TEXT,
                  tags TEXT,
                  author_profile TEXT)''')
    conn.commit()
    return conn


def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    quotes_data = []
    quote_divs = soup.find_all('div', class_='quote')
    
    for quote_div in quote_divs:
        
        quote_text = quote_div.find('span', class_='text').text.strip()
        
        
        author = quote_div.find('small', class_='author').text.strip()
        
        
        tags = [tag.text for tag in quote_div.find_all('a', class_='tag')]
        tags_str = ', '.join(tags)
        
        
        author_link = quote_div.find('a')['href']
        
        quotes_data.append({
            'quote': quote_text,
            'author': author,
            'tags': tags_str,
            'author_profile': author_link 
        })
    
    
    next_btn = soup.find('li', class_='next')
    next_page = None
    if next_btn:
        next_page = next_btn.find('a')['href']
        next_page = f"https://quotes.toscrape.com{next_page}"
    
    return quotes_data, next_page


def scrape_quotes(num_pages=10):
    all_quotes = []
    url = "https://quotes.toscrape.com/page/1/"
    
    for i in range(num_pages):
        print(f"Scraping page {i+1}...")
        quotes, next_url = scrape_page(url)
        all_quotes.extend(quotes)
        
        if not next_url:
            print(f"No more pages. Scraped {i+1} pages total.")
            break
        
        url = next_url
    
    return all_quotes


def save_to_csv(quotes, filename=CSV_FILE):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['quote', 'author', 'tags', 'author_profile'])
        writer.writeheader()
        writer.writerows(quotes)
    print(f"Saved {len(quotes)} quotes to {filename}")


def save_to_database(quotes, conn):
    c = conn.cursor()
    saved = 0
    duplicates = 0
    
    for q in quotes:
        try:
            c.execute('''INSERT INTO quotes (quote, author, tags, author_profile)
                        VALUES (?, ?, ?, ?)''',
                     (q['quote'], q['author'], q['tags'], q['author_profile']))
            saved += 1
        except sqlite3.IntegrityError:
            duplicates += 1
    
    conn.commit()
    print(f"Saved {saved} quotes to database ({duplicates} skipped as duplicates)")


if __name__ == "__main__":
    print(f"Working directory: {BASE_DIR}")
    print(f"CSV file: {CSV_FILE}")
    print(f"Database file: {DB_FILE}")
    print("-" * 50)
    
   
    conn = setup_database()
    
    quotes = scrape_quotes(num_pages=10)
    
    save_to_csv(quotes)
    
    save_to_database(quotes, conn)
    
    conn.close()
    
    print("-" * 50)
    print(f"Total quotes scraped: {len(quotes)}")
    print("Done!")