import pandas as pd

df = pd.read_csv(r'C:\Users\wlgpr\Downloads\filtered_traffic_crashes.csv')


weekday_weekend_counts = df.groupby(['day_category', 'type_of_collision']).size().reset_index(name='accident_count')

# Save for Tableau visualization
weekday_weekend_counts.to_csv(r'C:\Users\wlgpr\Downloads\WeekdayWeekendAccidents.csv', index=False)
print('done')