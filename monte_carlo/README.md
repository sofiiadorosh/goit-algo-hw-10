# 🧮 Integral Calculation Using the Monte Carlo Method

This project demonstrates the calculation of a definite integral for the function $f(x) = x^2$ on the interval $[0, 2]$ using the **Monte Carlo method**.

## 1. 📝 Problem Statement
The goal is to calculate the area under the curve $f(x) = x^2$ from $x=0$ to $x=2$. 
Analytically, this is calculated as:
$$\int_{0}^{2} x^2 dx = \left[ \frac{x^3}{3} \right]_0^2 = \frac{8}{3} \approx 2.6667$$

## 2. ⚙️ Methodology
The Monte Carlo method uses a stochastic (probabilistic) approach:
1.  **Define a Bounding Box**: Create a rectangle that encloses the function area. For $x \in [0, 2]$, the maximum height is $f(2) = 4$.
2.  **Generate Random Points**: Generate $N$ random coordinates $(x_i, y_i)$ within this rectangle.
3.  **Check Condition**: Determine if the point lies below the curve ($y_i \le x_i^2$).
4.  **Calculate Area**: The integral is estimated by multiplying the total area of the rectangle by the fraction of points that fell under the curve.

## 3. ⚖️ Results Comparison
Based on a simulation with 100,000 points:

| Method | Result | Description |
| :--- | :--- | :--- |
| **Analytical** | 2.6667 | The exact mathematical solution. |
| **SciPy `quad`** | 2.6667 | High-precision numerical integration (standard). |
| **Monte Carlo** | ~2.6658 | Stochastic approximation (varies slightly each run). |

## 4. ✅ Conclusions

1.  **Accuracy**: The Monte Carlo method provides a reliable approximation. While it is less precise than the `quad` function for simple 1D functions, its accuracy increases as more points ($N$) are added.
2.  **Convergence**: The error decreases at a rate of $1/\sqrt{N}$, meaning to double the precision, you need four times as many points.
3.  **The "Curse of Dimensionality"**: The true strength of Monte Carlo integration is revealed in **multi-dimensional calculus**. Traditional methods (like the Trapezoidal rule) become extremely slow as dimensions increase, whereas Monte Carlo's efficiency remains relatively stable.
4.  **Practical Application**: This method is widely used in computational physics, financial modeling (risk analysis), and AI, where functions are often too complex to solve analytically.