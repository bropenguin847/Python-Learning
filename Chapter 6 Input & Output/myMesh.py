import numpy as np

def separateIR(R):
    """
    Separates resistances and current indicators.

    Parameters:
    R (np.ndarray): 2D array with resistances and current flow indicators.

    Returns:
    Tuple: (i, r, totalLoop) - current flow indicators, resistor values, and number of loops.
    """
    r = R[0, :]
    i = R[1:, :].astype(bool)
    totalLoop = R.shape[0] - 1
    return i, r, totalLoop

def myMesh(V, R):
    """
    Computes the current I on every loop of a mesh circuit.

    Parameters:
    V (np.ndarray): Column vector of voltage sources on each loop.
    R (np.ndarray): 2D array representing resistances and current indicators.

    Returns:
    np.ndarray: Column vector of the computed current on each loop.
    """
    i, r, M = separateIR(R)
    Rmat = np.zeros((M, M))
    
    for m in range(M):
        for n in range(M):
            indI = np.logical_and(i[m, :], i[n, :])
            if n != m:
                Rmat[m, n] = -np.sum(r[indI])
            else:
                Rmat[m, n] = np.sum(r[indI])
                
    I = np.linalg.solve(Rmat, V)
    return I
