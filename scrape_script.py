import pandas as pd
import json
import os

with open('./data/lists.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for list in data['items']:
    list_name = list['name']
    nested_items = list['listItems']['items']

    place_names = [item['venue']['name'] for item in nested_items]

    df = pd.DataFrame(place_names, columns=['Place Name'])

    # Ensure the directory exists
    output_directory = './formattedCSV'
    os.makedirs(output_directory, exist_ok=True)

    # Create the full file path
    csv_filename = os.path.join(output_directory, f"{list_name}.csv")

    # Save to the specified directory
    df.to_csv(csv_filename, index=False)

    print(f"Data exported to {csv_filename}")