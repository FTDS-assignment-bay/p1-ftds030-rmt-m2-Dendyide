import streamlit as st
import pandas as pd
import pickle
import json


# memanggil data yang sudah di download

with open('list_num_cols.txt', 'r') as file_1:
  list_num_cols = json.load(file_1)

with open('list_cat_cols.txt', 'r') as file_2:
  list_cat_cols = json.load(file_2)

with open('pipeline.pkl', 'rb') as file_3:
  pipeline = pickle.load(file_3)

def run():
    with st.form('consumen_itention'):
    
        # administrative
        Administrative = st.number_input('Administrative', min_value = 0, max_value = 60, help = 'represent the number of different types of pages visited by the visitor in that session and total time spent in each of these page categories.')
        
        # administrative duration
        Administrative_Duration = st.number_input('Administrative Duration', step=0.01, format="%.2f", help = 'represent the number of different types of pages visited by the visitor in that session and total time spent in each of these page categories.')

        # informational
        Informational = st.number_input('Informational', min_value=0, max_value=100, help = 'represent the number of different types of pages visited by the visitor in that session and total time spent in each of these page categories.')

        # informational duration
        Informational_Duration = st.number_input('Informational Duration', step=0.01, format="%.2f", help = 'represent the number of different types of pages visited by the visitor in that session and total time spent in each of these page categories.')

        # Product related
        ProductRelated = st.number_input('Product Related', min_value=0, max_value=100, help = 'represent the number of different types of pages visited by the visitor in that session and total time spent in each of these page categories.')

        # Product Related duration
        ProductRelated_Duration = st.number_input('Product Related Duration', step=0.01, format="%.2f", help = 'represent the number of different types of pages visited by the visitor in that session and total time spent in each of these page categories.')
        
        # Bounce Rates
        BounceRates = st.number_input('Bounce Rates', step=0.01, format="%.2f", help = 'feature for a web page refers to the percentage of visitors who enter the site from that page and then leave.')

        # Exit Rates
        ExitRates = st.number_input('Exit Rates', step=0.01, format="%.2f", help = 'feature for a specific web page is calculated as for all pageviews to the page, the percentage that were the last in the session.')
        
        # Page Values
        PageValues = st.number_input('Page Values', step=0.01, format="%.2f", help = 'feature represents the average value for a web page that a user visited before completing an e-commerce transaction.')

        # Spesial Day
        SpecialDay = st.number_input('Spesial Day', step=0.01, format="%.2f", help = 'The value of this attribute is determined by considering the dynamics of e-commerce such as the duration between the order date and delivery date.')
        
        # Month
        Month = st.number_input('Month', min_value=1, max_value=12)

        # Operating System
        OperatingSystems = st.number_input('Operating System', min_value=0, max_value=20)

        # Browser
        Browser = st.number_input('Browser', min_value=0, max_value=20)

        # Region
        Region = st.number_input('Region', min_value=0, max_value=20)

        # Traffic Type
        TrafficType = st.number_input('Traffic Type', min_value=0, max_value=20)

        # Visitor Type
        VisitorType = st.selectbox('Visitor Type', ('New_Visitor', 'Returning_Visitor', 'Others'), index = 1)

        # Weekend
        Weekend = st.number_input('Weekend', min_value=0, max_value=1, help = '0 = False, 1 = True')

        #bikin submit button form
        submitted = st.form_submit_button('Predict')

    data_inf = {
    'Administrative' : Administrative,
    'Administrative_Duration' : Administrative_Duration,
    'Informational' : Informational,
    'Informational_Duration' : Informational_Duration,
    'ProductRelated' : ProductRelated,
    'ProductRelated_Duration' : ProductRelated_Duration,
    'BounceRates' : BounceRates,
    'ExitRates' : ExitRates,
    'PageValues' : PageValues,
    'SpecialDay' : SpecialDay,
    'Month' : Month,
    'OperatingSystems' : OperatingSystems,
    'Browser' : Browser,
    'Region' : Region,
    'TrafficType' : TrafficType,
    'VisitorType' : VisitorType,
    'Weekend' : Weekend}
    
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        #split between numerical and categorical columns
        data_inf_num = data_inf[list_num_cols]
        data_inf_cat = data_inf[list_cat_cols]

        # menggabungkan categorical dan numerical
        data_inf_final = pd.concat([data_inf_cat, data_inf_num], axis=1)
        data_inf_final
        #predict using linear reg model

        y_pred_inf = pipeline.predict(data_inf_final)

        st.write('## Rating : ', str(int(y_pred_inf)))


if __name__ == '__main__':
   run()

