# Personal Blog Search Engine

A custom search engine that surfaces authentic personal blogs and insightful articles, filtering out corporate SEO content.

---

## Table of Contents

1. [Features](#features)
2. [Supported Websites](#supported-websites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Configuration](#configuration)
7. [Troubleshooting](#troubleshooting)
8. [License](#license)
9. [Contributing](#contributing)

---

## Features

* 🔍 **Curated Search Results**: High-quality personal blog content only.
* 🚫 **SEO Filtering**: Excludes corporate and SEO-heavy sites.
* 🌐 **Multi-Platform Support**: Medium, Substack, WordPress, Blogger, GitHub Pages, Dev.to, Hashnode, etc.
* 🎨 **Responsive UI**: Clean, modern design using Flask and Jinja2 templates.
* ⚡ **Fast & Scalable**: Powered by Google Custom Search API.

## Supported Websites

* `medium.com`
* `*.wordpress.com`
* `*.blogspot.com`
* `*.substack.com`
* `*.github.io`
* `dev.to`
* `*.hashnode.dev`
* `waitbutwhy.com`
* `paulgraham.com`
* `manassaloi.com`
* Any other personal blogs matching `.blog` domains

## Installation

### Prerequisites

* Python 3.9+
* Flask
* Google Account (for API access)
* Windows 11 (or any OS with Python support)

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/personal-blog-search.git
   cd personal-blog-search
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate # macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Enable Google Custom Search API**

   * Go to Google Cloud Console
   * Create a new project
   * Enable **Custom Search JSON API**
   * Create **API Key**

5. **Configure Programmable Search Engine**

   * Visit [Programmable Search Engine](https://programmablesearchengine.google.com)
   * Add your desired domains
   * Copy **Search Engine ID**

6. **Create environment file**

   ```ini
   # .env
   GOOGLE_API_KEY=<your_api_key>
   SEARCH_ENGINE_ID=<your_search_engine_id>
   ```

## Usage

1. **Run the application**

   ```bash
   flask run
   ```

2. **Access in browser**

   * Open [http://localhost:5000](http://localhost:5000)

3. **Perform a search**

   * Enter query (e.g., `"how to become a product manager"`)
   * View filtered results from personal blogs

## Project Structure

```bash
personal-blog-search/
├── app.py                # Main Flask application
├── .env                  # Environment variables
├── whitelist.json        # Approved sites regex list
├── requirements.txt      # Python dependencies
└── templates/            # Jinja2 HTML templates
    ├── index.html        # Homepage
    ├── results.html      # Display search results
    └── error.html        # Error page
```

## Configuration

To add more websites to the whitelist, update **whitelist.json**:

```json
{
  "sites": [
    "newwebsite\\.com",
    ".*\\.personal\\.blog"
  ]
}
```

* Also update your Programmable Search Engine settings to include new domains.

## Troubleshooting

* **Issue**: Only getting results from one site (e.g., Medium)

  * Verify domains are added in Programmable Search Engine.
  * Check patterns in `whitelist.json`.

* **Issue**: `Template not found` error

  * Ensure `templates/` directory contains all `.html` files.
  * Verify file permissions.

* **Issue**: API quota exceeded

  * Free tier: 100 requests/day.
  * Upgrade quota in Google Cloud Console.

* **Issue**: `JSONDecodeError` on startup

  * Validate `whitelist.json` syntax.
  * Delete and re-create file if corrupted.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to:

* Add new high-quality blog sources
* Improve search/filter algorithm
* Enhance UI/UX

