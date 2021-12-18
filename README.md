
# Snowflake Animation Inside Streamlit

Within the **style** directory you will find the **style.css** containg the snowflakes animation.
Example on injecting the CSS code into your streamlit app:

```
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")

# Load Animation
animation_symbol = "❄"

st.markdown(
    f"""
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    <div class="snowflake">{animation_symbol}</div>
    """,
    unsafe_allow_html=True,
)
```

## Demo

[![Demo](https://raw.githubusercontent.com/Sven-Bo/happy-holidays-streamlit-app/master/demo.gif)


## Author

- Sven from Coding Is Fun
- YouTube: https://youtube.com/c/CodingIsFun
- Website: https://pythonandvba.com


## Feedback

If you have any feedback, please reach out to me at contact@pythonandvba.com


![Logo](https://content.screencast.com/users/jubbel3/folders/Snagit/media/c42ea34b-4057-4754-96b0-e8e05c866afb/08.18.2021-19.56.png)

