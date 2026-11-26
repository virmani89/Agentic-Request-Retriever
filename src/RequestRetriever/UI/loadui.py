import streamlit as st

from src.RequestRetriever.Main import run_agent
from src.RequestRetriever.UI.display_result import display_result
from src.RequestRetriever.UI.uiconfigfile import Config


def load_ui():

    config = Config()

    st.set_page_config(
        page_title=config.PAGE_TITLE,
        page_icon=config.PAGE_ICON,
        layout=config.LAYOUT
    )

    st.title(config.PAGE_TITLE)
    st.write(config.APP_DESCRIPTION)
    st.divider()

    user_query = st.text_input(
        config.INPUT_LABEL,
        placeholder=config.INPUT_PLACEHOLDER
    )

    if st.button(config.BUTTON_NAME):

        if not user_query.strip():
            st.warning("Please enter your query first.")

        else:
            with st.spinner("Searching for matching request..."):

                result = run_agent(user_query)

                display_result(result)