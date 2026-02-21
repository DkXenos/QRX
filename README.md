# QRX — CLI QR Code Generator 🔳

A simple command-line tool that generates a QR code from any URL and saves it as a `.jpg` on your Desktop.

---

## Requirements
- Python 3.12
- Homebrew (Mac) — [https://brew.sh](https://brew.sh)

---

## Installation & Setup

### Step 1 — Install Python 3.12 via Homebrew
```bash
brew install python@3.12
```

### Step 2 — Clone or Download this project
```bash
git clone https://github.com/yourusername/QRX.git
cd QRX
```

### Step 3 — Create and activate the virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 4 — Install dependencies
```bash
pip install -r requirements.txt
```

---

## Running the Program

### Option A — Run manually (inside the project folder)
```bash
source .venv/bin/activate
python main.py
```

### Option B — Set up a global shortcut (recommended) ⚡
This lets you type `qrx` anywhere in your terminal to instantly generate a QR code.

**1. Open your `.zshrc`:**
```bash
nano ~/.zshrc
```

**2. Add this line at the bottom** *(replace `/path/to/QRX` with your actual project path)*:
```bash
alias qrx="/path/to/QRX/.venv/bin/python /path/to/QRX/main.py"
```

**Example:**
```bash
alias qrx="/Users/yourusername/Documents/PYTHON/Programs/QRX/.venv/bin/python /Users/yourusername/Documents/PYTHON/Programs/QRX/main.py"
```

**3. Save and reload:**

Press `CTRL + X`, then `Y`, then `ENTER` to save. Then run:
```bash
source ~/.zshrc
```

**4. Now just type anywhere in your terminal:**
```bash
qrx
```

---

## Usage
```
=== CLI QR Code Generator ===

Enter the URL or link to encode: https://github.com
Enter the output filename (without extension): github_qr

✅ QR code saved successfully!
   Path: /Users/yourusername/Desktop/github_qr.jpg
```

---

## Notes
- The QR code is saved as a `.jpg` on your **Desktop** automatically
- Works completely **offline** — no internet needed to generate QR codes
- The URL inside the QR code still requires internet to visit

---

## Dependencies
| Package | Purpose |
|---------|---------|
| `qrcode[pil]` | QR code generation |
| `Pillow` | Image rendering & saving |

---

## Project Structure
```
QRX/
├── .venv/              # Virtual environment (not committed to git)
├── main.py             # Main script
├── requirements.txt    # Project dependencies
└── README.md           # This file
```

---

## License
MIT License — feel free to use and modify!