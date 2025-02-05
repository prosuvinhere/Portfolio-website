import streamlit as st

# Page Configuration
st.set_page_config(page_title="Suvin Singh", page_icon="🚀", layout="centered")

# Header
st.title("Suvin Singh")
st.write("Email: suvinsingh2003@gmail.com | Mob: +91 8830545823")
st.write("[GitHub](https://github.com/prosuvinhere) | [LinkedIn](https://linkedin.com/in/suvin-singh/)")

# Sidebar for Navigation
section = st.sidebar.radio("Navigation", ["Home", "Skills", "Work Experience", "Education", "Projects", "Publications & Certifications", "Positions of Responsibility"])

if section == "Home":
    st.header("Welcome to My Portfolio!")
    st.write("This interactive portfolio showcases my skills, experience, and projects. Use the sidebar to navigate!")

elif section == "Skills":
    st.header("Skills")
    st.write("**ML:** Google Palm, LangChain, Hugging Face, ChromaDB, Streamlit, Llama3.1")
    st.write("**DSA:** Java")

elif section == "Work Experience":
    st.header("Work Experience")
    st.subheader("TMEIC, Hyderabad (Aug 2023 - Oct 2023)")
    st.write("**ML Intern Developer**")
    st.write("- Developed an IT support chatbot using Large Language Models (LLM), achieving 98% accuracy in issue resolution.")
    st.write("- Implemented automation for IT support tasks, improving support efficiency by 83%.")
    st.write("- Utilized LangChain and HuggingFaceEmbeddings for a responsive chatbot.")

elif section == "Education":
    st.header("Education")
    st.write("**VIT Vellore (Aug 2021 - Jun 2025)**")
    st.write("B.Tech. in Computer Science and Engineering | CGPA: 8.59/10")
    st.write("**City International School, Pune (2019 - 2021)**")
    st.write("Central Board of Secondary Education (PCM - 12th) | CGPA: 8.30/10")
    st.write("**Vikhe Patil Memorial School, Pune (2015 - 2019)**")
    st.write("Central Board of Secondary Education (10th) | CGPA: 8.48/10")

elif section == "Projects":
    st.header("Projects")
    project = st.selectbox("Select a Project", ["SQLTranslator", "URL2Email"])
    
    if project == "SQLTranslator":
        st.subheader("SQLTranslator")
        st.write("A system that converts human language queries into SQL statements.")
        st.write("**Tech:** Streamlit, Google Palm LLM, Hugging Face, LangChain")
        st.write("[GitHub](https://github.com/prosuvinhere/SQLTranslator)")
    elif project == "URL2Email":
        st.subheader("URL2Email")
        st.write("Scrapes job descriptions from URLs to generate personalized cold emails.")
        st.write("**Tech:** Llama3.1, ChromaDB, LangChain, Streamlit")
        st.write("[GitHub](https://github.com/prosuvinhere/URL2Email)")

elif section == "Publications & Certifications":
    st.header("Publications & Certifications")
    st.write("**AWS Certified Solutions Architect–Associate (869/1000)**")
    st.write("Expertise in designing distributed systems on AWS.")
    st.write("**A Comparative Analysis of Web** (Inderscience Publishers)")
    st.write("Comparative analysis of Web 3.0, Web 2.0, and Web 1.0.")

elif section == "Positions of Responsibility":
    st.header("Positions of Responsibility")
    st.write("- **Volunteer | VIT Cultural Fest (Rivera 23):** Managed 10+ international students.")
    st.write("- **Sports:** Organized 50+ sports events.")
    st.write("- **Finance & Stalls:** Handled event finances and 100+ stall operations.")

# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit")
