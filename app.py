import streamlit as st
st.title("power Calculator")
st.write("enter a number to calculate its square , cube and fith power")

n=st.number_input("Enter a number", value=1.0, step=1.0)

square = n**2
cube = n**3
fifth_power = n**5

st.write(f"Square of {n} is {square}")
st.write(f"Cube of {n} is {cube}")
st.write(f"Fifth power of {n} is {fifth_power}")