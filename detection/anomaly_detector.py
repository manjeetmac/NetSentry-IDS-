import time
from collections import deque

timestamps = deque(maxlen=100)

def detect_anomaly(packet):
    current_time = time.time()
    timestamps.append(current_time)
    if len(timestamps) > 10:
        interval = timestamps[-1] - timestamps[0]
        if interval < 2:  # Too many packets in a short time
            return True
    return False
