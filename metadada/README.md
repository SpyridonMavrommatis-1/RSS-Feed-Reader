# RSS Feed Reader

## Description

- **RSS Feed Reader Spimav v.0.1**  
- A Python program that allows monitoring new updates from various sites.  
- The monitored sites are categorized into two groups: _European Union_ and _Literary Magazines_.  
- It analyzes and categorizes the feeds and saves the results in a CSV file.  

---

## Project Files

- `main.py`: The main workflow of the program. It manages the retrieval and analysis of the feeds.
- `feed_manager.py`: Contains functions for managing the feeds and categorizing them.
- `feeds.json`: Input file containing the RSS feeds information.
- `updates.csv`: Output file containing the analysis results.

---

## Installation and Usage

1. **Download the project:**

   ```bash
   git clone https://github.com/SpyridonMavrommatis-1/RSS-Feed-Reader.git
   cd RSS-Feed-Reader
   ```

2. **Create and Activate the Virtual Environment (if not already created):**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate   # MacOS/Linux
   ```

3. **Install the required libraries:**

   ```bash
   pip install feedparser
   ```

4. **Run the program using the .bat file:**

- In the project folder, locate the `run_rss_reader.bat` file.
- Double-click to launch the program.

---

## How It Works

- **Step Configuration:** Organizes the program's flow and calls the necessary functions.
- **Management:** Analyzes and categorizes the RSS feeds.
- **Data Analysis:** Extracts articles and information from the feeds.
- **Information Input (JSON):** Loads RSS feeds from `feeds.json`.
- **Extraction of Useful Information:** Saves results in `updates.csv`.

---

## Examples and Screenshots

- **Sample Input (`feeds.json`):**
  ```json
  [
    { "name": "Vakxikon", "url": "https://www.vakxikon.gr/feed/" },
    {
      "name": "Diastixo",
      "url": "https://diastixo.gr/index.php?option=com_jmap&view=sitemap&format=rss"
    }
  ]
  ```
- **Sample Output (`updates.csv`):**
  ```
  Category, Feed Name, Title, Link, Published Date
  Literary Magazines, Vakxikon, Poem of the Week, https://example.com, 2025-02-28
  ```

---

## Notes and Troubleshooting

- **Issue with `updates.csv`:**
  - If the program displays an error `PermissionError: [Errno 13] Permission denied: 'updates.csv'`,
    ensure that the file is not open in another program like Excel or VSCode.
  - If it is open, close it and try again. If the issue persists, close VSCode and rerun the program.

---

## Future Improvements

- Ability to add more categories.
- Automatic refresh of feeds.
- Future GUI implementation for category selection and real-time feed updates.

---

## Author

- **Name** Spyridon Mavrommatis
- **LinkedIn:** https://www.linkedin.com/in/spiridonmavrommatis/
- **GitHub:** https://github.com/SpyridonMavrommatis-1

