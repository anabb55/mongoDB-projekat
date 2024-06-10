import csv
import json

csv_file_path = 'product_info.csv'

products_list = []

def uninitialized(value):
    if value == '':
        return None
    return value

def true_false(value):
    if value == '1':
        return True
    elif value == '0':
        return False
    return None

with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row
    next(csv_reader)
    
    for idx, row in enumerate(csv_reader, start=1):
        product_id = row[0]
        product_name = row[1]
        loves_count = row[4]
        brand_id = row[2]
        brand_name = row[3]
        rating = row[5]
        reviews = row[6]
        size = row[7]
        ingredients = row[11]
        price = row[12]
        sale_price = row[14]
        limited_edition = row[15]
        new = row[16]
        online_only = row[17]
        out_of_stock = row[18]
        sephora_exclusive = row[19]
        higlights = row[20]
        primary_category = row[21]
        secondary_category = row[22]
        tertiary_category = row[23]

        category = {
            'primary': uninitialized(primary_category),
            'secondary': uninitialized(secondary_category),
            'tertiary': uninitialized(tertiary_category)
        }

        brand = {
            'brand_id': int(brand_id),
            'brand_name': uninitialized(brand_name)
        }
        

        variation = {
            '_id': product_id,
            'product_name': uninitialized(product_name),
            'loves_count': uninitialized(loves_count),
             'brand':brand,
            'rating': uninitialized(rating),
            'reviews': uninitialized(reviews),
            'size': uninitialized(size),
            'ingredients': uninitialized(ingredients),
            'price': uninitialized(price),
            'sale_price': uninitialized(sale_price),
            'limited_edition': true_false(limited_edition),
            'new': true_false(new),
            'online_only': true_false(online_only),
            'out_of_stock': true_false(out_of_stock),
            'sephora_exclusive': true_false(sephora_exclusive),
            'highlights': uninitialized(higlights),
             'category': category
            
        }

        products_list.append(variation)

output_file_path = 'C:/Users/Hp/Desktop/sbp projekat/products.json'

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(products_list, output_file, indent=4)

print(f"JSON data exported to {output_file_path}")
