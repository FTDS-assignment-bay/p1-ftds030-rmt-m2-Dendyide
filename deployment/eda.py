import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

def run():
    #membuat judul
    st.title('Consumen Intention Prediction')

    #tambahkan gambar
    image = Image.open('consumen.png')
    st.image(image, caption = 'Consumen Decission')

    #menambahkan deskripsi
    st.write('Page ini dibuat oleh Dendy Dwinanda')

    #show dataframe
    data = pd.read_csv('online_shoppers_intention.csv')
    st.dataframe(data)

    #membuat histogram berdasarkan input user
    st.write('#### Histogram berdasarkan input user')
    option = st.selectbox('Pilih column : ', ('Administrative', 
                                              'Administrative_Duration', 
                                              'Informational', 
                                              'Informational_Duration',
                                              'ProductRelated',
                                              'ProductRelated_Duration',
                                              'BounceRates',
                                              'ExitRates',
                                              'PageValues',
                                              'SpecialDay',
                                              'Month',
                                              'OperatingSystems',
                                              'Browser',
                                              'Region',
                                              'TrafficType',
                                              'VisitorType',
                                              'Weekend',
                                              'Revenue'))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data[option], bins = 30, kde = True)
    st.pyplot(fig)


if __name__ == '__main__':
    run()