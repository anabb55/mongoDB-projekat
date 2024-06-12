# db.getCollection("authors").aggregate(
#     [
#         {
#             "$match" : {
#                 "eye_color" : "brown"
#             }
#         }, 
#         {
#             "$lookup" : {
#                 "from" : "reviews1",
#                 "localField" : "_id",
#                 "foreignField" : "author_id",
#                 "as" : "reviews"
#             }
#         }, 
#         {
#             "$unwind" : {
#                 "path" : "$reviews"
#             }
#         }, 
#         {
#             "$addFields" : {
#                 "review_ID" : "$reviews._id",
#                 "review_text" : "$reviews.review_text"
#             }
#         }, 
#         {
#             "$project" : {
#                 "_id" : NumberInt(1),
#                 "eye_color" : NumberInt(1),
#                 "review_ID" : NumberInt(1),
#                 "review_text" : NumberInt(1)
#             }
#         }, 
#         {
#             "$lookup" : {
#                 "from" : "feedbackStatistics",
#                 "localField" : "review_ID",
#                 "foreignField" : "review_id",
#                 "as" : "feedbacks"
#             }
#         }, 
#         {
#             "$unwind" : {
#                 "path" : "$feedbacks"
#             }
#         }, 
#         {
#             "$addFields" : {
#                 "feedback_id" : "$feedbacks._id",
#                 "total_feedback_count" : "$feedbacks.total_feedback_count"
#             }
#         }, 
#         {
#             "$project" : {
#                 "feedbacks" : NumberInt(0)
#             }
#         }, 
#         {
#             "$match" : {
#                 "total_feedback_count" : {
#                     "$gt" : NumberInt(5)
#                 }
#             }
#         }, 
#         {
#             "$project" : {
#                 "_id" : NumberInt(0),
#                 "eye_color" : NumberInt(1),
#                 "review_text" : NumberInt(1),
#                 "total_feedback_count" : NumberInt(1)
#             }
#         }
#     ], 
#     {
#         "allowDiskUse" : false
#     }
# );