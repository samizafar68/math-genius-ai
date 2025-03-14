import streamlit as st

def math_riddle_factory():
    st.subheader("Math Riddle Factory")
    st.write("Generate and display math riddles here.")
    # Example riddle
    riddle = "What number becomes zero when you subtract 15 from half of it?"
    solution = "The number is 30."
    st.write(f"**Riddle:** {riddle}")
    st.write(f"**Solution:** {solution}")

def math_meme_repair():
    st.subheader("Math Meme Repair")
    st.write("Fix incorrect viral math memes.")
    wrong_meme = "8 ÷ 2(2+2) = 1?"
    correct_answer = "16 (Following proper PEMDAS order)"
    st.write(f"**Incorrect Meme:** {wrong_meme}")
    st.write(f"**Corrected Explanation:** {correct_answer}")

def creative_math_solver():
    st.subheader("Creative Math Problem Solver")
    st.write("Solve emoji-based math problems.")
    problem = "🍎 + 🍎 + 🍎 = 12"
    solution = "Each 🍎 = 4"
    st.write(f"**Problem:** {problem}")
    st.write(f"**Solution:** {solution}")

st.title("Math AI Assignment")

option = st.sidebar.selectbox("Select a Function", ["Math Riddle Factory", "Math Meme Repair", "Creative Math Solver"])

if option == "Math Riddle Factory":
    math_riddle_factory()
elif option == "Math Meme Repair":
    math_meme_repair()
elif option == "Creative Math Solver":
    creative_math_solver()
