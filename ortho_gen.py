import numpy as np

def get_factor_levels(factor_name):
    num_levels = int(input(f"Enter the number of levels for {factor_name}: "))
    levels = [input(f"Enter level {i + 1} for {factor_name}: ") for i in range(num_levels)]
    return np.array(levels)

def create_orthogonal_matrix():
    num_factors = int(input("Enter the number of factors: "))
    factor_names = [input(f"Enter name for factor {i + 1}: ") for i in range(num_factors)]

    factor_levels = [get_factor_levels(name) for name in factor_names]
    design_matrix = np.array(factor_levels)

    # Perform QR factorization
    Q, R = np.linalg.qr(design_matrix)

    print("Orthogonal matrix Q:")
    print(Q)

if __name__ == "__main__":
    create_orthogonal_matrix()
