import pandas as pd
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\wlgpr\Downloads\filtered_traffic_crashes.csv')

weekday_accidents = df[df['day_category'] == 'Weekday']
weekend_accidents = df[df['day_category'] == 'Weekend']


#Extracts only the latitude and longitude columns
#then coverts it into NumPy array for DBSCAN
X_weekday = weekday_accidents[['tb_latitude', 'tb_longitude']].values
X_weekend = weekend_accidents[['tb_latitude', 'tb_longitude']].values
#Apply the DBSCAN
dbscan_weekday = DBSCAN(eps=0.01, min_samples=5).fit(X_weekday)
dbscan_weekend = DBSCAN(eps=0.01, min_samples=5).fit(X_weekend)

weekday_accidents.loc[:, 'cluster'] = dbscan_weekday.labels_
weekend_accidents.loc[:, 'cluster'] = dbscan_weekend.labels_

weekday_accidents.to_csv(r'C:\Users\wlgpr\Downloads\WeekdayClusters.csv', index=False)
weekend_accidents.to_csv(r'C:\Users\wlgpr\Downloads\WeekendClusters.csv', index=False)

print('done')
