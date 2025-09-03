import numpy as np
def input_matrix(name):
    
    print(name)
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns : "))

    print("Enter the matrix row by row(seperated by space:)")
    matrix=[]
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return np.array(matrix)
print("\n=== MATRIX OPERATIONS TOOL ===\n")
A=input_matrix("Matrix A")


B=input_matrix("Matrix B")

print("\nMatrix A:")
print(A)
print("\nMatrix B:")
print(B)

while True:
    print("\nChoose an operation:")
    print("1. Add (A + B)")
    print("2. Subtract (A - B)")
    print("3. Multiply (A x B)")
    print("4. Transpose (A^T, B^T)")
    print("5. Determinant (A or B)")
    print("6. Rank (A, B)")
    print("7. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        if A.shape == B.shape:
            print("\nResult:\n", A + B)
        else:
            print("Matrices must have the same shape for addition.")
    elif choice == "2":
        if A.shape == B.shape:
            print("\nResult:\n", A - B)
        else:
            print("Matrices must have the same shape for subtraction.")
    elif choice == "3":
        if A.shape[1] == B.shape[0]:
            print("\nResult:\n", np.dot(A, B))
        else:
            print("Number of columns of A must equal rows of B for multiplication.")
    elif choice == "4":
        print("\nTranspose of A:\n", A.T)
        print("Transpose of B:\n", B.T)
    elif choice == "5":
        print("\nDeterminant of A (if square):")
        if A.shape[0] == A.shape[1]:
            print(np.linalg.det(A))
        else:
            print("A is not square.")

        print("\nDeterminant of B (if square):")
        if B.shape[0] == B.shape[1]:
            print(np.linalg.det(B))
        else:
            print("B is not square.")
    elif choice == "6":
        print(f"Rank of A = {np.linalg.matrix_rank(A)}")
        print(f"Rank of B = {np.linalg.matrix_rank(B)}")
    elif choice == "7":
        print("Exiting... ")
        break
    else:
        print("Invalid choice.")