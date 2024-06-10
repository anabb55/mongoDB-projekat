# //upit 1
# //prvo samo racunamo broj komentara za primary category Skincare
# db.reviews.aggregate([
    
#     {
#         $lookup: {
#             from: "products",
#             localField: "product_id",
#             foreignField: "_id",
#             as: "product_info"
#         }
#     },
    
#     {
#         $unwind: "$product_info"
#     },
#     //filtriramo samo one review-ove koji s odnose na proizvode sa primarnom kategorijom Skincare
#     {
#         $match: {
#             "product_info.category.primary": "Skincare"
#         }
#     },
    
#     {
#         $count: "total_reviews"
#     }
# ])



# //celi upit kada pridruzujemo i autora kako bismo nasli tip koze autora - vreme izvrsavanja: 2:51

# db.reviews.aggregate([
    
#     {
#         $lookup: {
#             from: "products",
#             localField: "product_id",
#             foreignField: "_id",
#             as: "product_info"
#         }
#     },
    
#     {
#         $unwind: "$product_info"
#     },
  
#     {
#         $match: {
#             "product_info.category.primary": "Skincare"
#         }
#     },
    
#     {
#         $lookup: {
#             from: "authors",
#             localField: "author_id",
#             foreignField: "_id",
#             as: "author_info"
#         }
#     },
   
#     {
#         $unwind: "$author_info"
#     },
#     //pravis grupe dokumenata u odnosu na tip koze i za svaki tip koze racunas ukuban broj komentara
#     {
#         $group: {
#             _id: {
#                 skin_type: "$author_info.skin_type"
#             },
#             total_reviews: { $sum: 1 }
#         }
#     },
#     //ovo je samo menjanje izgleda dokumenta
#     {
#         $project: {
#             _id: 0,
#             skin_type: "$_id.skin_type",
#             total_reviews: 1
#         }
#     },
   
#     {
#         $group: {
#             _id: null,
#             total_reviews: { $sum: "$total_reviews" },
#             dry_skin_reviews: {
#                 $sum: {
#                     $cond: [{ $eq: ["$skin_type", "dry"] }, "$total_reviews", 0]
#                 }
#             }
#         }
#     },
    
#     {
#         $project: {
#             _id: 0,
#             dry_skin_reviews: 1,
#             total_reviews: 1,
#             dry_skin_ratio: {
#                 $cond: [{ $eq: ["$total_reviews", 0] }, 0, { $divide: ["$dry_skin_reviews", "$total_reviews"] }]
#             }
#         }
#     }
# ])

