 About This Project : 

I created this project while learning about **machine learning**. It's a simple **course recommendation system** that suggests Udemy courses based on the course title you choose. The goal was to apply what I learned in a small but useful project with a working user interface.

---

 ✅ Features

- Recommends similar Udemy course titles based on your selection.
- Uses content-based filtering (based on course title and subject).
- Fast and lightweight — no complex model training.
- Built with a simple and interactive UI using Streamlit.

---

## 🔍 How It Works

1. The user selects a course title from a dropdown list.
2. The system uses a combination of the **course title** and **subject** to represent the course.
3. Text is converted into numerical form using **CountVectorizer** (bag-of-words model).
4. It calculates **cosine similarity** between courses.
5. It shows the top 5 most similar course titles as recommendations.
