# Finding high risk intersection by collision type (with tallimarks)
import pandas as pd

df = pd.read_csv(r'C:\Users\wlgpr\Downloads\filtered_traffic_crashes.csv')

# Count accidents at each intersection by type
high_risk_intersections = df.groupby(['intersection', 'type_of_collision']).size().reset_index(name='accident_count')

# Sort by highest accident counts
high_risk_intersections = high_risk_intersections.sort_values(by='accident_count', ascending=False)

# Save for Tableau visualization
high_risk_intersections.to_csv(r'C:\Users\wlgpr\Downloads\High_Risk_Intersections.csv', index=False)

print('All done!')  
