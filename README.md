# XML / HTML / JSON CLI Tool

A simple Python CLI tool for working with XML, HTML, and JSON files.  
This tool provides three main commands:

- **format-xml** → Reads and formats an XML file.  
- **html-to-json** → Extracts data from an HTML file by tag and saves it as JSON.  
- **json-to-xml** → Converts a JSON file into a simple XML structure.  

---

## 📦 Installation

Clone the repository and install requirements (if any):

```bash
git clone https://github.com/your-username/xml-html-json-cli.git
cd xml-html-json-cli
```

No external dependencies are strictly required (only built-in Python libraries are used).  
If you plan to extend functionality with `BeautifulSoup4`, install it:

```bash
pip install beautifulsoup4
```

---

## 🚀 Usage

Run the script with **Python 3.7+**:

```bash
python main.py <command> [arguments]
```

### Commands

#### 1. Format XML

Reads and formats an XML file.

```bash
python main.py format-xml path/to/file.xml
```

#### 2. HTML → JSON

Converts an HTML file to JSON by extracting a specific tag.

```bash
python main.py html-to-json path/to/file.html div
```

The output will be saved as `file.json` in the same directory.

#### 3. JSON → XML

Converts a JSON file into XML.

```bash
python main.py json-to-xml path/to/file.json
```

The output will be saved as `file.xml` in the same directory.

---

## 📂 Example

```bash
# Format an XML file
python main.py format-xml sample.xml

# Convert HTML to JSON
python main.py html-to-json page.html h1

# Convert JSON back to XML
python main.py json-to-xml data.json
```

---

## 🛠 Project Structure

```
.
├── main.py        # CLI script
├── README.txt     # Documentation
└── examples/      # Example files (optional)
```

---

## 📜 License

This project is licensed under the MIT License.
