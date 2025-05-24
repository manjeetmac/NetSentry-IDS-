from detection.signatures import detect_signature
from detection.anomaly_detector import detect_anomaly
from logger.alert_logger import log_alert
from utils.packet_utils import packet_summary
from scapy.all import sniff

def packet_callback(packet):
    summary = packet_summary(packet)
    if detect_signature(packet) or detect_anomaly(packet):
        log_alert(summary)

if __name__ == "__main__":
    sniff(prn=packet_callback, store=False)
