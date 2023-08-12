import streamlit as st

st.set_page_config(page_title="Number Guessing Game", page_icon=":game_die:")

## necesarry function

def is_int(num):
    try:
        num = int(num)
    except ValueError:
        return False
    else:
        return True
    
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
#####

## load local css file
local_css(".//style//style.css")

## ----- HEADER SECTION -----
st.title("Number Guessing Game :game_die:")

st.write('This is **Number Guessing Game** with Streamlit. You just have to correctly guess the number from 0 to 9. Good luck and have fun.')
# st.write('*PS.* If you are done, refresh the website to get a new number to guess.')

## --- Game Area ---
with st.container():
    st.subheader("I'm rolling the number. What could it be? :thinking_face:")
    num = st.text_input("Guess the number (0-9)", placeholder='e.g. 5')
    
    correct_num = 2
    
    if num:
        
        if is_int(num):
            num = int(num)
            if num == correct_num:
                st.write(f"That's right. It is {num}. Well done. :thumbsup:")
            else:
                st.write("Better luck next time. :wink:")
                
        else:
            st.write("It is not number. Try again.")

with st.container():
    st.write("---")
    st.header("Message Me in Email. :e-mail:")
    
    msg_form = """
    <form action="https://formsubmit.co/ekkpawin1d@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    
    st.markdown(msg_form, unsafe_allow_html=True)