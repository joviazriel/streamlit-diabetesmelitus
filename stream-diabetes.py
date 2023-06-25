import pickle
import streamlit as st

#membaca model
diabetes_model = pickle.load(open('diabetes_model6.sav', 'rb'))

#judul web
st.title('Prediksi Penyakit Diabetes Melitus ')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    Pregnancies = st.text_input ('input nilai Kehamilan ( 1 - 9 )')

with col2 :
    Glucose = st.text_input ('input nilai Gula Darah ( 70 - 99 )')

with col1:
    BloodPressure = st.text_input ('input nilai Tekanan Darah ( 90 - 120 / 60 - 90 )')

with col2 :
    SkinThickness = st.text_input ('input nilai Ketebalan Kulit ( 1 - 50 )')

with col1:
    Insulin = st.text_input ('input nilai Insulin ( 0 - 500 )')

with col2 :
    BMI = st.text_input ('input nilai Body Massa Index ( 18.5 - 25 )')

with col1:
    DiabetesPedigreeFunction = st.text_input ('input nilai Riwayat Diabetes ( 0 - 2 )')

with col2 :
    Age = st.text_input ('input nilai Umur')

# code untuk prediksi
diab_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0] == 0):
        diab_diagnosis = 'Pasien terkena Diabetes'
    else :
        diab_diagnosis = 'Pasien tidak terkena Diabetes'

    st.success(diab_diagnosis)
