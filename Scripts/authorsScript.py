import csv
import json

csv_file_path = 'merged_comments.csv'

authors_list = []

def unitialized(value):
    if value == '':
        return None
    try:
        return value
    except ValueError:
        return None 


with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row
    next(csv_reader)
    
    for idx, row in enumerate(csv_reader, start=1):
        
        
            author_id = row[1]
            skin_tone = row[11]
            eye_color = row[12]
            skin_type = row[13]
            hair_color = row[14]

           

            author = {
                '_id': author_id,
                'skin_tone': unitialized(skin_tone),
                'eye_color': unitialized(eye_color),
                'skin_type': unitialized(skin_type),
                'hair_color': unitialized(hair_color)
            }

          
            authors_list.append(author)
            

       
output_file_path = 'C:/Users/Hp/Desktop/sbp projekat/authors.json'

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(authors_list, output_file, indent=4)

print(f"JSON data exported to {output_file_path}")



