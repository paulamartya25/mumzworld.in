import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

# Configure the Groq client
if API_KEY:
    client = Groq(api_key=API_KEY)
else:
    st.error("API Key not found. Please add it to your .env file.")

# Design the webpage
st.set_page_config(page_title="Mumzworld Assistant", page_icon="👶")

# --- CUSTOM CSS FOR PINK BACKGROUND & ANIMATIONS ---
st.markdown("""
    <style>
    /* 1. Add a vibrant pink background to the entire app */
    [data-testid="stAppViewContainer"] {
        background-color: #FFB6D9; /* Vibrant Pink */
    }
    
    /* Make the top header transparent so it blends with the pink */
    [data-testid="stHeader"] {
        background-color: transparent;
    }
    
    /* Ensure all text is black for readability */
    body {
        color: #000000 !important;
    }
    
    p, div, span, h1, h2, h3, h4, h5, h6, li, ul, ol {
        color: #000000 !important;
    }
    
    /* 2. Animation: Slide-down effect for the main title */
    @keyframes slideDown {
        0% { transform: translateY(-30px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }
    .animated-title {
        animation: slideDown 1s ease-out;
        color: #d81b60; /* Deep pink */
        text-align: center;
        font-family: 'Helvetica', sans-serif;
    }

    /* 3. Animation: Continuous pulsing effect for the slogans */
    @keyframes pulse {
        0% { transform: scale(1); color: #ff69b4; }
        50% { transform: scale(1.05); color: #ff1493; }
        100% { transform: scale(1); color: #ff69b4; }
    }
    .slogan-text {
        animation: pulse 2.5s infinite;
        text-align: center;
        font-weight: bold;
        font-size: 1.2rem;
        margin-top: -10px;
        margin-bottom: 25px;
    }
    
    /* Button styling - Pink */
    .stButton > button {
        background: linear-gradient(135deg, #FF69B4 0%, #FF1493 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(255, 20, 147, 0.3) !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #FF1493 0%, #FF69B4 100%) !important;
        box-shadow: 0 6px 20px rgba(255, 20, 147, 0.5) !important;
        transform: translateY(-2px) !important;
    }
    
    .stButton > button:active {
        transform: scale(0.98) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Language selection at the top
col_lang1, col_lang2, col_lang3 = st.columns([1, 3, 1])
with col_lang2:
    selected_language = st.radio(
        "🌍 Select Language | اختر اللغة:",
        ["English 🇬🇧", "العربية 🇸🇦", "Both 🌐"],
        horizontal=True,
        key="language_selector"
    )

st.markdown("---")

# Bilingual content dictionaries
content_en = {
    "welcome": "🎉 Welcome to Mumzworld! 🎉",
    "title": "👶 Smart Parenting Assistant",
    "slogans": [
        "✨ Because every mom deserves a little magic! ✨",
        "💝 Your baby, your love, our support!",
        "🌟 Every milestone matters - we're here for all of them!",
        "👶 From newborns to toddlers - we've got you covered!",
        "🛍️ Shop Smarter, Parent Better! 🧸",
        "💕 Making motherhood moments magical!",
        "🌈 Where parenting meets possibility!",
        "👨‍👩‍👧‍👦 Family first, always!",
    ],
    "tagline": "🏪 Your One-Stop Shop for All Baby Needs 🏪",
    "description": "Not sure what to buy? Tell us about your baby's current stage or your situation, and we'll curate a list of essentials for you!",
    "example": "Example: 'My 6-month-old is starting to eat solid foods. What equipment do I need?'",
    "input_label": "💭 What's your baby concern?",
    "arabic_checkbox": "🌍 Also display the response in Arabic",
    "button_text": "Get Product Recommendations 🚀",
}

content_ar = {
    "welcome": "🎉 أهلا وسهلا بك في مامز وورلد! 🎉",
    "title": "👶 مساعد الأبوة والأمومة الذكي",
    "slogans": [
        "✨ لأن كل أم تستحق قليلاً من السحر! ✨",
        "💝 طفلك، حبك، دعمنا!",
        "🌟 كل مرحلة مهمة - نحن هنا من أجلك!",
        "👶 من حديثي الولادة إلى الأطفال الصغار - نحن نغطيك!",
        "🛍️ تسوقي بذكاء، كوني أماً أفضل! 🧸",
        "💕 صنع لحظات الأمومة سحرية!",
        "🌈 حيث تلتقي الأبوة بالإمكانية!",
        "👨‍👩‍👧‍👦 العائلة أولاً، دائماً!",
    ],
    "tagline": "🏪 متجرك الشامل لجميع احتياجات طفلك 🏪",
    "description": "غير متأكدة مما تشترين؟ أخبرينا عن مرحلة طفلك الحالية أو وضعك، وسنختار لك قائمة بالضروريات!",
    "example": "مثال: 'طفلي البالغ من العمر 6 أشهر يبدأ في تناول الأطعمة الصلبة. ما المعدات التي أحتاجها؟'",
    "input_label": "💭 ما هي مخاوف طفلك؟",
    "arabic_checkbox": "🌍 عرض الرد أيضاً باللغة العربية",
    "button_text": "احصل على التوصيات 🚀",
}

# Display content based on language selection
import random

if selected_language in ["English 🇬🇧", "Both 🌐"]:
    st.markdown(f'<div style="text-align: center; margin-bottom: 20px;"><h2 style="color: #FF1493; font-size: 2.5em; margin: 0;">{content_en["welcome"]}</h2></div>', unsafe_allow_html=True)
    st.markdown(f'<h1 class="animated-title">{content_en["title"]}</h1>', unsafe_allow_html=True)
    selected_slogan_en = random.choice(content_en["slogans"])
    st.markdown(f'<p class="slogan-text">{selected_slogan_en}</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center; color: #000000; font-size: 1.1em; margin-top: -15px;"><b>{content_en["tagline"]}</b></p>', unsafe_allow_html=True)
    st.write(content_en["description"])

if selected_language == "Both 🌐":
    st.markdown("---")

if selected_language in ["العربية 🇸🇦", "Both 🌐"]:
    st.markdown(f'<div style="text-align: center; margin-bottom: 20px; direction: rtl;"><h2 style="color: #FF1493; font-size: 2.5em; margin: 0;">{content_ar["welcome"]}</h2></div>', unsafe_allow_html=True)
    st.markdown(f'<h1 class="animated-title" style="direction: rtl;">{content_ar["title"]}</h1>', unsafe_allow_html=True)
    selected_slogan_ar = random.choice(content_ar["slogans"])
    st.markdown(f'<p class="slogan-text" style="direction: rtl;">{selected_slogan_ar}</p>', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align: center; color: #000000; font-size: 1.1em; margin-top: -15px; direction: rtl;"><b>{content_ar["tagline"]}</b></p>', unsafe_allow_html=True)

st.markdown("---")

# --- USER INPUT SECTION ---
if selected_language in ["English 🇬🇧", "Both 🌐"]:
    st.write(content_en["example"])

if selected_language == "Both 🌐":
    st.write(content_ar["example"])
elif selected_language == "العربية 🇸🇦":
    st.markdown(f'<p style="color: #000000; direction: rtl; text-align: right;">{content_ar["example"]}</p>')

# User input box
user_input = st.text_area(
    "💭 What's your baby concern?" if selected_language in ["English 🇬🇧", "Both 🌐"] else "💭 ما هي مخاوف طفلك؟",
    placeholder="Example: 'My 6-month-old is starting to eat solid foods. What equipment do I need?'" if selected_language in ["English 🇬🇧", "Both 🌐"] else "مثال: 'طفلي البالغ من العمر 6 أشهر يبدأ في تناول الأطعمة الصلبة. ما المعدات التي أحتاجها؟'",
    height=100
)

# Add a checkbox for the Arabic translation option
show_arabic = st.checkbox(
    "🌍 Also display the response in Arabic" if selected_language in ["English 🇬🇧", "Both 🌐"] else "🌍 عرض الرد أيضاً باللغة العربية"
)

# What happens when they click the button
button_label = content_en["button_text"] if selected_language in ["English 🇬🇧", "Both 🌐"] else content_ar["button_text"]
if st.button(button_label):
    if user_input:
        with st.spinner("Analyzing your needs and translating..." if selected_language in ["English 🇬🇧", "Both 🌐"] else "جاري تحليل احتياجاتك وترجمتها..."):
            
            # The core prompt telling the AI how to act
            prompt = f"""
            You are an expert shopping assistant for Mumzworld, a Middle Eastern e-commerce site for mothers and children.
            A parent has come to you with this situation: "{user_input}"
            
            Provide a warm, empathetic response. Then, list 3 to 5 specific product categories they should look for on Mumzworld to solve this situation. 
            Briefly explain why they need each item.
            
            IMPORTANT: If the baby's situation involves illness, fever, pain, or discomfort, please include:
            1. Recommended baby medicines/supplements that can help (e.g., paracetamol, ibuprofen for babies, saline drops, etc.)
            2. Dosage guidelines (always recommend consulting a pediatrician)
            3. Safe medical products available on Mumzworld
            
            Always emphasize consulting with a pediatrician before giving any medication. Keep the tone helpful and reassuring.
            """
            
            # If the user checked the Arabic box, we add this instruction
            if show_arabic:
                prompt += """
                
                CRITICAL INSTRUCTION: You must provide your entire response in English first. 
                Then, add a visual separator (like ---), and provide the exact translation of your entire response in Arabic.
                """
            
            try:
                # Call the Groq API
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful, empathetic shopping assistant."
                        },
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    # UPDATED: Using the latest Llama 3.3 70B model ID
                    model="llama-3.3-70b-versatile", 
                )
                
                success_message = "✨ Here are your recommendations!" if selected_language in ["English 🇬🇧", "Both 🌐"] else "✨ إليك التوصيات الخاصة بك!"
                st.success(success_message)
                # Display the response in a styled container with black text
                recommendations = chat_completion.choices[0].message.content
                st.markdown(f'<div style="background-color: white; padding: 20px; border-radius: 10px; border-left: 5px solid #FF69B4; color: #000000;"><p style="color: #000000;">{recommendations}</p></div>', unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        warning_message = "Please type a situation in the box above first." if selected_language in ["English 🇬🇧", "Both 🌐"] else "يرجى كتابة الوضع في الصندوق أعلاه أولاً."
        st.warning(warning_message)