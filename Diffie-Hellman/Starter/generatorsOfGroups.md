Nous pouvons utiliser le théorème suivant issu de la théorie des corps :

> Supposons que $p > 2$ soit un nombre premier et $\alpha \in \mathbb{Z}_p^*$.  
> Alors $\alpha$ est un élément primitif modulo $p$ si et seulement si  
> $\alpha^{\frac{p-1}{q}} \not\equiv 1 \pmod{p}$ pour tout nombre premier $q$ tel que $q \mid (p-1)$.  
> *(D. R. Stinson, "Cryptographie : Théorie et Pratique", Théorème 5.8)*

Voici un exemple de code Python pour trouver le plus petit élément primitif modulo $p$ :

```python
from primefac import primefac

p = 28151
totient = p - 1 
facteurs_totient = set(primefac(totient))

for candidat in range(2, p):
    est_primitif = True

    for facteur in facteurs_totient:
        exp = totient // facteur
        puissance = pow(candidat, exp, p)
        print(f'Candidat : {candidat}, facteur : {facteur}, résultat : {puissance}')

        if puissance == 1:
            est_primitif = False
            break

    if est_primitif:
        print(f'\nPrimitif trouvé :\n{candidat} est le plus petit élément primitif pour p={p}\na^((p-1)/q) != 1 mod p pour chaque nombre premier q : q|(p-1)')
        break
```