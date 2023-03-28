# cleaning text data before feeding it to model. Functions for tokenizing, stemming, stop words, etc


# Get the student's input

import nltk
import transformers
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from transformers import pipeline
from utils import decode_output

def preprocess_text(text):
    # Tokenize text into words
    words = nltk.word_tokenize(text.lower())

    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    #  put words back into string
    preprocessed_text = ' '.join(words)

    return preprocessed_text


def parse_user_input(user_input):
    # Split user input into pieces
    student_id, major, *courses = user_input.split(",")

    major = preprocess_text(major)

    completed_courses = []
    for course in courses:
        if course != "":
            completed_courses.append(preprocess_text(course.strip()))

    # put parsed information into dictionary
    parsed_input = {"student_id": student_id, "major": major, "completed_courses": completed_courses}

    return parsed_input


'''
import nltk
import transformers
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from transformers import pipeline
from utils import decode_output


def parse_user_input(user_input):
    student_id, major, *courses = user_input.split(",")

    major = preprocess_text(major)

    completed_courses = []
    for course in courses:
        if course != "":
            completed_courses.append(preprocess_text(course.strip()))

    parsed_input = {"student_id": student_id, "major": major, "completed_courses": completed_courses}

    return parsed_input


def preprocess_text(text):
    words = nltk.word_tokenize(text.lower())

    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]

    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    preprocessed_text = ' '.join(words)

    return preprocessed_text


def get_course_recommendation(user_input, course_catalog, model_output):
    input_text = preprocess_text(user_input)
    model = pipeline("text-generation", model="gpt2")
    output_text = model(input_text + model_output, max_length=50, do_sample=True, temperature=0.7)[0]["generated_text"]
    recommendation = decode_output(output_text)
    required_courses = course_catalog[user_input["major"]]["required_courses"]

'''