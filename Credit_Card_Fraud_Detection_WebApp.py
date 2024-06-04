# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:58:55 2024

@author: prachet
"""

import numpy as np
import pickle
import streamlit as st

#loading. the saved model
loaded_model = pickle.load(open('C:/Users/prachet/OneDrive - Vidyalankar Institute of Technology/Desktop/Coding/Machine Learning/ML-Project-10-Credit Card Fraud Detection/creditcard_fraud_trained_model.sav','rb'))

#creating a function for prediction

def credit_card_fraud_detection(input_data):

    #changing the input data to numpy
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting on 1 instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    #print(prediction)

    if(prediction[0]==0):
      return 'It is a Legit Transaction' 
    else:
      return 'It is a Fraud Transaction'
  
    
  
def main():
    
    #giving a title
    st.title('Credit Card Fraud Detection Web App')
    
    col1 ,col2 ,col3 = st.columns(3)
    #getting input data from user
    with col1:
        time = st.number_input("Time")
    with col2:
        v1 = st.number_input("V1")
    with col3:
        v2 = st.number_input("V2")
    with col1:	
        v3 = st.number_input("V3") 
    with col2:
        v4 = st.number_input("V4") 
    with col3:
        v5 = st.number_input("V5")
    with col1:
        v6 = st.number_input("V6")
    with col2:
        v7 = st.number_input("V7")
    with col3:
        v8 = st.number_input("V8")
    with col1:
        v9 = st.number_input("V9")
    with col2:
        v10 = st.number_input("V10")
    with col3:
        v11 = st.number_input("V11")
    with col1:
        v12 = st.number_input("V12")
    with col2:
        v13 = st.number_input("V13")
    with col3:
        v14 = st.number_input("V14")
    with col1:
        v15 = st.number_input("V15")
    with col2:
        v16 = st.number_input("V16")
    with col3:
        v17 = st.number_input("V17")
    with col1:
        v18 = st.number_input("V18")
    with col2:
        v19 = st.number_input("V19")
    with col3:
        v20 = st.number_input("V20")
    with col1:
        v21 = st.number_input("V21")
    with col2:
        v22 = st.number_input("V22")
    with col3:
        v23 = st.number_input("V23")
    with col1:
        v24 = st.number_input("V24")
    with col2:
        v25 = st.number_input("V25")
    with col3:
        v26 = st.number_input("V26")
    with col1:
        v27 = st.number_input("V27")
    with col2:
        v28 = st.number_input("V28")
    with col3:
        amount = st.number_input("Amount")
    
    
    # code for prediction
    predict = ''
    
    #creating a button for Prediction
    if st.button('Predict Credit Card Fraud'):
        predict = credit_card_fraud_detection((time,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,amount))
        
    st.success(predict)
    
    
    
if __name__ == '__main__':
    main()
    