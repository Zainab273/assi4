import streamlit as st

# Page config
st.set_page_config(page_title="My Website", page_icon="🌐", layout="centered")

# Header
st.title("👋 Welcome to My Portfolio Website")
st.subheader("Hi, I'm Mehma! A Developer & Creative Thinker")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go To", ["Home", "About", "Projects", "Contact"])

# ------------------ PAGE: HOME ------------------
if page == "Home":
    st.markdown("""
    # 👋 Welcome to My Digital Space

    Hi, I'm **MehmaRashid123** — a passionate developer, designer, and tech enthusiast.

    🔧 I specialize in building modern web applications with tools like:
    - Next.js
    - Sanity CMS
    - Streamlit
    - OpenAI API

    🎯 My goal is to create seamless, intelligent, and visually stunning digital experiences.

    ---
    ## 🚀 What You'll Find Here
    - 💼 My latest **projects**
    - 🧠 Insights on **AI, tech, and creativity**
    - 🔐 Tools like a **secure data encryption app**
    - ✨ And much more coming soon...

    📫 **Let's Connect:**  
    Feel free to reach out if you’d like to collaborate or just say hi!
    """)

# ------------------ PAGE: ABOUT ------------------
elif page == "About":
    st.markdown("""
    ## 🧠 About Me

    I'm passionate about building web apps, exploring AI, and creating animations.  
    Currently working on:
    - 🔹 Streamlit
    - 🔹 Sanity CMS
    - 🔹 Next.js
    - 🔹 OpenAI tools
    
    I love crafting modern, minimal, and functional digital solutions that make life easier and more fun!
    """)

# ------------------ PAGE: PROJECTS ------------------
elif page == "Projects":
    st.markdown("## 💼 My Projects")

    projects = {
        "🔐 Secure Data App": "A Streamlit app with encryption & hashed passkey.",
        "🛋️ Furniture Store": "E-commerce website with Sanity + Next.js.",
        "🤖 AI Blog": "AI-powered blog using OpenAI, Sanity, and MongoDB."
    }

    for project, desc in projects.items():
        st.markdown(f"**{project}**  \n{desc}\n")

# ------------------ PAGE: CONTACT ------------------
elif page == "Contact":
    st.markdown("## 📬 Contact Me")

    contact_form = """
    <form action="https://formsubmit.co/YOUR_EMAIL_HERE" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here..." required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Add some basic CSS
    st.markdown("""
    <style>
    input, textarea {
        width: 100%;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ccc;
        margin-bottom: 10px;
    }
    button {
        padding: 10px 20px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 8px;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)
