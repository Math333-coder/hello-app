import streamlit as st

# Page Configuration
st.set_page_config(page_title="Mathavan G | Python Developer", page_icon="💻", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
/* Main background */
.stApp {
    background-color: #0f172a;
    color: white;
}

/* Remove default padding */
.block-container {
    padding-top: 2rem;
}

/* Title styling */
h1 {
    color: #38bdf8;
    text-align: center;
}

/* Section headers */
h2 {
    color: #facc15;
    border-bottom: 2px solid #38bdf8;
    padding-bottom: 5px;
}

/* Subheaders */
h3 {
    color: #4ade80;
}

/* Contact links */
a {
    color: #38bdf8;
    text-decoration: none;
    font-weight: bold;
}

a:hover {
    color: #facc15;
}

/* Card effect */
.card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 15px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("<h1>MATHAVAN G</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center;'>Python Developer</h3>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center;'>
📞 6374950532 | 
📧 mathavaannavy@gmail.com | 
<a href='https://github.com/Math333-coder' target='_blank'>GitHub</a> | 
<a href='https://www.linkedin.com/in/mathavan-g-5344b5299' target='_blank'>LinkedIn</a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------- PROFILE ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.header("👨‍💻 Profile")
st.write("""
Motivated MCA graduate (2025) seeking an entry-level Python Developer role. 
Skilled in Python, SQL, and data analytics with strong backend development knowledge. 
Passionate about building scalable and efficient real-world applications.
""")
st.markdown("</div>", unsafe_allow_html=True)

# ---------- EDUCATION ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.header("🎓 Education")

st.subheader("Master of Computer Applications (2023 – 2025)")
st.write("Hindustan College of Arts and Science")
st.write("Affiliated to Bharathiar University")
st.write("CGPA: 7.8")

st.subheader("Bachelor of Computer Science (2020 – 2023)")
st.write("Sri S. Ramaswamy Naidu Memorial College")
st.write("Affiliated to Madurai Kamaraj University")
st.write("CGPA: 6.8")

st.markdown("</div>", unsafe_allow_html=True)

# ---------- SKILLS ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.header("🛠 Technical Skills")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Programming")
    st.write("✔ Python")
    st.write("✔ MySQL")

with col2:
    st.subheader("Tools & Technologies")
    st.write("✔ Excel")
    st.write("✔ Power BI")
    st.write("✔ Problem Solving")

st.markdown("</div>", unsafe_allow_html=True)

# ---------- PROJECTS ----------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.header("🚀 Projects")

st.subheader("📊 Sales Analytics Dashboard (Power BI)")
st.write("""
• Regional sales analysis  
• Product-wise revenue tracking  
• Profit trend analysis  
• Customer behavior insights  
• KPI-based data-driven decisions  
""")

st.subheader("📈 Dynamic Retail Dashboard (Excel)")
st.write("""
• Sales & Profit analysis  
• Discount & Quantity tracking  
• Segment & Category performance  
• Market & Region insights  
""")

st.markdown("</div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("<center>© 2026 Mathavan G | Python Developer</center>", unsafe_allow_html=True)
