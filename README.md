# NetSentry: Real-Time Network Threat Detection

NetSentry is a lightweight intrusion detection system written in Python.
It uses packet sniffing, signature-based and anomaly-based detection to alert on potential threats.

## Features
- Real-time packet analysis using `scapy`
- Signature-based detection of blacklisted IPs
- Basic anomaly detection (packet flood detection)
- Logs alerts to file and prints them in terminal

## Usage
```bash
pip install -r requirements.txt
sudo python netsentry.py
```

## Folder Structure
- `detection/`: Detection logic
- `logger/`: Logging alerts
- `utils/`: Packet utility functions
- `config/`: Configuration files
- `tests/`: Unit tests

## Future Improvements
- Integration with VirusTotal or AbuseIPDB
- Slack/email alerting
- Web interface with Flask

---
This project is ideal for showcasing your cybersecurity skills and Python programming proficiency.
