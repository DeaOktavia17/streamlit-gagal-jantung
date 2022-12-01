import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('penyakit_gagal_jantung.sav', 'rb'))

st.title('Prediksi Penyakit Gagal Jantung')

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input('Umur')

with col2:
    anaemia = st.number_input('Anemia')

with col3:
    creatinine_phosphokinase = st.number_input('Kreatinin Fosfokinase')

with col1:
    diabetes = st.number_input('Diabetes')

with col2:
    ejection_fraction = st.number_input('Fraksi Ejeksi')

with col3:
    high_blood_pressure = st.number_input('Tekanan Darah Tinggi')

with col1:
    platelets = st.number_input('Trombosit')

with col2:
    serum_creatinine = st.number_input('Kreatinin Serum')

with col3:
    serum_sodium = st.number_input('Sodium Serum')

with col1:
    sex = st.number_input('Jenis Kelamin')

with col2:
    smoking = st.number_input('Merokok')

with col3:
    time = st.number_input('Waktu')

heart_diagnosis = ''

if st.button('Prediksi Penyakit Gagal Jantung'):
    heart_prediction = model.predict([[age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time]])

    if(heart_prediction[0]==1):
        heart_diagnosis = 'Pasien Terkena Penyakit Gagal Jantung'
    else:
        heart_diagnosis = 'Pasien Tidak terkena Penyakit Gagal Jantung'

st.success(heart_diagnosis)




