# db.getCollection("feedbackStatistics").aggregate(
#     [
#         {
#             "$lookup" : {
#                 "from" : "reviews",
#                 "localField" : "review_id",
#                 "foreignField" : "_id",
#                 "as" : "review"
#             }
#         }, 
#         {
#             "$unwind" : {
#                 "path" : "$review"
#             }
#         }, 
#         {
#             "$match" : {
#                 "review.submission_time" : {
#                     "$gte" : "2018-01-01",
#                     "$lte" : "2023-01-01"
#                 }
#             }
#         }, 
#         {
#             "$lookup" : {
#                 "from" : "products",
#                 "localField" : "review.product_id",
#                 "foreignField" : "_id",
#                 "as" : "product"
#             }
#         }, 
#         {
#             "$unwind" : {
#                 "path" : "$product"
#             }
#         }, 
#         {
#             "$match" : {
#                 "product.online_only" : true
#             }
#         }, 
#         {
#             "$group" : {
#                 "_id" : "$product._id",
#                 "product_name" : {
#                     "$first" : "$product.product_name"
#                 },
#                 "brand_name" : {
#                     "$first" : "$product.brand.brand_name"
#                 },
#                 "primary_category" : {
#                     "$first" : "$product.category.primary"
#                 },
#                 "total_neg_feedback_count" : {
#                     "$sum" : "$total_neg_feedback_count"
#                 },
#                 "review_count" : {
#                     "$sum" : NumberInt(1)
#                 }
#             }
#         }, 
#         {
#             "$sort" : {
#                 "total_neg_feedback_count" : NumberInt(-1)
#             }
#         }, 
#         {
#             "$project" : {
#                 "_id" : NumberInt(0),
#                 "product_name" : NumberInt(1),
#                 "brand_name" : NumberInt(1),
#                 "primary_category" : NumberInt(1),
#                 "total_neg_feedback_count" : NumberInt(1),
#                 "review_count" : NumberInt(1)
#             }
#         }
#     ], 
#     {
#         "allowDiskUse" : false
#     }
# );




## pravi upit

# db.feedbackStatistics.aggregate([
 
#   {
#     $lookup: {
#       from: "reviews",
#       localField: "review_id",
#       foreignField: "_id",
#       as: "review"
#     }
#   },
 
#   {
#     $unwind: "$review"
#   },
 
#   {
#     $match: {
#       "review.submission_time": {
#         $gte: "2018-01-01",
#         $lte: "2023-01-01"
#       }
#     }
#   },
  
#   {
#     $lookup: {
#       from: "products",
#       localField: "review.product_id",
#       foreignField: "_id",
#       as: "product"
#     }
#   },
 
#   {
#     $unwind: "$product"
#   },
  
#   {
#     $match: {
#       "product.online_only": true
#     }
#   },
  
#   {
#     $group: {
#       _id: "$product._id",
#       product_name: { $first: "$product.product_name" },
#       brand_name: { $first: "$product.brand.brand_name" },
#       primary_category: { $first: "$product.category.primary" },
#       total_neg_feedback_count: { $sum: "$total_neg_feedback_count" },
#       review_count: { $sum: 1 }
#     }
#   },
  
#   {
#     $sort: {
#       total_neg_feedback_count: -1
#     }
#   },
 
#   {
#     $project: {
#       _id: 0,
#       product_name: 1,
#       brand_name: 1,
#       primary_category: 1,
#       total_neg_feedback_count: 1,
#       review_count: 1
#     }
#   }
# ])
