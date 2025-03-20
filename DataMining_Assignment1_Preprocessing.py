import pandas as pd

# Load the CSV file 
df = pd.read_csv(r'C:\Users\wlgpr\Downloads\Traffic_Crashes_Resulting_in_Injury_20250317.csv')

# Keep only the specified columns
columns_to_keep = ['unique_id', 'collision_time', 'collision_severity', 'intersection', 
                   'type_of_collision', 'weather_1','day_of_week','month', 'tb_latitude', 'tb_longitude']

df = df[columns_to_keep]

# Remove duplicate rows
df = df.drop_duplicates(subset=columns_to_keep, keep='first')

#Remove 'Not Stated' from the two attributes 
df = df.loc[(df['type_of_collision'] != 'Not Stated') & (df['weather_1'] != 'Not Stated') & (df['type_of_collision'] != 'Other') &  (df['collision_time'] != ' ')]
#Remove rows with empty columns
df = df.dropna(subset=columns_to_keep)

# Convert 'collision_time' to datetime format if it's not already
df['collision_time'] = pd.to_datetime(df['collision_time'], format='%H:%M:%S').dt.time

#Function to categorize rush hour
def is_rush_hour(time):
    if (time >= pd.to_datetime('07:00:00', format='%H:%M:%S').time() and time <= pd.to_datetime('09:00:00', format='%H:%M:%S').time()) or \
       (time >= pd.to_datetime('16:30:00', format='%H:%M:%S').time() and time <= pd.to_datetime('18:30:00', format='%H:%M:%S').time()):
        return 1
    else:
        return 0

# Apply function to create the 'rush_hour' column
df['rush_hour'] = df['collision_time'].map(is_rush_hour)

#Categorize weekday and weekends
df['day_category'] = df['day_of_week'].apply(lambda x: 'Weekend' if x in ['Saturday', 'Sunday'] else 'Weekday')


severity_map = {
    'Injury (Complaint of Pain)': 2,
    'Injury (Other Visible)': 1,
    'Injury (Severe)': 3
}

df['severity_num'] = df['collision_severity'].map(severity_map)

#Delete these after creating the new columns
df = df.drop(columns =['collision_severity','collision_time', 'day_of_week']) 
# Save the cleaned data to a new CSV file
df.to_csv(r'C:\Users\wlgpr\Downloads\filtered_traffic_crashes.csv', index=False)

print("Filtered CSV saved successfully!") #confirm it saved
