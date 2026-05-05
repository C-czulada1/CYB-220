from scapy.all import sniff, IP, TCP
import time
from collections import defaultdict
import logging

PORT_SCAN_THRESHOLD = 8
TIME_WINDOW = 10  
SENSITIVE_PORTS = [22, 23, 3389]
LOG_FILE = "ids_log.txt"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)
ip_activity = defaultdict(list)
def alert(message):
    print(f"[ALERT] {message}")
    logging.warning(message)
def detect_port_scan(ip):
    current_time = time.time()
    ip_activity[ip] = [
        t for t in ip_activity[ip]
        if current_time - t < TIME_WINDOW
    ]
    if len(ip_activity[ip]) > PORT_SCAN_THRESHOLD:
        alert(f"Possible port scan from {ip}")

def process_packet(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_activity[ip_src].append(time.time())
        detect_port_scan(ip_src)
        if packet.haslayer(TCP):
            port = packet[TCP].dport
            if port in SENSITIVE_PORTS:
                alert(f"Access to sensitive port {port} from {ip_src}")
def main():
    print("[*] Simple IDS running... Logging to file.")
    sniff(prn=process_packet, store=0)

if __name__ == "__main__":
    main()
logging.warning("TEST LOG ENTRY")
