import streamlit as st

def math_riddle_factory():
    st.subheader("Math Riddle Factory")
    riddle = st.text_input("Enter a math riddle:")
    solution = st.text_input("Enter the answer:")
    if st.button("Generate Riddle"):
        if riddle and solution:
            st.write(f"**Riddle:** {riddle}")
            st.write(f"**Solution:** {solution}")
        else:
            st.warning("Please enter both a riddle and a solution.")

def math_meme_repair():
    st.subheader("Math Meme Repair")
    wrong_meme = st.text_input("Enter an incorrect math meme:")
    correct_answer = st.text_input("Enter the correct explanation:")
    if st.button("Fix Meme"):
        if wrong_meme and correct_answer:
            st.write(f"**Incorrect Meme:** {wrong_meme}")
            st.write(f"**Corrected Explanation:** {correct_answer}")
        else:
            st.warning("Please enter both an incorrect meme and a correction.")

def creative_math_solver():
    st.subheader("Creative Math Problem Solver")
    problem = st.text_input("Enter an emoji-based math problem:")
    solution = st.text_input("Enter the solution:")
    if st.button("Solve Problem"):
        if problem and solution:
            st.write(f"**Problem:** {problem}")
            st.write(f"**Solution:** {solution}")
        else:
            st.warning("Please enter both a problem and a solution.")

st.title("Math AI Assignment")

option = st.sidebar.selectbox("Select a Function", ["Math Riddle Factory", "Math Meme Repair", "Creative Math Solver"])

if option == "Math Riddle Factory":
    math_riddle_factory()
elif option == "Math Meme Repair":
    math_meme_repair()
elif option == "Creative Math Solver":
    creative_math_solver()
