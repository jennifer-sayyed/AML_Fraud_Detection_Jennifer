import streamlit as st

from chatbot import generate_response

st.set_page_config(
    page_title="AML Fraud Co-Pilot"
)

st.title(
    "AML & Fraud Detection Co-Pilot"
)

query = st.text_area(
    "Ask a Banking Question"
)

if st.button(
    "Submit"
):

    result = generate_response(
        query
    )

    st.json(
        result.model_dump()
        if hasattr(result, "model_dump")
        else result
    )