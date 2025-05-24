import unittest
from scapy.layers.inet import IP
from scapy.packet import Packet
from detection.signatures import detect_signature

class DummyPacket(Packet):
    def __init__(self, src_ip):
        self[IP] = IP(src=src_ip)

class TestSignatureDetection(unittest.TestCase):
    def test_blacklisted_ip(self):
        pkt = DummyPacket("123.45.67.89")
        self.assertTrue(detect_signature(pkt))

    def test_safe_ip(self):
        pkt = DummyPacket("8.8.8.8")
        self.assertFalse(detect_signature(pkt))

if __name__ == '__main__':
    unittest.main()
