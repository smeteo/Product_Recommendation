import streamlit as st
import pandas as pd
import bz2
import pickle
import _pickle as cPickle

st.title('Product Recommendation')

html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit Recommendation App </h2>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)

#df_pivot = pickle.load(open("df_pivot","rb"))

##df_pivot = pd.read_csv('df_pivot.csv', index_col='order_id')

#def decompress_pickle(file):
#    data = bz2.BZ2File(file, 'rb')
#    data = cPickle.load(data)
#    return data

file = 'compressed_pivot.pbz2'

data = bz2.BZ2File(file, 'rb')
df_pivot = cPickle.load(data)







selected_product=st.selectbox('Select Your Product', list(df_pivot.columns))


recommendations = df_pivot.corrwith(df_pivot[int(selected_product)])
recommendations.dropna(inplace=True)
recommendations = pd.DataFrame(recommendations, columns=['Correlation']).reset_index()
recommendations = recommendations.sort_values(by='Correlation', ascending=False)




st.write("Top 5 Products You May Also Like")

st.dataframe(recommendations[1:].head().set_index('product_id'))