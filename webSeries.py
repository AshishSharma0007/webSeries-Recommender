import pickle
import pandas as pd
import streamlit as st


def recommend(value):
    Series_index = Series[Series['Series_Title'] == value].index[0]
    ditances = similarity[Series_index]
    Series_list = sorted(list(enumerate(ditances)),reverse=True,key=lambda x:x[1])[1:9]

    recommend_Series = []
    recommend_Series_posters = []
    recommend_Series_Rating = []
    for i in Series_list:
        recommend_Series.append(Series.iloc[i[0]].Series_Title)
        recommend_Series_posters.append(Series.iloc[i[0]].Poster_Link)
        recommend_Series_Rating.append(Series.iloc[i[0]].IMDB_Rating)
    return recommend_Series,recommend_Series_posters,recommend_Series_Rating

Series = pickle.load(open('webSeries.pkl','rb'))

similarity = pickle.load((open('webSeries_sim.pkl','rb')))
st. set_page_config(layout="wide")
st.title("Web Series Recommender")
selected = st.selectbox('Select any one Series for Recommendations:',Series['Series_Title'].values)

if st.button('Recommend Series'):
    names,posters,rating = recommend(selected)
    st.header('We recommend you these Series on basis of your choice:')    
    for i in range(2):
            col1, col2,col3,col4 = st.columns(4)
            with col1:
                st.subheader(names[0 + 4*i])
                st.image(posters[0 + 4*i],use_column_width='auto')
                st.write(rating[0 + 4*i])
            with col2:
                st.subheader(names[1 + 4*i])
                st.image(posters[1 + 4*i],use_column_width='auto')
                st.write(rating[0 + 4*i])
            with col3:
                st.subheader(names[2 + 4*i])
                st.image(posters[2 + 4*i],use_column_width='auto')
                st.write(rating[0 + 4*i])
            with col4:
                st.subheader(names[3 + 4*i])
                st.image(posters[3 + 4*i],use_column_width='auto')
                st.write(rating[0 + 4*i])
