import streamlit as st

# Custom CSS for title and subtitle
st.markdown("""
    <style>
    .main-title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: white;
    }
    .subtitle {
        font-size: 20px;
        font-weight: normal;
        text-align: center;
        color: #666666;
        margin-top: -20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Display title and subtitle
st.markdown('<h1 class="main-title">ParseMate</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Your AI partner in web scraping</p>', unsafe_allow_html=True)

# Web scraping input and functions
url = st.text_input('Enter a website URL:')
from scrape import scrape_website, clean_bodycontent, extract_bodycontent, split_domcontent
from parse import parse_with_ollama

# Scrape the website
if st.button("Scrape Site"):
    st.write("Scraping the site...")
    result = scrape_website(url)
    body_content = extract_bodycontent(result)
    cleaned_content = clean_bodycontent(body_content)
    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", cleaned_content, height=300)

# Parsing the content
if "dom_content" in st.session_state:
    parse_description = st.text_area('Describe what you want to parse:')

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            dom_chunks = split_domcontent(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)
