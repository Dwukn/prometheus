# Addition and multiplication of Asymptotic

### 1. **Big O (O)**: Upper Bound
- **Addition**: \( O(f(n)) + O(g(n)) = O(\max(f(n), g(n))) \)
- **Multiplication**: \( O(f(n)) · O(g(n)) = O(f(n) · g(n)) \)

### 2. **Big Omega (Ω)**: Lower Bound
- **Addition**: \( Ω(f(n)) + Ω(g(n)) = Ω(\min(f(n), g(n))) \)
- **Multiplication**: \( Ω(f(n)) · Ω(g(n)) = Ω(f(n) · g(n)) \)

### 3. **Big Theta (Θ)**: Tight Bound
- **Addition**: \( Θ(f(n)) + Θ(g(n)) = Θ(\max(f(n), g(n))) \)
- **Multiplication**: \( Θ(f(n)) · Θ(g(n)) = Θ(f(n) · g(n)) \)

---

### 1. **Big O (O) Notation**

Big O notation provides an **upper bound** for the growth rate of a function. It is used to describe the worst-case scenario of an algorithm.

- **Addition**: If you add two functions with \( O \)-notation, the larger of the two terms will dominate.
  - Example: \( O(n^2) + O(n) = O(n^2) \)
  - This is because \( n^2 \) grows faster than \( n \) as \( n \) increases.

- **Multiplication**: When multiplying, you simply multiply the two growth rates.
  - Example: \( O(n^2) · O(n) = O(n^3) \)
  - This is because the product of \( n^2 \) and \( n \) gives \( n^3 \).

---

### 2. **Big Omega (Ω) Notation**

Big Omega notation provides a **lower bound** for the growth rate of a function. It describes the best-case scenario or minimum growth rate for an algorithm.

- **Addition**: When adding two functions with \(Ω)-notation, the smaller term will dominate (since you're looking at the minimum growth rate).
  - Example: \( Ω(n^2) + Ω(n) = Ω(n) \)
  - This is because \( n \) is the lower growth rate compared to \( n^2 \).

- **Multiplication**: When multiplying, you multiply the two functions' lower bounds.
  - Example: \( Ω(n^2) · Ω(n) = Ω(n^3) \)
  - This is because the lower bounds are combined by multiplying them.

---

### 3. **Big Theta (Θ) Notation**

Big Theta notation provides a **tight bound** for the growth rate of a function. It describes both the upper and lower bounds, effectively capturing the exact growth rate of a function.

- **Addition**: When adding two functions with \(Θ)-notation, the larger growth rate dominates, just like with Big O.
  - Example: \( Θ(n^2) + Θ(n) = Θ(n^2) \)
  - This is because \( n^2 \) is the dominant term in the sum.

- **Multiplication**: When multiplying, you multiply the two functions' growth rates.
  - Example: \( Θ(n^2) · Θ(n) = Θ(n^3) \)
  - This is because multiplying the two functions gives the result \( n^3 \).

---

### Summary of Addition and Multiplication for All Notations

| **Operation**        | **Big O (O)**      | **Big Omega (Ω)**   | **Big Theta (Θ)**   |
|----------------------|--------------------|---------------------|---------------------|
| **Addition**          | \( O(\max(f(n), g(n))) \) | \( Ω(\min(f(n), g(n))) \) | \( Θ(\max(f(n), g(n))) \) |
| **Multiplication**    | \( O(f(n) · g(n)) \)    | \( Ω(f(n) · g(n)) \)   | \( Θ(f(n) · g(n)) \)   |

---

### Key Points:
- **For Addition**:
  - **Big O**: Take the maximum of the two growth rates.
  - **Big Omega**: Take the minimum of the two growth rates.
  - **Big Theta**: Take the maximum of the two growth rates.

- **For Multiplication**:
  - **Big O**: Multiply the growth rates.
  - **Big Omega**: Multiply the growth rates.
  - **Big Theta**: Multiply the growth rates.

This way, you can handle any combinations of asymptotic notations and simplify them based on the rules for addition and multiplication.
