import numpy as np

# example user interest data
user_interests = np.array([[1, 0, 1, 1, 0],  # user 1
                           [0, 1, 0, 1, 1],  # user 2
                           [1, 1, 0, 0, 1],  # user 3
                           [0, 0, 1, 1, 0],  # user 4
                           [0, 1, 1, 0, 1]]) # user 5

# compute similarity scores using dot product
def compute_similarity(user_interests, user):
    similarity_scores = np.dot(user_interests, user)
    return similarity_scores

# find top matches
def find_top_matches(similarity_scores, n):
    top_matches = np.argpartition(-similarity_scores, n)[:n]
    return top_matches

# example user input
user_input = np.array([1, 0, 0, 1, 0])  # user input interests

# compute similarity scores
similarity_scores = compute_similarity(user_interests, user_input)

# find top matches
top_matches = find_top_matches(similarity_scores, 3)

# display top matching users
print("top matching users based on interests:")
for i, user_idx in enumerate(top_matches):
    similarity_score = similarity_scores[user_idx]
    print("user", user_idx + 1, "with similarity score:", similarity_score)

    # display interests of the top matching users
    user_interests_str = " ".join(str(interest) for interest in user_interests[user_idx])
    print("interests: ", user_interests_str)
