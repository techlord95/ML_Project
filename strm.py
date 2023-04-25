# import streamlit as st
# import pandas as pd
# import pickle

# # Load your trained machine learning model
# with open('model.pkl', 'rb') as f:
#     model = pickle.load(f)

# # Create your Streamlit app UI
# st.title('My Machine Learning App')
# data = st.file_uploader('Upload a CSV file')
# if data is not None:
#     df = pd.read_csv(data)
#     prediction = model.predict(df)
#     st.write(prediction)

# import numpy as np
# import pickle
# import streamlit as st


# model=pickle.load(open("D:/classifier.pkl",'rb'))


# def main():
#     st.title(" Data Scientist Job Prediction ")
    
#     # input variables
#     city_devevelopment_index=st.text_input("City_dev_index(eg-0.920)")
#     education_level=st.text_input("edu_level(Graduate=2/Masters=3/High School=1/Phd=4/Primary School=0)")
#     experience=st.text_input("Experience(year),eg-8.0")
#     company_size=st.text_input("eg=74.5")
#     last_new_job=st.text_input('In year(1.0)')
#     training_hours=st.text_input('Training hours')
#     gender_Female=st.text_input("If gender=female,add 1 else 0")
#     gender_Male=st.text_input("If gender=Male,if yes add 1 else 0")
#     gender_Other=st.text_input("If gender=other,add 1 or 0")
#     relevent_experience_Hasreleventexperience=st.text_input("if yes add 1",key="re0")
#     relevent_experience_Noreleventexperience=st.text_input("if yes add 1",key='re1')
#     company_type_=st.text_input("0 or 1",key="type") #1
#     type_early_Stage=st.text_input('0 or 1',key="stage")#0
#     type_funded=st.text_input("0 or 1",key="fund")#0
#     type_Ngo=st.text_input("0 or 1",key="ngo")#0
#     type_other=st.text_input("0 or 1",key="ot")#0
#     type_public=st.text_input("0 or 1",key="pvt")#0
#     type_pvt=st.text_input("0 or 1",key="pub")#0
#     major_disc_arts=st.text_input("0/1",key="arts")#1
#     major_disc_bd=st.text_input("0/1",key="bd")#0
#     major_disc_hm=st.text_input("0/1",key="hm")#0
#     major_disc_nm=st.text_input("0/1",key="nm")#0
#     major_disc_other=st.text_input("0/1",key="other")#0
#     major_disc_stem=st.text_input("0/1",key="stem")#0
#     enrolled_ftc=st.text_input("0/1",key="ftc")#1
#     enrolled_ptc=st.text_input("0/1",key="ptc")#0
#     # enrolled_tc=st.text_input("0/1",key="tc")#0
    

#     # gender=st.text_input('Gender(Male,Female,Other)')
#     # enrollment=st.text_input('enrollment(no_enrollment/Full time course/Part time course)')
#     # comp_type=st.text_input(company_)

    
    
#     if st.button('Predict'):
#         makeprediction=model.predict([[city_devevelopment_index,education_level,experience,company_size,last_new_job,training_hours,gender_Female,gender_Male,gender_Other,relevent_experience_Hasreleventexperience,relevent_experience_Noreleventexperience,company_type_,type_early_Stage,type_funded,type_Ngo,type_other,type_public,type_pvt,major_disc_arts,major_disc_bd,major_disc_hm,major_disc_nm,major_disc_other,major_disc_other,major_disc_stem,enrolled_ftc,enrolled_ptc]])
#         # output=round(makeprediction[0],2)
        
#         st.success('Fit for the job')
        
    
        
# if __name__=='__main__':
#     main()

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


        
        
    
    
    
    