import pandas as pd
import numpy as np
import joblib
import streamlit as st
#Load the Model
model=joblib.load(open("decision_tree_model.joblib", 'rb'))
st.title("Sales app")
#Input feature
CompPrice=st.number_input("CompPrice", min_value=0.0)
Income=st.number_input("Income", min_value=0.0)
Advertising=st.number_input("Advertising", min_value=0.0)
Population=st.number_input("Population", min_value=0.0)
Price=st.number_input("Price", min_value=0.0)
ShelveLoc=st.number_input("ShelveLoc", min_value=0.0)
Age=st.number_input("Age", min_value=0.0)
Education=st.number_input("Education", min_value=0.0)
Urban=st.number_input("Urban",min_value=0.0)
US=st.number_input("US",min_value=0.0)

#Make Pred
if st.button('Sales'):
    input_data = np.array([[CompPrice,Income, Advertising, Population, Price, ShelveLoc,
                            Age, Education, Urban, US]])

    prediction = model.predict(input_data)[0]

    st.success(f'predict sal: {prediction}')
