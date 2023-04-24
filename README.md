# EnsomBot
This repository contains a Python script to match a user's interests with other users based on their interests. The matching is done using the dot product of the user interest matrix with a given user input.

## How to use

To use this script, you need to have `numpy` installed. The user interests are represented as a matrix where each row corresponds to a user and each column corresponds to an interest. 

You can customize the `user_interests` matrix to your needs by adding or removing users and interests. Then, you can run the `compute_similarity` function to compute the similarity scores between the users' interests and a given user input. Finally, you can use the `find_top_matches` function to find the top matching users based on their similarity scores.

