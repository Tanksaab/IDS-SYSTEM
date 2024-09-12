from scapy.all import sniff
import scapy.all as scapy
scapy.conf.use_pcap = True
def packet_handler(packet):
    print(packet.summary())

sniff(prn=packet_handler, store=0)  # Capture packets and process each packet using the packet_handler function