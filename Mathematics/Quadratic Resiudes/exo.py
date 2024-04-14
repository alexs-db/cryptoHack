def is_quadratic_residue(x, p):
    """Check if x is a quadratic residue modulo p."""
    for a in range(1, p):
        if (a ** 2) % p == x:
            return True
    return False

def quadratic_residues(p):
    """Find all quadratic residues modulo p."""
    residues = []
    for x in range(1, p):
        if is_quadratic_residue(x, p):
            residues.append(x)
    return residues

# Exemple d'utilisation avec p = 29
p = 29
residues_mod_29 = quadratic_residues(p)
print("Les résidus quadratiques modulo", p, "sont :", residues_mod_29)
