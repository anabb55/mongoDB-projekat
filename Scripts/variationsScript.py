import csv
import json

csv_file_path = 'product_info.csv'

variations_list = []

def uninitialized(value):
    if value == '':
        return None
    return value

with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row
    next(csv_reader)
    
    for idx, row in enumerate(csv_reader, start=1):
        product_id = row[0]
        variation_type = row[8]
        variation_value = row[9]
        variation_desc = row[10]
        child_count = row[24]
        child_max_price = row[25]
        child_min_price = row[26]

        variation = {
            '_id': idx,
            'product_id': product_id,
            'variation_type': uninitialized(variation_type),
            'variation_value': uninitialized(variation_value),
            'variation_desc': uninitialized(variation_desc),
            'child_count': uninitialized(child_count),
            'child_max_price': uninitialized(child_max_price),
            'child_min_price': uninitialized(child_min_price)
        }

        variations_list.append(variation)

output_file_path = 'C:/Users/Hp/Desktop/sbp projekat/variations.json'

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(variations_list, output_file, indent=4)

print(f"JSON data exported to {output_file_path}")
