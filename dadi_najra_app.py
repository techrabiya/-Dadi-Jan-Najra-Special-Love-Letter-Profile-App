import streamlit as st

# Page Configuration
st.set_page_config(page_title="Dadi Jan Najra ke liye Pyar 💖", page_icon="👵", layout="centered")

# Custom Styling for Elegance
st.markdown(
    """
    <style>
    .main {
        background-color: #fff5f8;
    }
    .title-text {
        color: #d81b60;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .sub-text {
        color: #555555;
        text-align: center;
        font-size: 18px;
    }
    .letter-box {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        border-left: 5px solid #d81b60;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        font-family: sans-serif;
        font-size: 17px;
        color: #333333;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section
st.markdown("<h1 class='title-text'>🌸 Meri Pyaari Dadi Jan Najra ke Naam 🌸</h1>", unsafe_layout=True)
st.markdown("<p class='sub-text'>Yeh chhota sa digital tohfa aapke liye, dher saare pyaar ke sath (Rabia ki taraf se)</p>", unsafe_allow_html=True)
st.write("---")

# Interactive Dadi Jan Profile Section
st.subheader("🌟 Dadi Jan ka Special Corner")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 👑 Naam aur Pehchan")
    st.write("**Full Name:** Najra (नजरा)")
    st.write("**Hamaari Jaan:** Hamaare ghar ki raunak aur sabse badi duayein.")

with col2:
    st.markdown("### 🎨 Pasand aur Khasiyat")
    dadi_color = st.selectbox("Unka Favourite Rang:", ["Royal Pink 💖", "Graceful White 🤍", "Peaceful Blue 💙", "Warm Golden 💛"])
    dadi_food = st.multiselect("Khane mein kya pasand hai:", ["Ghar ka khaana", "Meethi Kheer", "Taaze Phal", "Garam Chai"])

st.write("")

# Heartfelt Hinglish Letter Section
st.markdown("### 💌 Dadi Jan ke liye Dil se likha hua Pyara Khat")

letter_content = """
    <div class='letter-box'>
        <b>Meri Sabse Pyaari Dadi Jan Najra,</b><br><br>
        Assalamu Alaikum!<br><br>
        Meri zindagi mein agar koi sabse badi nemat hai, toh woh aapki duaayein aur aapka pyaar hai jo aap hum sab par hamesha barsti rehti hain. Aap hi hamaare ghar ki jaan aur barkat hain.<br><br>
        Jab bhi main padhai ya coding karti hoon, toh mujhe pata hai ki aapki khamosh duaayein mere sath hain. Yeh chhota sa app maine sirf aapko khush karne ke liye banaya hai, taaki aapko pata chale ki aap hum sab ke liye kitni khaas hain.<br><br>
        Allah Taala aapko lambi umar de, sehat-e-kamil ata farmaye aur aapka saaya hamesha humare sar par salamat rakhe. Ameen!<br><br>
        <b>Aapki pyari poti,</b><br>
        <i>Rabia</i> 💖
    </div>
"""

st.markdown(letter_content, unsafe_allow_html=True)

# Celebration / Balloons effect
st.write("")
if st.button("Dadi Jan ko Pyar aur Duayein Bhejein ✨"):
    st.balloons()
    st.success("Yeh pyaar bhara sandesh seedha Dadi Jan ke dil tak pahunch gaya! 🌸👵")
