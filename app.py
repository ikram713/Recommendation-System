
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess data
data = pd.read_csv('udemy_courses.csv')
data['title_subject'] = data['course_title'] + ' ' + data['subject']

cv = CountVectorizer(max_features=1000)
vectors = cv.fit_transform(data['title_subject']).toarray()
similarity = cosine_similarity(vectors)

def get_recommendations(course):
    if course not in data['course_title'].values:
        return ["Course not found."]
    idx = data[data['course_title'] == course].index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    return [data.iloc[i[0]]['course_title'] for i in sim_scores]

st.title("Course Recommendation System")

course = st.text_input("Enter a course title:")

if course:
    recommendations = get_recommendations(course)
    st.write("### Recommendations:")
    for rec in recommendations:
        st.write("- " + rec)
