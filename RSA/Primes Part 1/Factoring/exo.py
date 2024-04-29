from sympy import factorint

n = 510143758735509025530880200653196460532653147

factors = factorint(n)
smaller_prime = min(factors.keys())

print("The smallest prime is :", smaller_prime)
