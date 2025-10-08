# Lecture de fond : Cryptographie à courbes elliptiques (ECC)

L’Elliptic Curve Cryptography (ECC) est un protocole cryptographique asymétrique basé sur des courbes elliptiques. Il utilise une opération appelée **addition de points**, qui permet de définir un groupe abélien. La sécurité repose sur la difficulté de retrouver un nombre à partir d’une multiplication scalaire de points.

Sur une courbe elliptique, l’addition de deux points se fait en traçant une ligne entre eux, trouvant le troisième point d’intersection, puis en le réfléchissant. Si on additionne un point avec lui-même, on utilise la tangente. Il existe aussi un **point à l’infini** qui sert d’élément neutre.

Une courbe elliptique est définie par l’équation de Weierstrass :

```math
Y^2 = X^3 + aX + b
```

avec une condition sur `a` et `b` pour éviter les singularités.

En ECC, on travaille souvent sur des **champs finis**, donc les coordonnées sont des entiers modulo `p`.

---

**Réponse à donner :**  
`crypto{Abelian}`