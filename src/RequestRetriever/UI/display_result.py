import streamlit as st


def display_result(result):

    if result["error"]:

        st.warning(result["error"])

        return

    st.success("Matching Query Found!")

    #st.write("### File Name")

    #st.write(result["file_name"])

    #st.write("### File Location")

    #st.write(result["file_path"])

    #st.write("### Similarity Score")

    #st.write(

     #   f"{result['similarity_score'] * 100:.2f}%"

    # )

    st.write("### File Contents")

    st.text_area(

        "Query Content",

        value=result["file_content"],

        height=400

    )