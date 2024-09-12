from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def train_model(features):
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    kmeans = KMeans(n_clusters=3)  # Adjust the number of clusters as needed
    kmeans.fit(scaled_features)
    return kmeans

def detect_anomalies(features, model):
    scaled_features = scaler.transform(features)
    predictions = model.predict(scaled_features)
    anomalies = [i for i, pred in enumerate(predictions) if pred == -1]
    return anomalies