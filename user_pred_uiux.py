# import streamlit as st
# import pickle
# st.title("User predictions based on Input features")
# st.write("Write something")
# a=st.text_input("Enter input")
# model=pickle.load()
# st.button(":cherries: Press Me")

import numpy as np
import pickle
import pandas as pd
import streamlit as st 


pickle_in = open("/Users/adityapnv/Documents/AD_userreview/model/user_pred.pkl","rb")
classifier=pickle.load(pickle_in)


def welcome():
    return "Welcome All"


def predict_note_authentication(Age,EstimatedSalary,Gender_Female,Gender_Male):
   
    prediction=classifier.predict([[Age,EstimatedSalary,Gender_Female,Gender_Male]])
    print(prediction)
    return prediction



def main():
    st.title("User predictions based on Input features")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit User Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.text_input("Age","Type Here")
    EstimatedSalary = st.text_input("EstimatedSalary","Type Here")
    Gender_Female = st.text_input("Gender_Female","Type Here")
    Gender_Male = st.text_input("Gender_male","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(eval(Age), 
                                           eval(EstimatedSalary), 
                                           eval(Gender_Female), 
                                           eval(Gender_Male)
                                          )
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("If 1 is the output")
        st.text("The user purchases the product")

if __name__=='__main__':
    main()
    