# Calcul de l'inverse modulaire dans un corps fini F_p

Dans le cadre du protocole de Diffie-Hellman, on travaille dans un corps fini F_p, où p est un nombre premier. Cela garantit que chaque élément non nul a un inverse multiplicatif.

## 🎯 Objectif

Trouver l'inverse de :

- g = 209  
- modulo p = 991 (nombre premier)

On cherche donc un entier d tel que :

    209 * d ≡ 1 mod 991

---

## 🧠 Théorie : Inverse modulaire

L'inverse modulaire de a modulo m est le nombre x tel que :

    a * x ≡ 1 mod m

Il existe si et seulement si pgcd(a, m) = 1, ce qui est le cas ici car 209 et 991 sont premiers entre eux.

---

## ⚙️ Méthode : Algorithme d’Euclide Étendu

L’algorithme d’Euclide étendu permet de trouver deux entiers x et y tels que :

    a * x + m * y = pgcd(a, m)

Ici, on a :

    209 * x + 991 * y = 1

Le coefficient x est l’inverse modulaire recherché.

---

## 💻 Implémentation Python

```python
def modinv(a, m):
    t, new_t = 0, 1
    r, new_r = m, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    return t % m

# Exemple :
inverse = modinv(209, 991)
print(inverse)  # Résultat : 569
````

---

## ✅ Résultat

L'inverse de 209 modulo 991 est :

```
569
```

Vérification :

```
209 * 569 = 118921
118921 mod 991 = 1
```