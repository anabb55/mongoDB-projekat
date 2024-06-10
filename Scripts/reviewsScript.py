import csv
import json

csv_file_path = 'merged_comments.csv'

reviews_list = []
feedback_statistics_list = []

with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row
    next(csv_reader)
    
    for idx, row in enumerate(csv_reader, start=1):
        
        if len(row) >= 7:
            author_id = row[1]
            product_id = row[15]
            rating = row[2]
            is_recommended = row[3]
            submission_time = row[8]
            review_text = row[9]
            review_title = row[10]
            helpfulness = row[4]
            total_feedback_count = row[5]
            total_pos_feedback_count = row[7]
            total_neg_feedback_count = row[6]

   
            try:
                rating = int(rating)
            except ValueError:
                rating = 0
           
            try:
                is_recommended = float(is_recommended)
            except ValueError:
                is_recommended = 0.0

            try:
                helpfulness = float(helpfulness)
            except ValueError:
                helpfulness = 0.0

            review = {
                '_id': idx,
                'author_id': author_id,
                'product_id': product_id,
                'rating': rating,
                'is_recommended': is_recommended,
                'submission_time': submission_time,
                'review_text': review_text,
                'review_title': review_title
            }

            feedbackStatistic = {
                '_id' : idx,
                'review_id' : idx,
                'helpfulness': helpfulness,
                'total_feedback_count': int(total_feedback_count),
                'total_pos_feedback_count': int(total_pos_feedback_count),
                'total_neg_feedback_count': int(total_neg_feedback_count)
            }
            
            reviews_list.append(review)
            feedback_statistics_list.append(feedbackStatistic)

        else:
            print(f"Skipping row {idx} due to insufficient columns.")

output_file_path_reviews = 'C:/Users/Hp/Desktop/sbp projekat/reviews.json'
output_file_path_feedback_statistics = 'C:/Users/Hp/Desktop/sbp projekat/feedbackStatistics.json'

with open(output_file_path_reviews, 'w', encoding='utf-8') as output_file:
    json.dump(reviews_list, output_file, indent=4)

print(f"JSON data exported to {output_file_path_reviews}")


with open(output_file_path_feedback_statistics, 'w', encoding='utf-8') as output_file:
    json.dump(feedback_statistics_list, output_file, indent=4)

print(f"JSON data exported to {output_file_path_feedback_statistics}")
