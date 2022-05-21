===Mathematische Äquivalente===

Unter der Annahme {{tmath|x \geq y}} können die bitweisen Operationen für die nicht negativen ganzen Zahlen wie folgt geschrieben werden:

:<math>\begin{align}
   \operatorname{NOT}x &= \sum_{n=0}^{\lfloor\log_2(x)\rfloor} 2^n\left[\left(\left\lfloor\frac{x}{2^n} \right\rfloor \bmod 2 + 1\right) \bmod 2\right] = 2^{\left\lfloor\log_2(x)\right\rfloor + 1} - 1 - x
\\
  x\operatorname{AND}y &= \sum_{n=0}^{\lfloor\log_2(x)\rfloor} 2^n\left(\left\lfloor\frac{x}{2^n}\right \rfloor \bmod 2\right)\left(\left\lfloor\frac{y}{2^n}\right\rfloor \bmod 2\right)
\\
   x\operatorname{OR}y &= \sum_{n=0}^{\lfloor\log_2(x)\rfloor} 2^n\left(\left[\left(\left\lfloor\frac{x}{ 2^n}\right\rfloor \bmod 2\right) + \left(\left\lfloor\frac{y}{2^n}\right\rfloor \bmod 2\right) + \left(\left\lfloor \frac{x}{2^n}\right\rfloor \bmod 2\right)\left(\left\lfloor\frac{y}{2^n}\right\rfloor \bmod 2\right)\right] \bmod 2\right)
\\
  x\operatorname{XOR}y &=
    \sum_{n=0}^{\lfloor\log_2(x)\rfloor} 2^n\left(\left[\left(\left\lfloor\frac{x}{2^n}\right\rfloor \ bmod 2\right) + \left(\left\lfloor\frac{y}{2^n}\right\rfloor \bmod 2\right)\right]\bmod 2\right) =
    \sum_{n=0}^{\lfloor\log_2(x)\rfloor} 2^n\left[\left(\left\lfloor\frac{x}{2^n}\right\rfloor + \left\ lfloor\frac{y}{2^n}\right\rfloor\right) \bmod 2\right]
\end{align}</math>
