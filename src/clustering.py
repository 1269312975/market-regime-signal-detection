# Clustering methods for regime detection
from sklearn.cluster import KMeans

def apply_kmeans(data, n_clusters=3):
    model = KMeans(n_clusters=n_clusters)
    labels = model.fit_predict(data)
    return labels