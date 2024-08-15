# Task: Explore Image Compression Using SVD

# 1. Import numpy, matplotlib.pyplot using their corresponding alias.
# Also import Image from the PIL library.



# 2. Load and display the original image. Use Image.open and convert the image
# to grayscale. Call the output image.



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

# plt.figure(figsize=(12, 4))

# plt.subplot(2, 3, 1)
# plt.imshow(compressed_image_5, cmap="gray")
# plt.title("Compressed Image\n(5 SVs)")
# plt.axis("off")

# plt.subplot(2, 3, 2)
# plt.imshow(compressed_image_10, cmap="gray")
# plt.title("Compressed Image\n(10 SVs)")
# plt.axis("off")

# plt.subplot(2, 3, 3)
# plt.imshow(compressed_image_30, cmap="gray")
# plt.title("Compressed Image\n(30 SVS)")
# plt.axis("off")

# plt.subplot(2, 3, 4)
# plt.imshow(compressed_image_50, cmap="gray")
# plt.title("Compressed Image\n(50 SVs)")
# plt.axis("off")

# plt.subplot(2, 3, 5)
# plt.imshow(compressed_image_100, cmap="gray")
# plt.title("Compressed Image\n(100 SVs)")
# plt.axis("off")

# plt.subplot(2, 3, 6)
# plt.imshow(image, cmap="gray")
# plt.title("Original Image\n(1024 SVs)")
# plt.axis("off")

# plt.show()
