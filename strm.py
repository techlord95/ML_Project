
import numpy as np
import pickle
import streamlit as st


model = pickle.load(open("D:/classifier.pkl",'rb'))


def main():
    st.title("Data Scientist Job Prediction")
    
    city_development_index = st.text_input("City development index (eg. 0.920)")
    education_level = st.selectbox("Education level", ["Primary School", "High School", "Graduate", "Masters", "Phd"])
    experience = st.text_input("Experience (years), eg. 8.0")
    company_size = st.text_input("Company size, eg. 74.5")
    last_new_job = st.text_input("Years since last new job, eg. 1.0")
    training_hours = st.text_input("Training hours")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    rel_exp = st.selectbox("Experience", ["yes", "No"])
    enrollment = st.selectbox("Enrollment", ["no_enrollment", "Full time course", "Part time course"])
    company_type = st.selectbox("Company type", ["Early Stage Startup", "Funded Startup", "NGO", "Other", "Public Sector", "Pvt Ltd","onepoint"])
    major_discipline = st.selectbox("Major discipline", ["Arts", "Business Degree", "Humanities", "No Major", "Other", "STEM"])
    
    education_level=1 if education_level=="Primary School"else 0
    education_level=1 if education_level=="High School"else 0
    education_level=1 if education_level=="Graduate"else 0
    education_level=1 if education_level=="Masters"else 0
    education_level=1 if education_level=="Phd"else 0
    
    gender_female = 1 if gender == "Female" else 0
    gender_male = 1 if gender == "Male" else 0
    gender_other = 1 if gender == "Other" else 0
    
    has_exp=1 if rel_exp=="yes" else 0 
    no_exp=1 if rel_exp=="yes" else 0 
    
    enrollment_no = 1 if enrollment == "no_enrollment" else 0
    enrollment_ft = 1 if enrollment == "Full time course" else 0
    enrollment_pt = 1 if enrollment == "Part time course" else 0
    
    
    if company_type == "Early Stage Startup":
        company_type_one=0
        company_type_es = 1
        company_type_fs = 0
        company_type_n = 0
        company_type_o = 0
        company_type_ps = 0
        company_type_pl = 0
    elif company_type == "Funded Startup":
        company_type_one=0
        company_type_es = 0
        company_type_fs = 1
        company_type_n = 0
        company_type_o = 0
        company_type_ps = 0
        company_type_pl = 0
    elif company_type == "NGO":
        company_type_one=0
        company_type_es = 0
        company_type_fs = 0
        company_type_n = 1
        company_type_o = 0
        company_type_ps = 0
        company_type_pl = 0
    elif company_type == "Other":
        company_type_one=0
        company_type_es = 0
        company_type_fs = 0
        company_type_n = 0
        company_type_o = 1
        company_type_ps = 0
        company_type_pl = 0
    elif company_type == "Public Sector":
        company_type_one=0
        company_type_es = 0
        company_type_fs = 0
        company_type_n = 0
        company_type_o = 0
        company_type_ps = 1
        company_type_pl = 0
    elif company_type == "onepoint":
        company_type_one=1
        company_type_es = 0
        company_type_fs = 0
        company_type_n = 0
        company_type_o = 0
        company_type_ps = 0
        company_type_pl = 0
    
    else:
        company_type_one=0
        company_type_es = 0
        company_type_fs = 0
        company_type_n = 0
        company_type_o = 0
        company_type_ps = 0
        company_type_pl = 1
        
    major_discipline_arts = 1 if major_discipline == "Arts" else 0
    major_discipline_bd = 1 if major_discipline =="Business Degree" else 0
    major_discipline_hum = 1 if major_discipline == "Humanities" else 0
    major_discipline_nm = 1 if major_discipline == "No Major" else 0
    major_discipline_ot = 1 if major_discipline == "Other" else 0
    major_discipline_stem = 1 if major_discipline == "STEM" else 0
    
    data = np.array([[city_development_index, education_level, experience, company_size, last_new_job, training_hours,
                      gender_female, gender_male, gender_other,has_exp,
                      no_exp, enrollment_no, enrollment_ft, enrollment_pt,company_type_one,company_type_es, company_type_fs, company_type_n, company_type_o, company_type_ps, company_type_pl,
                      major_discipline_arts, major_discipline_bd, major_discipline_hum, major_discipline_nm, major_discipline_ot, major_discipline_stem]])
    
    if st.button("Predict"):
        prediction = model.predict(data)
        if prediction == 0:
            st.write("The applicant is not likely to be hired.")
        else:
            st.write("The applicant is likely to be hired.")
if __name__=="__main__":
    main()


        
        
    
    
    
    
