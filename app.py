books = [
"Chemistry book"
"The Hobbit"
"The Great Gatsby"
"1984"
"Pride and Prejudice"
]

st.title("Book Checker App")
st.write("Enter a book title to check if it exists in the database.")

user_input = st.text_input("Book Title")

if st.button("Check Book"):
  if user_input.strip() == "":
    st.warning("Please enter a book title")
  elif user_input in books:
    st.success("The book exists in database!")
  else:
    st.error("The book is NOT in database!")



