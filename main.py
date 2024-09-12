import packet_capture
import feature_extraction
import anomaly_detection
import alert_system

def main():
    packets = packet_capture.capture_packets()
    features = feature_extraction.process_packets(packets)
    model = anomaly_detection.train_model(features)
    anomalies = anomaly_detection.detect_anomalies(features, model)
    alert_system.flag_suspicious_activities(anomalies)

if __name__ == '__main__':
    main()