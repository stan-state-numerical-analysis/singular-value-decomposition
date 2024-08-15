# Task: Explore Image Compression Using SVD

# 1. Import numpy, matplotlib.pyplot using their corresponding alias.
# Also import Image from the PIL library.



# 2. Load and display the original PNG image included in this folder. Use Image.open
# and convert the image to grayscale. Call the output image.



# 3. Redefine image to be the numpy array version of itself.



# 4. Print the image (now a numpy array) to see how the image is
# represented as a matrix.



# 4. Use numpy.linalg.svd to decompose the image matrix into U, S, and Vt
# from its SVD.



# 6. Define a function called compress_image which will compress the image.
#    - Parameters:
#      - U: The matrix of left singular vectors of the original image.
#      - S: The singular values of the original image.
#      - Vt: The matrix of right singular vectors of the original image.
#      - num_singular_values: The number of singular values to retain.



    # 7. Initialize U_compressed, S_compressed, and Vt_compressed to be
    # U, S, and Vt with only the indicated number of singular values retained.



    # 8. Reconstruct the (now compressed) image using S_ compressed, U_compressed,
    # and V_compressed from above. Call the output compressed_image.



    # 9. Return the compressed image.



# 7. Define compressed_image_5, compressed_image_10, compressed_image_30, compressed_image_50,
# and compressed_image_100 to be the result of the image compression retaining 5, 10, 30,
# 50, and 100 singular values respectively.



# 8. Uncomment the code belo to display the compressed images.

# def plot_svd_comparison(
#     img_1,
#     img_2,
#     img_3,
#     img_4,
#     img_5,
#     original_image,
# ):
#     fig, axes = plt.subplots(2, 3, figsize=(12, 8))  # Create a 2x3 grid of subplots

#     # Plot the compressed images with varying numbers of singular values
#     axes[0, 0].imshow(img_1, cmap="gray")
#     axes[0, 0].set_title("Compressed Image\n(5 SVs)")
#     axes[0, 0].axis("off")

#     axes[0, 1].imshow(img_2, cmap="gray")
#     axes[0, 1].set_title("Compressed Image\n(10 SVs)")
#     axes[0, 1].axis("off")

#     axes[0, 2].imshow(img_3, cmap="gray")
#     axes[0, 2].set_title("Compressed Image\n(30 SVs)")
#     axes[0, 2].axis("off")

#     axes[1, 0].imshow(img_4, cmap="gray")
#     axes[1, 0].set_title("Compressed Image\n(50 SVs)")
#     axes[1, 0].axis("off")

#     axes[1, 1].imshow(img_5, cmap="gray")
#     axes[1, 1].set_title("Compressed Image\n(100 SVs)")
#     axes[1, 1].axis("off")

#     axes[1, 2].imshow(original_image, cmap="gray")
#     axes[1, 2].set_title("Original Image\n(1024 SVs)")
#     axes[1, 2].axis("off")

#     plt.tight_layout()  # Adjust the layout to avoid overlap
#     return fig


# plot_svd_comparison(
#     compressed_image_5,
#     compressed_image_10,
#     compressed_image_30,
#     compressed_image_50,
#     compressed_image_100,
#     image,
# )
