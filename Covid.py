import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open(r"C:\Users\phuon\OneDrive\Desktop\Medi_safety\Covid_model.sav", 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Covid Disease Prediction System',
                          
                          ['Covid Prediction'],
                          icons=['person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Covid Prediction'):
    
    # page title
    st.title('Covid Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
         
        #Indicates whether the patient treated medical units of the first, second or third level.
        USMER = st.text_input('USMER: the patient treated medical units of the first, second or third level.')
        
    with col2:
        MEDICAL_UNIT = st.text_input('MEDICAL UNIT: TYPE OF INSTITUTION')
    
    with col3:
        SEX = st.text_input('SEX')
    
    with col1:
        PATIENT_TYPE = st.text_input('Type of care the patient received')
    
    with col2:
        INTUBED = st.text_input('Connected to the ventilator')
    
    with col3:
        PNEUMONIA = st.text_input('Have air sacs inflammation')
    
    with col1:
        AGE = st.text_input('Age of the person')
    
    with col2:
        PREGNANT = st.text_input('Patient is pregnant or not')

    with col3:
        DIABETES = st.text_input('Patient has diabetes or not')

    with col1:
        COPD = st.text_input('The patient has Chronic obstructive pulmonary disease or not')
    
    with col2:
        ASTHMA = st.text_input('Patient has asthma or not')
        
    with col3:
        INMSUPR = st.text_input('The patient is immunosuppressed or not.')

    with col1:
        HIPERTENSION = st.text_input('The patient has hypertension or not')
    with col2:
        OTHER_DISEASE = st.text_input('Patient has other disease or not')
        
    with col3:
        CARDIOVASCULAR = st.text_input('The patient has heart or blood vessels related disease')
    
    with col1:
        OBESITY = st.text_input('The patient is obesity or not')
    with col2:
        RENAL_CHRONIC = st.text_input('Patient has chronic renal disease or not')
        
    with col3:
        TOBACCO = st.text_input('Whether the patient is a tobacco user')
    with col1:
        ICU = st.text_input('Whether the patient had been admitted to an Intensive Care Unit')
    
    
    
    
    # code for Prediction
    covid_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        covid_prediction = diabetes_model.predict([['USMER', 'MEDICAL_UNIT', 'SEX', 'PATIENT_TYPE', 'INTUBED', 'PNEUMONIA', 'AGE', 'PREGNANT', 'DIABETES', 'COPD', 'ASTHMA', 'INMSUPR', 'HIPERTENSION', 'OTHER_DISEASE', 'CARDIOVASCULAR', 'OBESITY', 'RENAL_CHRONIC', 'TOBACCO', 'ICU']])
        
        if (covid_prediction[0] == 1):
          covid_diagnosis = 'The person is diabetic'
        else:
          covid_diagnosis = 'The person is not diabetic'
        
    st.success(covid_diagnosis)