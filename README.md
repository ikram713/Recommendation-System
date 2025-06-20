# 📚 Udemy Course Recommendation System

A simple and lightweight machine learning project that recommends Udemy courses based on your selection using content-based filtering. Built with an interactive UI using **Streamlit**.



## 📖 About This Project

I created this project while learning about **machine learning**. It's a simple **course recommendation system** that suggests Udemy courses based on the course title you choose. The goal was to apply what I learned in a small but useful project with a working user interface.



## ✅ Features

- Recommends similar Udemy course titles based on your selection.
- Uses content-based filtering (based on course title and subject).
- Fast and lightweight — no complex model training required.
- Built with a clean and simple **Streamlit** interface.



## 🔍 How It Works

1. The user selects a course title from a dropdown list.
2. The system uses the **course title** and **subject** to represent each course.
3. Text data is transformed into vectors using **CountVectorizer** (bag-of-words model).
4. The system calculates **cosine similarity** between the selected course and all others.
5. It displays the **top 5 most similar** course titles as recommendations.






