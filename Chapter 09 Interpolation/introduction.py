from scipy.interpolate import interp1d

# Define the interpolation function
f = interp1d(x, v, kind=method)

# Interpolated values at xq
vq = f(xq)
