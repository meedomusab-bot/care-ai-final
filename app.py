import streamlit as st

# قاعدة بيانات بسيطة لأكواد الأعطال (يمكنك توسيعها لاحقاً)
diagnostic_database = {
    "P0300": "يوجد خلل في إشعال المحرك (Random/Multiple Cylinder Misfire). قد تحتاج لفحص شمعات الاحتراق (Spark Plugs).",
    "P0171": "خليط الوقود فقير جداً (System Too Lean). قد يكون هناك تسريب في هواء المحرك أو حساس الـ MAF يحتاج تنظيف.",
    "P0420": "كفاءة نظام الحفاز أقل من الحد المسموح. قد يكون هناك مشكلة في دبة التلوث (Catalytic Converter).",
    "P0301": "خلل في الإشعال في الأسطوانة رقم 1.",
}

st.title("🚗 نظام تشخيص أعطال السيارات الذكي")

menu = ["كشف الأعطال", "حول التطبيق"]
choice = st.sidebar.selectbox("القائمة", menu)

if choice == "كشف الأعطال":
    st.subheader("أدخل كود العطل الموجود في جهاز الفحص")
    user_code = st.text_input("مثال: P0300").upper()
    
    if st.button("تحليل العطل"):
        if user_code in diagnostic_database:
            st.success("تم العثور على معلومات:")
            st.write(f"**العطل:** {diagnostic_database[user_code]}")
        elif user_code == "":
            st.warning("الرجاء إدخال كود أولاً.")
        else:
            st.error("الكود غير موجود في قاعدة البيانات الحالية. هل تود تجربة كود آخر؟")

elif choice == "حول التطبيق":
    st.write("هذا التطبيق يساعدك في فهم أكواد أعطال السيارة الأساسية.")

