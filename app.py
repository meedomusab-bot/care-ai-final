import streamlit as st
from PIL import Image

st.title("Car AI System 🚗")
uploaded_file = st.file_uploader("ارفع صورة...", type=["jpg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='الصورة المرفوعة')
    
    if st.button("اكتشف السيارات"):
        with st.spinner("جاري تحميل الذكاء الاصطناعي والتحليل..."):
            try:
                from ultralytics import YOLO
                # تحميل النموذج
                model = YOLO('yolov8n.pt')
                results = model.predict(image)
                st.image(results[0].plot(), caption='النتيجة')
            except Exception as e:
                st.error(f"خطأ أثناء التحليل: {e}")
