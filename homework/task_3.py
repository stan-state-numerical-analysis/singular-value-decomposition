# Task: Dimensionality Reduction Using SVD
# In this assignment, you will explore how SVD can be used to help classify wines.

# 1. Import numpy and matplotlib.pyplot under their corresponding aliases.



# 2. Import load_wine from sklearn.datasets.



# 3. Import StandardScaler from sklearn.preprocessing.



# 4. Initialize the variable data from the load_wine method.



# 5. Initialize the variable X to be the data attribute of the data
# variable defined above.



# Each row of X represents 13 different properties of a wine sample.
# Examples of properties measured are alcohol content, malic acid, ash, etc.
# There are 178 samples represented in X (so that many rows) and each one comes from
# one of three types of wine (in the wine world they call these cultivars).
# So X has 178 rows and 13 columns.

# 6. Print X to confirm its description above.



# 7. Initialize the variable y to be the target attribute of the data
# variable defined in 4.



# The vector y has 178 rows and one column. Each row of y corresponds to a row of X.
# The value of the column classifies what type of wine the sample came from.
# The type of win is represented as either 0, 1, or 2.

# 8. Print y to confirm its description above.



# 9. Use StandardScaler and its fit_transform method to standardize the data in X.
# This will ensure each column of X has a mean of 0 and variance of 1. Call the
# standardized version of X X_standardized.



# 10. Use numpy.linalg.svd to decompose the standardized data matrix X_standardized.
# Call the result of the decomposition U, S, and Vt.



# 11. Define a function similar to compress_image from task_2 which reduces the
# dimensions of the data. Call the function reduce_dimensions.
#    - Parameters:
#      - U: The matrix of left singular vectors of the standardized data.
#      - S: The singular values of the the standardized data.
#      - Vt: The matrix of right singular vectors of the standardized data.
#      - num_dimensions: The number of singular values / dimensions to retain.



    # 12. Initialize U_reduced, S_reduced, and Vt_reduced to be
    # U, S, and Vt with only the indicated number of singular values retained.



    # 13. Reconstruct the (now reduced) data using S_reduced, U_reduced,
    # and V_reduced from above. Call the output X_reduced.



    # 14. Return the reduced data.



# 15. Define X_reduced_2 and X_reduced_3 to be the result of the
# dimensionality reduction on X retaining 2 and 3 dimensions, respectively.



# 16. Uncomment the code below to plot the original data in 2D and
# the reduced-dimensional data in 2D. You should see that the three
# different types of wine are more separated after dimensionality reduction.


# def plot_data_2D(X_standardized, X_reduced_2, y):
#     fig, ax = plt.subplots(1, 2, figsize=(12, 6))

#     # Original data in 2D
#     ax[0].scatter(X_standardized[:, 0], X_standardized[:, 1], c=y, cmap="viridis")
#     ax[0].set_title("Original Data (First 2 Features)")
#     ax[0].set_xlabel("Feature 1")
#     ax[0].set_ylabel("Feature 2")

#     # Reduced-dimensional data in 2D (using 2 components)
#     ax[1].scatter(X_reduced_2[:, 0], X_reduced_2[:, 1], c=y, cmap="viridis")
#     ax[1].set_title("Reduced-Dimensional Data (2 Dimensions)")
#     ax[1].set_xlabel("Dimension 1")
#     ax[1].set_ylabel("Dimension 2")

#     # Adjust layout for better spacing
#     plt.tight_layout()

#     return fig


# plot_data_2D(X_standardized, X_reduced_2, y)

# 16. Uncomment the code below to plot the original data in 3D and
# the reduced-dimensional data in 3D. You should see that the three
# different types of wine are more separated after dimensionality reduction.
# You can use your mouse to rotate the 3D plot.


# def plot_data_3D(X_standardized, X_reduced_3, y):
#     fig = plt.figure(figsize=(12, 6))

#     # Original data in 3D
#     ax1 = fig.add_subplot(121, projection="3d")
#     ax1.scatter(
#         X_standardized[:, 0],
#         X_standardized[:, 1],
#         X_standardized[:, 2],
#         c=y,
#         cmap="viridis",
#     )
#     ax1.set_title("Original Data (First 3 Features)")
#     ax1.set_xlabel("Feature 1")
#     ax1.set_ylabel("Feature 2")
#     ax1.set_zlabel("Feature 3")

#     # Reduced-dimensional data in 3D (using 3 components)
#     ax2 = fig.add_subplot(122, projection="3d")
#     ax2.scatter(
#         X_reduced_3[:, 0],
#         X_reduced_3[:, 1],
#         X_reduced_3[:, 2],
#         c=y,
#         cmap="viridis",
#     )
#     ax2.set_title("Reduced-Dimensional Data (3 Dimensions)")
#     ax2.set_xlabel("Dimension 1")
#     ax2.set_ylabel("Dimension 2")
#     ax2.set_zlabel("Dimension 3")

#     # Adjust layout for better spacing
#     plt.tight_layout()

#     return fig


# plot_data_3D(X_standardized, X_reduced_3, y)
# plt.show()
