# app.py
import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import requests
import json
import re
# from flask_cors import CORS
# CORS(app)

load_dotenv()

app = Flask(__name__)

# Load blog whitelist from JSON file with error handling
try:
    with open('whitelist.json', 'r') as f:
        BLOG_WHITELIST = json.load(f)['sites']
except FileNotFoundError:
    print("Error: whitelist.json file not found. Using default list.")
    BLOG_WHITELIST = [
        "medium\\.com",
        "wordpress\\.com",
        "blogspot\\.com",
        "tumblr\\.com",
        "substack\\.com",
        "github\\.io",
        "dev\\.to",
        "hashnode\\.dev",
        "\\.blog",
        "personal\\.blog",
        "waitbutwhy\\.com",
        "manassaloi\\.com"
    ]
except json.JSONDecodeError:
    print("Error: whitelist.json is not valid JSON. Using default list.")
    BLOG_WHITELIST = [
        "medium\\.com",
        "wordpress\\.com",
        "blogspot\\.com",
        "tumblr\\.com",
        "substack\\.com",
        "github\\.io",
        "dev\\.to",
        "hashnode\\.dev",
        "\\.blog",
        "personal\\.blog",
        "waitbutwhy\\.com",
        "manassaloi\\.com"
    ]

def is_personal_blog(url):
    """Check if URL matches any whitelisted personal blog patterns"""
    for pattern in BLOG_WHITELIST:
        if re.search(pattern, url, re.IGNORECASE):
            return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
@app.route('/search', methods=['GET'])
def search():
    try:
        query = request.args.get('q', '').strip()
        if not query:
            return render_template('error.html', message="Please enter a search query"), 400
        
        if not os.getenv('GOOGLE_API_KEY') or not os.getenv('SEARCH_ENGINE_ID'):
            return render_template('error.html', message="Search service not configured properly"), 500

        api_key = os.getenv('GOOGLE_API_KEY')
        cx = os.getenv('SEARCH_ENGINE_ID')
        url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
        
        response = requests.get(url)
        response.raise_for_status()  # Raises exception for 4XX/5XX responses
        results = response.json()
        
        filtered_results = []
        if 'items' in results:
            for item in results['items']:
                if is_personal_blog(item['link']):
                    filtered_results.append({
                        'title': item.get('title', 'No title'),
                        'link': item.get('link', '#'),
                        'snippet': item.get('snippet', ''),
                        'source': re.search(r'https?://([^/]+)', item.get('link', '')).group(1)
                    })
        
        return render_template('results.html', 
                            query=query, 
                            results=filtered_results, 
                            result_count=len(filtered_results))
    
    except requests.exceptions.RequestException as e:
        return render_template('error.html', message=f"Search API error: {str(e)}"), 500
    except Exception as e:
        return render_template('error.html', message=f"An unexpected error occurred: {str(e)}"), 500
if __name__ == '__main__':
    app.run(debug=True)