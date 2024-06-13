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

def to_int(value):
    if value == '':
        return None
    try:
        return int(value)
    except ValueError:
        return None

def to_float(value):
    if value == '':
        return None
    try:
        return float(value)
    except ValueError:
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
        variation_type = row[8]
        variation_value = row[9]
        variation_desc = row[10]
        child_count = row[24]
        child_max_price = row[25]
        child_min_price = row[26]

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
            'variation_type': uninitialized(variation_type),
            'variation_value': uninitialized(variation_value),
            'variation_desc': uninitialized(variation_desc),
            'child_count': to_int(child_count),
            'child_max_price': to_float(child_max_price),
            'child_min_price': to_float(child_min_price)
        }
        

        product = {
            '_id': product_id,
            'product_name': uninitialized(product_name),
            'loves_count': to_int(loves_count),
             'brand':brand,
            'rating': to_float(rating),
            'reviews': to_int(reviews),
            'size': uninitialized(size),
            'ingredients': uninitialized(ingredients),
            'price': to_float(price),
            'sale_price': to_float(sale_price),
            'limited_edition': true_false(limited_edition),
            'new': true_false(new),
            'online_only': true_false(online_only),
            'out_of_stock': true_false(out_of_stock),
            'sephora_exclusive': true_false(sephora_exclusive),
            'highlights': uninitialized(higlights),
             'category': category,
             'variation': variation
            
        }

        products_list.append(product)

output_file_path = 'C:/Users/Hp/Desktop/sbp projekat/products_final.json'

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(products_list, output_file, indent=4)

print(f"JSON data exported to {output_file_path}")