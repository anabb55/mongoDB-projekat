##ovde je potrebno dodati indeks na product_id unutar kolekcije reviews1
# db.getCollection("products1").aggregate(
#     [
#         {
#             "$match" : {
#                 "category.secondary" : "Cleansers"
#             }
#         }, 
#         {
#             "$lookup" : {
#                 "from" : "reviews1",
#                 "localField" : "_id",
#                 "foreignField" : "product_id",
#                 "as" : "review_info"
#             }
#         }, 
#         {
#             "$unwind" : {
#                 "path" : "$review_info"
#             }
#         }, 
#         {
#             "$addFields" : {
#                 "brand_id" : "$brand.brand_id",
#                 "brand_name" : "$brand.brand_name",
#                 "review_id" : "$review_info._id",
#                 "author_id" : "$review_info.author_id",
#                 "submission_time" : "$review_info.submission_time",
#                 "review_text" : "$review_info.review_text"
#             }
#         }, 
#         {
#             "$project" : {
#                 "_id" : NumberInt(1),
#                 "product_name" : NumberInt(1),
#                 "price" : NumberInt(1),
#                 "brand_id" : NumberInt(1),
#                 "brand_name" : NumberInt(1),
#                 "review_id" : NumberInt(1),
#                 "author_id" : NumberInt(1),
#                 "submission_time" : NumberInt(1),
#                 "review_text" : NumberInt(1)
#             }
#         }, 
#         {
#             "$lookup" : {
#                 "from" : "authors",
#                 "localField" : "author_id",
#                 "foreignField" : "_id",
#                 "as" : "author_info"
#             }
#         }, 
#         {
#             "$unwind" : {
#                 "path" : "$author_info"
#             }
#         }, 
#         {
#             "$addFields" : {
#                 "author_skin_type" : "$author_info.skin_type"
#             }
#         }, 
#         {
#             "$match" : {
#                 "author_skin_type" : "normal"
#             }
#         }, 
#         {
#             "$group" : {
#                 "_id" : "$brand_id",
#                 "brand_name" : {
#                     "$first" : "$brand_name"
#                 },
#                 "total_products" : {
#                     "$addToSet" : "$_id"
#                 },
#                 "total_comments" : {
#                     "$sum" : NumberInt(1)
#                 }
#             }
#         }, 
#         {
#             "$project" : {
#                 "_id" : NumberInt(1),
#                 "brand_name" : NumberInt(1),
#                 "total_products" : {
#                     "$size" : "$total_products"
#                 },
#                 "total_comments" : NumberInt(1)
#             }
#         }, 
#         {
#             "$sort" : {
#                 "total_comments" : NumberInt(-1)
#             }
#         }, 
#         {
#             "$limit" : NumberInt(10)
#         }
#     ], 
#     {
#         "allowDiskUse" : false
#     }
# );




##obican upit

# db.getCollection("products1").aggregate([
#     {
#         "$match": {
#             "category.secondary": "Cleansers"
#         }
#     },
#     {
#         "$lookup": {
#             "from": "reviews1",
#             "localField": "_id",
#             "foreignField": "product_id",
#             "as": "review_info"
#         }
#     },
#     {
#         "$unwind": {
#             "path": "$review_info"
#         }
#     },
#     {
#         "$addFields": {
#             "brand_id": "$brand.brand_id",
#             "brand_name": "$brand.brand_name",
#             "review_id": "$review_info._id",
#             "author_id": "$review_info.author_id",
#             "submission_time": "$review_info.submission_time",
#             "review_text": "$review_info.review_text"
#         }
#     },
#     {
#         "$lookup": {
#             "from": "authors",
#             "localField": "author_id",
#             "foreignField": "_id",
#             "as": "author_info"
#         }
#     },
#     {
#         "$unwind": {
#             "path": "$author_info"
#         }
#     },
#     {
#         "$addFields": {
#             "author_skin_type": "$author_info.skin_type"
#         }
#     },
#     {
#         "$match": {
#             "author_skin_type": "normal"
#         }
#     },
#     {
#         "$group": {
#             "_id": "$brand_id",
#             "brand_name": { "$first": "$brand_name" },
#             "total_products": { "$addToSet": "$_id" },
#             "total_comments": { "$sum": 1 }
#         }
#     },
#     {
#         "$project": {
#             "_id": 0,
#             "brand_id": "$_id",
#             "brand_name": 1,
#             "total_products": { "$size": "$total_products" },
#             "total_comments": 1
#         }
#     },
#     {
#         "$sort": { "total_comments": -1 }
#     },
#     {
#         "$limit": 10
#     }
# ])








