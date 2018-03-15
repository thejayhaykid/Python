def inchesToMetersConv(n_in):
    n_m = n_in * 0.0254
    return n_m

print inchesToMetersConv(12)
print inchesToMetersConv(39.37007874)

def CelToFahrConv(deg_cel):
    deg_fahr = (deg_cel * 9) / 5 + 32
    return deg_fahr

print CelToFahrConv(0)
print CelToFahrConv(100)
