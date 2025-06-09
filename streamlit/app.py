import streamlit as st
import pickle
import helper


xgd_model = pickle.load(open('model/xgb_model.pkl', 'rb'))

st.set_page_config(
  page_title="Duplicate Question Pairs'",
  layout="wide"
)

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = xgd_model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')