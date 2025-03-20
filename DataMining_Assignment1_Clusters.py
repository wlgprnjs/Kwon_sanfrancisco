import pandas as pd
import matplotlib.pyplot as plt #visualization
import seaborn as sns #visualization
from sklearn.cluster import KMeans

# Load the CSV files into DataFrames
weekday_data = pd.read_csv(r'C:\Users\wlgpr\Downloads\WeekdayClusters.csv')
weekend_data = pd.read_csv(r'C:\Users\wlgpr\Downloads\WeekendClusters.csv')

#Preparing longitude and latitude for each csv
weekday_coords = weekday_data[['tb_longitude', 'tb_latitude']]
weekend_coords = weekend_data[['tb_longitude', 'tb_latitude']]

sample_fraction = 0.3 # Yearly apporoximately about 15,000. which is 30% out of all the dataset i have
weekday_sample = weekday_data.sample(frac=sample_fraction)
weekend_sample = weekend_data.sample(frac=sample_fraction)

# Weekday k-means
weekday_kmeans = KMeans(n_clusters=7)  #6 clusters 
weekday_data['cluster'] = weekday_kmeans.fit_predict(weekday_coords)

# Weekend k-means
weekend_kmeans = KMeans(n_clusters= 4)  # 4 clusters because less traffic in some parts of the area
weekend_data['cluster'] = weekend_kmeans.fit_predict(weekend_coords)

# Weekend Visualization (using sample)
plt.figure(figsize=(10, 8)) #size for the vizualization
sns.scatterplot(x='tb_longitude', y='tb_latitude', hue='cluster', data=weekday_sample, palette='viridis')
#Plotting the cluster centers with red stars and NumPy
plt.scatter(weekday_kmeans.cluster_centers_[:, 0], weekday_kmeans.cluster_centers_[:, 1], s=300, c='red', marker='*', label='Centroids')
plt.title('Weekday Accident Clusters (K-means,30% Sample)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.show()

# Weekend Visualization (using sample)
plt.figure(figsize=(10, 8))
sns.scatterplot(x='tb_longitude', y='tb_latitude', hue='cluster', data=weekend_sample, palette='viridis')
plt.scatter(weekend_kmeans.cluster_centers_[:, 0], weekend_kmeans.cluster_centers_[:, 1], s=300, c='red', marker='*', label='Centroids')
plt.title('Weekend Accident Clusters (K-means, 30% Sample)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.show()