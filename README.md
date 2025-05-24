
# NetSentry

NetSentry is a lightweight network monitoring tool designed to detect suspicious network activity through **signature-based** and **anomaly-based** detection mechanisms. It leverages packet sniffing using `scapy`, maintains blacklists for signature detection, and logs alerts to file and console.

---

## 🛡 Features

- 📡 Real-time packet sniffing
- 🔍 Signature-based detection using IP blacklists
- 📈 Anomaly detection based on traffic frequency
- ⚠️ Alert logging (console and file)
- 🧪 Unit tests for signature detection
- 🔧 Configurable settings via `settings.json`

---

## 🗂 Project Structure

```

netsentry/
├── netsentry.py                  # Main packet sniffer
├── config/
│   └── settings.json             # Configurable detection settings
├── detection/
│   ├── anomaly\_detector.py       # Anomaly detection logic
│   └── signatures.py             # Signature detection logic
├── logger/
│   └── alert\_logger.py           # Logging functionality
├── utils/
│   └── packet\_utils.py           # Packet summarizer
├── tests/
│   └── test\_signatures.py        # Unit tests for signature detection
└── requirements.txt              # Python dependencies

````

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/netsentry.git
cd netsentry
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run NetSentry

```bash
sudo python netsentry.py
```

> ℹ️ `sudo` may be required for raw packet sniffing privileges.

---

## ⚙️ Configuration

Edit the `config/settings.json` file to customize:

* **Blacklisted IPs**
* **Packet threshold**
* **Detection interval**

Example:

```json
{
  "blacklist_ips": ["123.45.67.89"],
  "packet_threshold": 10,
  "interval_seconds": 2
}
```

---

## 🧪 Running Tests

Run unit tests using:

```bash
python -m unittest tests/test_signatures.py
```

---

## 📋 Dependencies

* `scapy`: Packet sniffing and parsing
* `pandas`, `matplotlib`, `requests`: Reserved for future enhancements (currently unused)

Install all using:

```bash
pip install -r requirements.txt
```

---

## 📝 developed by Manjeet 🦦
