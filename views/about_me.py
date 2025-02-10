import streamlit as st

from forms.contact import contact_form

@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile_image.png", width=230)

with col2:
    st.title("Suvin Singh", anchor=False)
    st.write(
        'Analytics Specialist | Audit & Assurance at Deloitte USI | Driving Insights Through Data'
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()
    
    # Social Media Badges
    st.markdown(
        """
        [![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/prosuvinhere)
        [![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/suvin-singh)
        [![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/_suvin_singh/)
        """
    )

# --- EXPERIENCE & EDUCATION ---
st.write("\n")
st.subheader("💼 Professional Experience & 🎓 Education", anchor=False)
st.write(
    """
    - **Data Analyst** | Deloitte USI  
    - **Python Developer** | Prorigo  
    - **ML Developer** | Toshiba Mitsubishi-EIC  
    - **B.Tech in Computer Science** | VIT Vellore  
    """
)

# --- PUBLICATIONS & CERTIFICATIONS ---
st.write("\n")
st.subheader("📚 Publications & 🏅 Certifications", anchor=False)
st.write(
    """
    - **Research Paper:** *A Comparative Analysis of Web 3.0, Web 2.0, and Web 1.0: Evolution and Implications* | [Read Here](https://www.inderscienceonline.com/doi/10.1504/IJLC.2025.143530)  
    - **AWS Certified Solutions Architect – Associate** | [View Certificate](https://cp.certmetrics.com/amazon/en/public/verify/credential/5a537ec94e504bdfb0009ed23ff7390e)  
    - **NPTEL Certifications:**  
      - *Entrepreneurship* | IIT Madras | [Certificate](https://archive.nptel.ac.in/content/noc/NOC23/SEM2/Ecertificates/110/noc23-mg74/Course/NPTEL23MG74S74510399320410893.pdf)  
      - *Forests and Their Management* | IIT Kanpur | [Certificate](https://archive.nptel.ac.in/content/noc/NOC24/SEM1/Ecertificates/102/noc24-bt23/Course/NPTEL24BT23S56980118630759409.pdf)  
      - *Wildlife Ecology* | IIT Kanpur | [Certificate](https://archive.nptel.ac.in/content/noc/NOC24/SEM2/Ecertificates/102/noc24-bt59/Course/NPTEL24BT59S205381087604423167.pdf)  
    """
)

# --- ACHIEVEMENTS & LEADERSHIP ---
st.write("\n")
st.subheader("🏆 Achievements & 🛠️ Leadership", anchor=False)
st.write(
    """
    - **Secured the highest package** at Deloitte USI among VIT Vellore placements  
    - **Maharashtra Science Talent Search Exam (MSTSE) 2019** – Ranked **59th**  
    - **VIT Cultural Fest (Rivera '23):**  
      - *GuestCare:* Managed **10+ international students**  
      - *Sports:* Organized **50+ sports events**  
      - *Finance & Stalls:* Handled event finances and **100+ stall operations**  
    - **VIT Cultural Fest (Rivera '25):**  
      - *Sponsorship:* Secured **5+ sponsors**, raising over **₹1.5L+**  
    """
)
