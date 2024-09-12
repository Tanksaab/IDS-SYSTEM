import pandas as pd

def extract_features(packet):
    features = {
        'src_ip': packet[IP].src,
        'dst_ip': packet[IP].dst,
        'src_port': packet[TCP].sport,
        'dst_port': packet[TCP].dport,
        'protocol': packet.protocol,
        'packet_length': len(packet),
        'time_interval': packet.time - packet.prev_packet.time
    }
    return features

def process_packets(packets):
    features_list = []
    for packet in packets:
        features = extract_features(packet)
        features_list.append(features)
    return pd.DataFrame(features_list)