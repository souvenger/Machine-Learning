import numpy as np
import pandas as pd
import streamlit as st
import pickle as pk
import difflib

movies_data = pk.load(open('movies_data.pkl', 'rb'))
similarity_score = pk.load(open('model.pkl', 'rb'))

indices = pd.Series(movies_data.index,
                    index=movies_data['title']).drop_duplicates()


def find_movie(name):
    movie = movies_data['title'].tolist()
    similar_movies = difflib.get_close_matches(name, movie)

    close_matched = similar_movies[0]
    idx = indices[close_matched]
    similarity_movie_score = list(enumerate(similarity_score[idx]))
    movie_list = sorted(similarity_movie_score,
                        key=lambda x: x[1], reverse=True)

    # print name of movies based on index
    print("Suggested Movies are : ")
    j = 0
    l = []
    for i in movie_list:
        suggested_movie = movies_data[movies_data.index ==
                                      i[0]]['title'].values[0]
        l.append(suggested_movie)
        j += 1
        if(j == 25):
            break
    return l


def main():
    bg_img = '''
    <style>
              .stApp     {
          background-image: url("https://s3.ap-southeast-2.amazonaws.com/www.cryptoknowmics.com/blog/wp-content/uploads/2019/12/06164428/Hollywood-movies-of-2019.png");
          background-size: cover;
    }
    </style>
    '''

    st.sidebar.title("Developer's Contact")
    st.sidebar.markdown('[![Harsh-Dhamecha]'
                        '(https://img.shields.io/badge/Author-Sourav%20Dey-brightgreen)]'
                        '(https://github.com/souvenger)')
    st.markdown(bg_img, unsafe_allow_html=True)
    st.markdown("# MOVIE ENDORSEMENT SYSTEM")
    movie_input = st.text_input("Enter Ur Favourite Movie")
    if(st.button("Show Recommendation")):
        l = find_movie(movie_input)
        for i in l:
            st.subheader(i)


#find_movie('iron man')
if __name__ == '__main__':
    main()
