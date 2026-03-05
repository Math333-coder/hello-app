import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Mathavan G | Python Developer",
    page_icon="💻",
    layout="wide"
)

# ---------- CSS ----------
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#020617,#0f172a,#1e293b);
color:white;
font-family:Arial;
}

.center{
text-align:center;
}

.card{
background:#1e293b;
padding:25px;
border-radius:12px;
box-shadow:0px 0px 15px rgba(0,0,0,0.4);
margin-top:20px;
}

h1{
text-align:center;
color:#38bdf8;
}

h2{
color:#facc15;
}

h3{
color:#4ade80;
}

a{
color:#38bdf8;
text-decoration:none;
font-weight:bold;
}

a:hover{
color:#facc15;
}

.stButton>button{
background:#38bdf8;
color:black;
font-weight:bold;
border-radius:8px;
height:40px;
width:100%;
}

.stButton>button:hover{
background:#facc15;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
col1,col2,col3 = st.columns([3,2,1])

with col1:
    st.markdown("<h1>MATHAVAN G</h1>",unsafe_allow_html=True)
    st.markdown("<h3 class='center'>Python Developer</h3>",unsafe_allow_html=True)

    st.markdown("""
    <div class='center'>
    📞 6374950532 |  
    📧 mathavaannavy@gmail.com  
    <br><br>
    <a href='https://github.com/Math333-coder'>GitHub</a> |
    <a href='https://www.linkedin.com/in/mathavan-g-5344b5299'>LinkedIn</a>
    </div>
    """,unsafe_allow_html=True)

with col3:
    st.image("photo.jpeg",width=170)

st.markdown("---")

# ---------- SESSION STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "Profile"

# ---------- NAVIGATION BUTTONS ----------
col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    if st.button("👨‍💻 Profile"):
        st.session_state.page="Profile"

with col2:
    if st.button("🎓 Education"):
        st.session_state.page="Education"

with col3:
    if st.button("🛠 Skills"):
        st.session_state.page="Skills"

with col4:
    if st.button("🚀 Projects"):
        st.session_state.page="Projects"

with col5:
    if st.button("📬 Contact"):
        st.session_state.page="Contact"

st.markdown("---")

# ---------- PROFILE ----------
if st.session_state.page=="Profile":

    st.markdown("<div class='card'>",unsafe_allow_html=True)

    st.header("Profile")

    st.write("""
Motivated MCA graduate (2025) seeking an entry-level **Python Developer** role.

Skilled in **Python, SQL, Power BI, and Data Analytics** with strong backend development knowledge.

Passionate about building **scalable real-world applications**.
""")

    st.markdown("</div>",unsafe_allow_html=True)

# ---------- EDUCATION ----------
elif st.session_state.page=="Education":

    st.markdown("<div class='card'>",unsafe_allow_html=True)

    st.header("Education")

    st.subheader("Master of Computer Applications (2023 – 2025)")
    st.write("Hindustan College of Arts and Science")
    st.write("Affiliated to Bharathiar University")
    st.write("CGPA: 7.8")

    st.subheader("Bachelor of Computer Science (2020 – 2023)")
    st.write("Sri S. Ramaswamy Naidu Memorial College")
    st.write("Affiliated to Madurai Kamaraj University")
    st.write("CGPA: 6.8")

    st.markdown("</div>",unsafe_allow_html=True)

# ---------- SKILLS ----------
elif st.session_state.page=="Skills":

    st.markdown("<div class='card'>",unsafe_allow_html=True)

    st.header("Technical Skills")

    st.subheader("Python")
    st.progress(90)

    st.subheader("MySQL")
    st.progress(80)

    st.subheader("Power BI")
    st.progress(75)

    st.subheader("Excel")
    st.progress(70)

    st.subheader("Problem Solving")
    st.progress(85)

    st.markdown("</div>",unsafe_allow_html=True)

# ---------- PROJECTS ----------
elif st.session_state.page=="Projects":

    st.markdown("<div class='card'>",unsafe_allow_html=True)

    st.header("Projects")

    st.subheader("📊 Sales Analytics Dashboard (Power BI)")
    st.write("""
• Regional sales analysis  
• Product-wise revenue tracking  
• Profit trend analysis  
• Customer behavior insights  
• KPI-based decision making
""")

    st.subheader("📈 Dynamic Retail Dashboard (Excel)")
    st.write("""
• Sales & Profit analysis  
• Discount & Quantity tracking  
• Segment performance  
• Region-based insights
""")

    st.subheader("💻 GitHub")
    st.write("🔗 github.com/Math333-coder")

    st.markdown("</div>",unsafe_allow_html=True)

# ---------- CONTACT ----------
elif st.session_state.page=="Contact":

    st.markdown("<div class='card'>",unsafe_allow_html=True)

    st.header("Contact Me")

    name=st.text_input("Your Name")
    email=st.text_input("Your Email")
    msg=st.text_area("Message")

    if st.button("Send Message"):
        st.success("Message sent successfully!")

    st.markdown("</div>",unsafe_allow_html=True)

# ---------- RESUME ----------
st.markdown("---")

try:
    with open("Mathavan_Resume.pdf","rb") as file:
        st.download_button(
            "📄 Download Resume",
            file,
            "Mathavan_G_Resume.pdf"
        )
except:
    st.info("Upload resume file to enable download")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("<center>© 2026 Mathavan G | Python Developer</center>",unsafe_allow_html=True)
