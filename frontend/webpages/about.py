import streamlit as st
from backend.modules.css import load_css

# Load custom CSS
st.markdown(load_css(r'frontend/styles.css'), unsafe_allow_html=True)

st.title("What is CineQuiz?")
st.write("CineQuiz is a movie quiz, where you can test your knowledge on movies and their details.")
st.subheader("Our Team:")
st.markdown(
    """
    <p align="center">
        <a href="https://github.com/cipher-shad0w" target="_blank">Cipher Shadow</a>
        <a href="https://github.com/arvedb" target="_blank">Arved Bahde</a>
        <a href="https://github.com/mirixy" target="_blank">Miriam</a>
    </p>
    """, unsafe_allow_html=True
)
st.divider()
st.markdown("""

# CineQuiz

Welcome to the Streamlit app that utilizes the [Open OMDb API](http://www.omdbapi.com) This project was created for a mini hackathon organized by Kevin Chromik.

## Where to play?
[CineQuiz](https://cinequiz.streamlit.app)


## Demo

Coming soon

## Contributors

- [mirixy](https://github.com/mirixy)
- [cipher-shad0w](https://github.com/cipher-shad0w)
- [arvedb](https://github.com/arvedb)

## Features

- User-friendly UI.
- Score System, but it resets everytime if you start a new quiz session.
- If the movie has a poster, it will display the poster in the question cards.



## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mirixy/CineQuiz.git
   cd CineQuiz
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

3. **Press the Start Button.**

## Project Structure

- `app.py`: Main file to run the Streamlit app.
- `requirements.txt`: List of Python dependencies.

## Technologies Used

- [Streamlit](https://streamlit.io/): Framework for creating interactive web applications.
- [Open OMDb API](http://www.omdbapi.com)

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

Special thanks to Kevin Chromik for organizing the mini hackathon.

---

If you have any questions or need further assistance, please feel free to contact any of the contributors.

Happy coding!""")