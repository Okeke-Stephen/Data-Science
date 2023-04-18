#Creating the web app with streamlit
from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np


def predict_quality(model, df):
    
    predictions_data = predict_model(estimator = model, data = df)
    
    return predictions_data['Label'][0]
    
model = load_model('electgrid')

st.title("Electric Grid Stability Predictive App")
st.write('This app was created to predict the stability of electric grids by Okeke')

tau1 = st.number_input('tau1', 
                                                min_value=0.3, 
                                                max_value=10.0, 
                                                value=5.0)

tau2 = st.number_input('tau2', 
                                                min_value=0.3, 
                                                max_value=10.0, 
                                                value=5.0)

tau3 = st.number_input('tau3', 
                                                min_value=0.3, 
                                                max_value=10.0, 
                                                value=5.0)

tau4 = st.number_input('tau4', 
                                                min_value=0.3, 
                                                max_value=10.0, 
                                                value=5.0)

p1 = st.number_input('p1', 
                                        min_value=0.5, 
                                        max_value=10.0, 
                                        value=2.0)

p2 = st.number_input('p2', 
                                        min_value=-2.0, 
                                        max_value=-1.0, 
                                        value=-1.0)

p3 = st.number_input('p3', 
                                        min_value=-2.0, 
                                        max_value=-1.0, 
                                        value=-1.0)

p4 = st.number_input('p4', 
                                        min_value=-2.0, 
                                        max_value=-1.0, 
                                        value=-1.0)

g1 = st.number_input('g1', 
                                                min_value=0.01, 
                                                max_value=10.0, 
                                                value=4.0)

g2 = st.number_input('g2', 
                                                min_value=0.01, 
                                                max_value=10.0, 
                                                value=4.0)

g3 = st.number_input('g3', 
                                                min_value=0.01, 
                                                max_value=10.0, 
                                                value=4.0)

g4 = st.number_input('g4', 
                                                min_value=0.01, 
                                                max_value=10.0, 
                                                value=4.0)


features = {'tau1': Reaction_time_of_participant1, 'tau2': Reaction_time_of_participant2,
            'tau3': Reaction_time_of_participant3, 'tau4': Reaction_time_of_participant4,
            'p1': Nominal_power_consumed1,'p2': Nominal_power_consumed2,'p3': Nominal_power_consumed3,'p4': Nominal_power_consumed4,
            'g1': Coefficient_proportional_price1,'g2': Coefficient_proportional_price2,'g3': Coefficient_proportional_price3,'g4': Coefficient_proportional_price4
            }
 

features_df  = pd.DataFrame([features])

st.table(features_df)  

if st.button('Predict'):
    
    prediction = predict_quality(model, features_df)
    
    st.write('Based on the values provided, the Grid is '+ str(prediction))
