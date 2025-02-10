import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="Suvin Singh",
    icon="👀",
    default=True,
)
# project_1_page = st.Page(
#     "views/sales_dashboard.py",
#     title="Sales Dashboard",
#     icon=":material/bar_chart:",
# )
# project_2_page = st.Page(
#     "views/chatbot.py",
#     title="Chat Bot",
#     icon=":material/smart_toy:",
# )


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        # "Projects": [project_1_page, project_2_page],
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")
# st.sidebar.markdown("Get In Touch")
# st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/suvin-singh/)")
# st.sidebar.markdown("[GitHub](https://github.com/prosuvinhere)")


# --- RUN NAVIGATION ---
pg.run()
