import streamlit as st
from deep_translator import GoogleTranslator
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

st.set_page_config(page_title="Universal AI Translator", page_icon="🌐", layout="wide")
st.title("🌐 Universal AI Translator with English Script")
st.write("Translate English text into any language and read it easily using English words!")

try:
    translator = GoogleTranslator()
    supported_languages = translator.get_supported_languages(as_dict=True)
    languages_list = sorted([lang.title() for lang in supported_languages.keys()])
except Exception:
    languages_list = ["Hindi", "Telugu", "Tamil", "Kannada", "Malayalam"]
    supported_languages = {"hindi": "hi", "telugu": "te", "tamil": "ta", "kannada": "kn", "malayalam": "ml"}

selected_lang = st.selectbox("Select the target language:", languages_list)
user_text = st.text_area("Type your English sentence here:", height=120)

def get_english_transliteration(text, lang_code):
    try:
        if lang_code == 'te':
            return transliterate(text, sanscript.TELUGU, sanscript.ITRANS).lower()
        elif lang_code == 'hi':
            return transliterate(text, sanscript.DEVANAGARI, sanscript.ITRANS).lower()
        elif lang_code == 'ta':
            return transliterate(text, sanscript.TAMIL, sanscript.ITRANS).lower()
        elif lang_code == 'kn':
            return transliterate(text, sanscript.KANNADA, sanscript.ITRANS).lower()
        elif lang_code == 'ml':
            return transliterate(text, sanscript.MALAYALAM, sanscript.ITRANS).lower()
    except Exception:
        pass
    return None

if st.button("Translate Now", type="primary"):
    if user_text.strip() == "":
        st.warning("Please type some text first!")
    else:
        with st.spinner("Translating... Please wait..."):
            try:
                lang_code = supported_languages[selected_lang.lower()]
                translated_result = GoogleTranslator(source='auto', target=lang_code).translate(user_text)
                
                st.write("---")
                st.success("### 📊 Translation Results")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.info(f"**In Native Script ({selected_lang}):**")
                    st.subheader(translated_result)
                    
                with col2:
                    st.info("**How to Read (In English Words):**")
                    english_script = get_english_transliteration(translated_result, lang_code)
                    
                    if english_script:
                        clean_script = english_script.replace(".h", "").replace("aa", "a").replace("uu", "u")
                        st.subheader(f"🗣️ {clean_script.capitalize()}")
                    else:
                        st.subheader(f"🗣️ {translated_result}")
                        
                st.write("")
                st.caption(f"✍️ *Original Input: {user_text}*")
                
            except Exception as e:
                st.error(f"An error occurred: {e}")