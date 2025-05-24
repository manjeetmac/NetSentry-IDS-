BLACKLIST_IPS = ["123.45.67.89"]
from scapy.layers.inet import IP

def detect_signature(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        if src_ip in BLACKLIST_IPS:
            return True
    return False
