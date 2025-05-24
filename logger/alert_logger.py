import logging

logging.basicConfig(filename='alerts.log', level=logging.WARNING)

def log_alert(summary):
    print("[ALERT]", summary)
    logging.warning(summary)
