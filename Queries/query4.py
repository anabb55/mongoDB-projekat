# db.getCollection("products1").aggregate(
#     [
#         {
#             "$lookup" : {
#                 "from" : "variations",
#                 "localField" : "_id",
#                 "foreignField" : "product_id",
#                 "as" : "variation_info"
#             }
#         }, 
#         {
#             "$unwind" : {
#                 "path" : "$variation_info"
#             }
#         }, 
#         {
#             "$addFields" : {
#                 "variation_type" : "$variation_info.variation_type",
#                 "variation_num" : "$variation_info.child_count",
#                 "max_variation_price" : {
#                     "$toDouble" : "$variation_info.child_max_price"
#                 },
#                 "min_variation_price" : {
#                     "$toDouble" : "$variation_info.child_min_price"
#                 }
#             }
#         }, 
#         {
#             "$match" : {
#                 "max_variation_price" : {
#                     "$ne" : null
#                 },
#                 "min_variation_price" : {
#                     "$ne" : null
#                 }
#             }
#         }, 
#         {
#             "$project" : {
#                 "_id" : NumberInt(1),
#                 "product_name" : NumberInt(1),
#                 "price" : NumberInt(1),
#                 "variation_type" : NumberInt(1),
#                 "variation_num" : NumberInt(1),
#                 "max_variation_price" : NumberInt(1),
#                 "min_variation_price" : NumberInt(1)
#             }
#         }, 
#         {
#             "$addFields" : {
#                 "price_difference" : {
#                     "$subtract" : [
#                         "$max_variation_price",
#                         "$min_variation_price"
#                     ]
#                 }
#             }
#         }, 
#         {
#             "$group" : {
#                 "_id" : "$price_difference",
#                 "products" : {
#                     "$push" : "$$ROOT"
#                 }
#             }
#         }, 
#         {
#             "$sort" : {
#                 "_id" : NumberInt(-1)
#             }
#         }, 
#         {
#             "$limit" : NumberInt(1)
#         }, 
#         {
#             "$unwind" : {
#                 "path" : "$products"
#             }
#         }, 
#         {
#             "$addFields" : {
#                 "total_profit_for_product" : {
#                     "$multiply" : [
#                         NumberInt(50),
#                         {
#                             "$toDouble" : "$products.price"
#                         }
#                     ]
#                 },
#                 "product_name" : "$products.product_name",
#                 "price" : "$products.price",
#                 "variation_type" : "$products.variation_type",
#                 "variation_num" : "$products.variation_num",
#                 "max_variation_price" : "$products.max_variation_price",
#                 "min_variation_price" : "$products.min_variation_price",
#                 "price_difference" : "$products.price_difference"
#             }
#         }, 
#         {
#             "$project" : {
#                 "_id" : NumberInt(0),
#                 "product_name" : NumberInt(1),
#                 "price" : NumberInt(1),
#                 "variation_type" : NumberInt(1),
#                 "variation_num" : NumberInt(1),
#                 "max_variation_price" : NumberInt(1),
#                 "min_variation_price" : NumberInt(1),
#                 "price_difference" : NumberInt(1),
#                 "total_profit_for_product" : NumberInt(1)
#             }
#         }
#     ], 
#     {
#         "allowDiskUse" : false
#     }
# );


# db.getCollection("products1").aggregate([
#   {
#     "$lookup": {
#       "from": "variations",
#       "localField": "_id",
#       "foreignField": "product_id",
#       "as": "variation_info"
#     }
#   },
#   {
#     "$unwind": "$variation_info"
#   },
#   {
#     "$addFields": {
#       "variation_type": "$variation_info.variation_type",
#       "variation_num": "$variation_info.child_count",
#       "max_variation_price": { "$toDouble": "$variation_info.child_max_price" },
#       "min_variation_price": { "$toDouble": "$variation_info.child_min_price" }
#     }
#   },
#   {
#     "$match": {
#       "max_variation_price": { "$ne": null },
#       "min_variation_price": { "$ne": null }
#     }
#   },
#   {
#     "$project": {
#       "_id": 1,
#       "product_name": 1,
#       "price": 1,
#       "variation_type": 1,
#       "variation_num": 1,
#       "max_variation_price": 1,
#       "min_variation_price": 1
#     }
#   },
#   {
#     "$addFields": {
#       "price_difference": { "$subtract": ["$max_variation_price", "$min_variation_price"] }
#     }
#   },
#   {
#     "$group": {
#       "_id": "$price_difference",
#       "products": { "$push": "$$ROOT" }
#     }
#   },
#   {
#     "$sort": { "_id": -1 }
#   },
#   {
#     "$limit": 1
#   },
#   {
#     "$unwind": "$products"
#   },
#   {
#     "$addFields": {
#       "total_profit_for_product": { "$multiply": [50, { "$toDouble": "$products.price" }] },
#       "product_name": "$products.product_name",
#       "price": "$products.price",
#       "variation_type": "$products.variation_type",
#       "variation_num": "$products.variation_num",
#       "max_variation_price": "$products.max_variation_price",
#       "min_variation_price": "$products.min_variation_price",
#       "price_difference": "$products.price_difference"
#     }
#   },
#   {
#     "$project": {
#       "_id": 0,
#       "product_name": 1,
#       "price": 1,
#       "variation_type": 1,
#       "variation_num": 1,
#       "max_variation_price": 1,
#       "min_variation_price": 1,
#       "price_difference": 1,
#       "total_profit_for_product": 1
#     }
#   }
# ]);
