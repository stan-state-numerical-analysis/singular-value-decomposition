# Task: Implement Singular Value Decomposition (SVD) from Scratch

# 1. Import numpy with its corresponding alias.



# 2. Set the numpy random seed to 13.



# 3. Define a function called complete_orthonormal_basis that ensures all columns of U are orthonormal.
#    - Parameters:
#      - U: The matrix where some columns might be zero vectors.



    # 4. Iterate over the columns of U.



        # 5. If the column is approximately the zero vector, we will replace it with
        # a standard basis vector. Use the allclose comparison operator from numpy
        # to check if it is approximately the zero vector.



            # 6. Create a standard basis vector with a 1 in the position of the
            # current column index, call it new_vector .



            # 7. Apply Gram-Schmidt process to make new_vector orthogonal to previous columns.



            # 8. Normalize the new vector.



            # 9. Replace the zero column with the orthonormal vector.



    # 10. Return the updated matrix U.



# 11. Define a function called svd that computes the Singular Value Decomposition of a matrix A.
#     - Parameters:
#       - A: The matrix to decompose.
#     - Return:
#       - U, Sigma, Vt: The decomposed matrices.



    # 12. Use the np.linalg.eig method to find the eigenvalues and eigenvectors
    # of A^T * A. Call the pair eigenvalues, V (so V is the set of eigenvalues as columns).



    # 13. Use the np.argsort method to obtain the order of indices to
    # sort the eigenvalues *from biggest to smallest*. Call the output sorted_indices.



    # 14. Compute the singular values as the square root of the sorted eigenvalues, take
    # only the real parts (using numpy's real method) and sort the rows according
    # to sorted_indices. Call the output Sigma.



    # 15. Redefine V so that its *columns* use the sorted_indices ordering.



    # 16. Define Sigma_rec to be the list of reciprocals of
    # non-zero singular values (and 0 if they are 0).



    # 17. Compute the U matrix using the corresponding formula and Sigma_rec defined
    # above.



    # 18. Ensure all columns of U are orthonormal using the complete_orthonormal_basis function.
    # Note: Applying complete_orthonormal_basis only changes U if there are singular values equal to 0.



    # 19. Return U, Sigma (not Sigma_rec), and the *transpose* of V.


