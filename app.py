import streamlit as st
from deep_translator import GoogleTranslator

# యాప్ సెటప్
st.set_page_config(page_title="Universal AI Translator", page_icon="🌐")
st.title("🌐 Universal AI Translator")
st.write("Translate English text into any language in the world!")

# deep-translator నుండి అన్ని లాంగ్వేజెస్ లిస్ట్ ని ఆటోమేటిక్ గా తీసుకోవడం
try:
    translator = GoogleTranslator()
    supported_languages = translator.get_supported_languages(as_dict=True) # {'english': 'en', 'telugu': 'te', ...}
    
    # లాంగ్వేజ్ పేర్లను Capitalize చేయడం (చూడడానికి బాగుండడం కోసం)
    languages_list = sorted([lang.title() for lang in supported_languages.keys()])
except Exception:
    # ఒకవేళ నెట్‌వర్క్ ఇష్యూ వస్తే బ్యాకప్ లిస్ట్
    languages_list = ["Hindi", "Telugu", "Tamil", "Kannada", "Malayalam", "Spanish", "French", "German"]
    supported_languages = {"hindi": "hi", "telugu": "te", "tamil": "ta", "kannada": "kn", "malayalam": "ml", "spanish": "es", "french": "fr", "german": "de"}

# యూజర్ లాంగ్వేజ్ సెలెక్ట్ చేసుకోవడానికి డ్రాప్‌డౌన్
selected_lang = st.selectbox("Select the target language:", languages_list)

# యూజర్ టెక్స్ట్ ఇన్‌పుట్
user_text = st.text_area("Type your English sentence here:", height=150)

# ట్రాన్స్‌లేషన్ బటన్
if st.button("Translate Now", type="primary"):
    if user_text.strip() == "":
        st.warning("Please type some text first!")
    else:
        with st.spinner("Translating... Please wait..."):
            try:
                # సెలెక్ట్ చేసిన లాంగ్వేజ్ కోడ్ ని వెతకడం
                lang_code = supported_languages[selected_lang.lower()]
                
                # ట్రాన్స్‌లేట్ చేయడం
                translated_result = GoogleTranslator(source='auto', target=lang_code).translate(user_text)
                
                # రిజల్ట్ ని స్క్రీన్ మీద చూపించడం
                st.success("### Translated Text:")
                st.write(translated_result)
            except Exception as e:
                st.error(f"An error occurred: {e}")