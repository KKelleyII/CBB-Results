import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load your dataset
# Assuming your dataset is in a CSV format
df = pd.read_csv('/Users/kkelley/Desktop/CBB Results/MLDSCBB.csv')

# Extract columns relevant for unsupervised learning (you can adjust as necessary)
features = ['Away Team', 'Home Team', 'Away Score', 'Home Score', 
            'Away OR', 'Away DR', 'Away AT', 'Home OR', 'Home DR', 'Home AT', 'delta OR', 'delta DR', 'delta AT']

# Select only the numeric columns
X = df[features]

# Normalize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform PCA to reduce dimensionality
pca = PCA(n_components=2)  # Reduce to 2 dimensions for easy visualization
X_pca = pca.fit_transform(X_scaled)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3)  # Set the number of clusters you want to create
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Plot the PCA results
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df['Cluster'], cmap='viridis')
plt.title("PCA of Basketball Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar(label='Cluster')
plt.show()

# Examine the cluster centers (centroids)
print("Cluster centers (in original feature space):")
print(kmeans.cluster_centers_)

# Check the distribution of clusters
print(df['Cluster'].value_counts())
