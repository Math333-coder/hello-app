import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Mathavan G | Python Developer",
    page_icon="💻",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#020617,#0f172a,#1e293b);
color:white;
font-family: 'Segoe UI';
}

/* HERO */

.hero{
text-align:center;
padding:20px;
}

.hero h1{
color:#38bdf8;
font-size:50px;
}

.hero h3{
color:#4ade80;
}

/* CARD */

.card{
background:#1e293b;
padding:30px;
border-radius:15px;
box-shadow:0 0 20px rgba(0,0,0,0.5);
margin-top:20px;
}

/* PROJECT CARD */

.project{
background:#0f172a;
padding:20px;
border-radius:12px;
border:1px solid #334155;
transition:0.3s;
}

.project:hover{
transform:scale(1.03);
border:1px solid #38bdf8;
}

footer{
text-align:center;
margin-top:40px;
color:#94a3b8;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR NAVIGATION ----------------
st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Profile", "Education", "Skills", "Projects", "Contact"]
)

# ---------------- HERO SECTION ----------------
col1, col2 = st.columns([3,1])

with col1:
    st.markdown("""
<div class="hero">

<h1>MATHAVAN G</h1>
<h3>Python Developer</h3>

📞 6374950532  
📧 mathavaannavy@gmail.com  

<a href="https://github.com/Math333-coder">GitHub</a> |
<a href="https://www.linkedin.com/in/mathavan-g-5344b5299">LinkedIn</a>

</div>
""", unsafe_allow_html=True)

with col2:
    try:
        st.image("photo.jpeg", width=200)
    except:
        st.warning("Profile photo not found")

st.markdown("---")

# ---------------- PROFILE ----------------
if page == "Profile":

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.header("👨‍💻 Profile")

    st.write("""
Motivated **MCA Graduate (2025)** seeking an entry-level **Python Developer role**.

Strong knowledge in:

• Python Programming  
• SQL & Databases  
• Power BI Analytics  
• Data Visualization  
• Backend Development  

Passionate about building **scalable real-world applications and analytics solutions**.
""")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- EDUCATION ----------------
elif page == "Education":

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.header("🎓 Education")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Master of Computer Applications")
        st.write("2023 – 2025")
        st.write("Hindustan College of Arts and Science")
        st.write("Affiliated to Bharathiar University")
        st.success("CGPA : 7.8")

    with col2:
        st.subheader("Bachelor of Computer Science")
        st.write("2020 – 2023")
        st.write("Sri S. Ramaswamy Naidu Memorial College")
        st.write("Affiliated to Madurai Kamaraj University")
        st.write("Affiliated to Madurai Kamaraj University")
        st.success("CGPA : 6.8")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- SKILLS ----------------
elif page == "Skills":

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.header("🛠 Technical Skills")

    skills = {
        "Python":90,
        "MySQL":80,
        "Power BI":75,
        "Excel":70,
        "Data Analytics":80,
        "Problem Solving":85
    }

    for skill,value in skills.items():
        st.subheader(skill)
        st.progress(value)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- PROJECTS ----------------
elif page == "Projects":

    st.header("🚀 Projects")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='project'>", unsafe_allow_html=True)

        st.subheader("📊 Sales Analytics Dashboard")

        st.write("""
Power BI dashboard that provides:

• Regional sales analysis  
• Product performance tracking  
• Profit trend insights  
• KPI based decision support
""")

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='project'>", unsafe_allow_html=True)

        st.subheader("📈 Dynamic Retail Dashboard")

        st.write("""
Excel based analytics dashboard:

• Sales & profit tracking  
• Segment performance  
• Region insights  
• Discount analysis
""")

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")

    st.subheader("💻 GitHub Repository")
    st.markdown("🔗 https://github.com/Math333-coder")

# ---------------- CONTACT ----------------
elif page == "Contact":

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.header("📬 Contact Me")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")

    if st.button("Send Message"):

        if name and email and message:
            st.success("Message sent successfully!")
        else:
            st.warning("Please fill all fields")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- RESUME DOWNLOAD ----------------
st.markdown("---")

try:
    with open("Mathavan_Resume.pdf","rb") as file:
        st.download_button(
            "📄 Download Resume",
            file,
            "Mathavan_G_Resume.pdf"
        )
except:
    st.info("Upload Mathavan_Resume.pdf in the same folder")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("<footer>© 2026 Mathavan G | Python Developer</footer>", unsafe_allow_html=True)
