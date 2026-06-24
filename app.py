import streamlit as st
import sympy as sp

st.set_page_config(page_title="Newton-Raphson Solver", page_icon="📈")

st.title("📈 Newton-Raphson Method Solver")
st.write("Find roots of equations using iteration method")

# symbol
x = sp.Symbol('x')

# input function
func_input = st.text_input("Enter function f(x) (use x as variable)", "x**2 - 4")

if func_input:
    f = sp.sympify(func_input)
    df = sp.diff(f, x)

    f_num = sp.lambdify(x, f)
    df_num = sp.lambdify(x, df)

    st.latex(f"f(x) = {sp.latex(f)}")
    st.latex(f"f'(x) = {sp.latex(df)}")

    x0 = st.number_input("Enter initial guess x0", value=1.0)
    n = st.number_input("Number of iterations", min_value=1, max_value=50, value=5)

    if st.button("Run Newton-Raphson"):

        st.write("### Iteration Steps")

        for i in range(1, int(n) + 1):
            fx = f_num(x0)
            dfx = df_num(x0)

            if dfx == 0:
                st.error("Derivative became zero. Stop iteration.")
                break

            x1 = x0 - fx / dfx

            st.write(f"Iteration {i}: x = {x1}")

            x0 = x1

        st.success(f"Final root approximation: {x0}")