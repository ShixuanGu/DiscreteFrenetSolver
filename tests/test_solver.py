import numpy as np
from discrete_frenet_solver import solve_frenet_frame

def test_straight_line():
    curve = np.array([[0, 0, 0], [1, 0, 0], [2, 0, 0]])
    T, N, B = solve_frenet_frame(curve)
    assert np.allclose(T, np.array([[1, 0, 0]] * 3))
    assert np.allclose(np.abs(N), np.array([[0, 1, 0]] * 3))  # Use abs() to allow for either direction
    assert np.allclose(np.abs(B), np.array([[0, 0, 1]] * 3))  # Use abs() to allow for either direction

    # Check orthogonality
    for t, n, b in zip(T, N, B):
        assert np.isclose(np.dot(t, n), 0)
        assert np.isclose(np.dot(t, b), 0)
        assert np.isclose(np.dot(n, b), 0)

def test_orthogonality():
    curve = np.array([[0, 0, 0], [1, 1, 1], [2, 0, 2], [3, -1, 1]])
    T, N, B = solve_frenet_frame(curve)
    for t, n, b in zip(T, N, B):
        assert np.isclose(np.dot(t, n), 0)
        assert np.isclose(np.dot(t, b), 0)
        assert np.isclose(np.dot(n, b), 0)

def test_complex_curve():
    # Generate a complex 3D curve with 500 points
    t = np.linspace(0, 10*np.pi, 500)
    x = t * np.cos(t)
    y = t * np.sin(t)
    z = t
    curve = np.column_stack((x, y, z))

    # Solve for the Frenet frame
    T, N, B = solve_frenet_frame(curve)

    # Check that we have the correct number of vectors
    assert T.shape == (500, 3)
    assert N.shape == (500, 3)
    assert B.shape == (500, 3)

    # Check orthogonality
    for i in range(500):
        assert np.isclose(np.dot(T[i], N[i]), 0, atol=1e-6)
        assert np.isclose(np.dot(T[i], B[i]), 0, atol=1e-6)
        assert np.isclose(np.dot(N[i], B[i]), 0, atol=1e-6)

    # Check that vectors are unit length
    assert np.allclose(np.linalg.norm(T, axis=1), 1, atol=1e-6)
    assert np.allclose(np.linalg.norm(N, axis=1), 1, atol=1e-6)
    assert np.allclose(np.linalg.norm(B, axis=1), 1, atol=1e-6)

    # Check that T points in the direction of the curve
    tangents = np.diff(curve, axis=0)
    tangents = tangents / np.linalg.norm(tangents, axis=1)[:, np.newaxis]
    
    # Compare computed T with numerical tangents
    alignment = np.abs(np.sum(T[:-1] * tangents, axis=1))
    assert np.allclose(alignment, 1, atol=1e-2), f"Max deviation: {np.max(np.abs(1 - alignment))}"

    # If the above assertion fails, print more detailed information
    if not np.allclose(alignment, 1, atol=1e-2):
        worst_index = np.argmax(np.abs(1 - alignment))
        print(f"Worst alignment at index {worst_index}")
        print(f"Computed T: {T[worst_index]}")
        print(f"Numerical tangent: {tangents[worst_index]}")
        print(f"Alignment: {alignment[worst_index]}")