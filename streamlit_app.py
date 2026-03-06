import streamlit as st
from PIL import Image

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Mathavan Portfolio",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Custom Background Style
# -----------------------------
st.markdown(
"""
<style>

.stApp {
    background-color: #f4f8fb;
}

.main-title{
font-size:42px;
font-weight:bold;
color:#1f3c88;
}

.sub-title{
font-size:22px;
color:gray;
}

.section-title{
font-size:30px;
font-weight:bold;
color:#1f3c88;
margin-top:20px;
}

</style>
""",
unsafe_allow_html=True
)

# -----------------------------
# Navigation Menu
# -----------------------------
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Home","About","Skills","Projects","Resume","Contact"]
)

# -----------------------------
# HOME
# -----------------------------
if page == "Home":

    col1,col2 = st.columns([1,2])

    with col1:
        try:
            image = Image.open("photo.jpeg")
            st.image(image,width=220)
        except:
            st.write("Upload profile.jpg")

    with col2:
        st.markdown('<p class="main-title">Hi, I\'m Mathavan 👋</p>',unsafe_allow_html=True)
        st.markdown('<p class="sub-title">Data Analyst | Power BI | SQL | Excel</p>',unsafe_allow_html=True)

        st.write("""
I am a **Data Analyst passionate about transforming raw data into meaningful insights**.

I create **interactive dashboards and analytics solutions**
to help businesses make **data-driven decisions**.
""")

# -----------------------------
# ABOUT
# -----------------------------
elif page == "About":

    st.markdown('<p class="section-title">About Me</p>',unsafe_allow_html=True)

    st.write("""
I specialize in **data analysis, visualization and dashboard development**.

I enjoy working with business data and converting it into
**clear and actionable insights** using modern analytics tools.
""")

# -----------------------------
# SKILLS
# -----------------------------
elif page == "Skills":

    st.markdown('<p class="section-title">Skills</p>',unsafe_allow_html=True)

    col1,col2,col3 = st.columns(3)

    with col1:
        st.subheader("📊 Data Visualization")
        st.write("Power BI")
        st.write("Excel Dashboards")

    with col2:
        st.subheader("💻 Data Management")
        st.write("SQL")
        st.write("Data Cleaning")

    with col3:
        st.subheader("📚 Tools")
        st.write("Python")
        st.write("Pandas")
        st.write("Excel")

# -----------------------------
# PROJECTS
# -----------------------------
elif page == "Projects":

    st.markdown('<p class="section-title">Projects</p>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📊 Sales Analytics Dashboard", "📈 Dynamic Retail Dashboard"])

    # -------- PROJECT 1 --------
    with tab1:

        st.subheader("📊 Sales Analytics Dashboard")

        st.write("""
Built an interactive dashboard to analyze business sales performance.
""")

        st.write("""
**Tools Used**
- Power BI
- SQL
- Excel
""")

        st.write("""
**Features**
- Regional sales performance analysis
- Product level sales insights
- KPI metrics such as revenue and profit
- Interactive dashboard filters
""")

        st.write("""
**Insights**
- Identified top performing products
- Sales trends across months
- Regional performance comparison
""")

        st.markdown("GitHub Repository: https://github.com/Math333-coder/Sales-Analytics")

    # -------- PROJECT 2 --------
    with tab2:

        st.subheader("📈 Dynamic Retail Dashboard")

        st.write("""
Developed a dynamic retail dashboard to track and analyze sales data.
""")

        st.write("""
**Tools Used**
- Excel
- Pivot Tables
- Charts
- Slicers
""")

        st.write("""
**Features**
- Interactive dashboard
- Dynamic filtering
- Sales trend visualization
- KPI calculations
""")

        st.write("""
**Insights**
- Monthly sales performance
- Product category comparison
- Retail performance overview
""")

        st.markdown("GitHub Repository: https://github.com/Math333-coder/Dynamic_Retail_Dashboard")
# -----------------------------
# RESUME
# -----------------------------
elif page == "Resume":

    st.markdown('<p class="section-title">Resume</p>',unsafe_allow_html=True)

    try:
        with open("Mathavan_Resume.pdf","rb") as file:
            st.download_button(
                label="📄 Download Resume",
                data=file,
                file_name="Mathavan_Resume.pdf",
                mime="application/pdf"
            )
    except:
        st.info("Add resume.pdf to enable download")

# -----------------------------
# CONTACT
# -----------------------------
elif page == "Contact":

    st.markdown('<p class="section-title">Contact</p>',unsafe_allow_html=True)

    st.write("📧 Email: mathavannavy@gmail.com")
    st.write("💼 LinkedIn: https://linkedin.com/in/yourprofile")
    st.write("💻 GitHub: https://github.com/yourusername")

    st.success("Thanks for visiting my portfolio!")
