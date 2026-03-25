import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(page_title="Nexora",page_icon="discord_fake_avatar_decorations_1772433206923.gif", layout="wide")

# Load external CSS
def load_css():
    with open("static/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# --- HERO SECTION ---

## Hero text /Center logo using columns


    # logo.png in same folder

      

    
#1 sidebar menu

with st.sidebar:
     selected = option_menu(
          menu_title="Nexora Webpage",
          options=["Home Page","Why choose Nexora?","View Shopping","View Hosting","Contact Us"],
          icons=["house","question-lg","bag-check","server","envelope"],
          menu_icon="cast",
          default_index= 0 ,
          )

     
     




if selected== "Home Page":
     col1, col2, col3 = st.columns([1,2,1])
     with col1:
        st.image("nexora.png", width=400)
     with col2:
        st.markdown("<h1>🚀Welcome To Nexora Shop Official Webpage</h1>", unsafe_allow_html=True)
        st.markdown("<h3>Shopping & Hosting in One Place.</h3>", unsafe_allow_html=True)

elif selected == "Why choose Nexora?": 
   
    st.markdown("<h1 style='text-align:center;'>✨Why Choose Nexora?</h1>",unsafe_allow_html=True)

    col1,col2=st.columns(2)

    with col1:
        st.markdown("<div class='card'><h3>🛍️Easy Shopping</h3><p>Buy products quickly.</p></div>",unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'><h3>⚡Fast delivery </h3><p>High speed servers.</p></div>",unsafe_allow_html=True)



elif selected == "View Shopping":
    st.write("<h1 style='text-align:center;'>🛍️Nexora Products!</h1>",unsafe_allow_html=True)
    
    # Minecraft
    col1, col2 = st.columns([3,1])
    with col2:
        st.image("minecraft-1-logo-png-transparent.png",width=200 )
    with col1:
        st.write("<h2 >Minecraft Accounts.</h2>", unsafe_allow_html=True)

    # Steam
    col1, col2 = st.columns([3,1])
    with col2:
        st.image("Steam-Logo-PNG-Images-HD.png", width=200)
    with col1:
        st.write("<h2 >Steam Games (Keys).</h2>", unsafe_allow_html=True)

    # Discord
    col1, col2 = st.columns([3,1])
    with col2:
        st.image("29342-nitro-style-platinum.png", width=200)
    with col1:
        st.write("<h2 >Discord Items.</h2>", unsafe_allow_html=True)




     

elif selected== "View Hosting":
    st.write("<h1 style='text-align:center;'>Nexora Hosting Plans Are Coming Soon👀!</h1>",unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])  # Middle column is wider
    with col2:
        st.image("standard (2).gif",  use_container_width=True)

    

else:
    st.write("<h1 style='text-align:center;'>Conntact Us with Discord</h1>",unsafe_allow_html=True) 
    st.markdown(
    """
    <div class="flex-center">
    <a href='https://discord.gg/ZqEXhr7bkH'target='blank'>
    <button>📞Contact Us on Discord</button>
    </a>
    </div>
""",unsafe_allow_html=True) 
    
    st.markdown("<h3 style='text-align:center;'>To get more information.</h3>",unsafe_allow_html=True) 
       
st.write("---")  
st.markdown("<h6 style='text-align:center;'>©NEXORA SHOP PVT (LTD)</h6>",unsafe_allow_html=True)      




     
      







    




# CENTERED MAIN BUTTONS


