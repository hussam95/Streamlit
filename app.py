from math import factorial
import streamlit as st
import math

st.title('Factorial Program')

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))

number_ = st.number_input('Insert a number',min_value=-100,max_value=100,step=1)
number=int(number_)
if number < 0:
   st.write("Sorry, factorial does not exist for negative numbers")
elif number == 0:
   st.write("The factorial of 0 is 1")
else:
   out=factorial(number)
   st.write(f"The factorial of",number,"is",out)

pipreqs