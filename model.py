
#defining and training nlm input classes, functions for compiling, and functions for evaluating performance

from transformers import pipeline
from utils import decode_output
from preprocessing import preprocess_text
import json

def get_course_recommendation(user_input, course_catalog, model_output):
    input_text = preprocess_text(user_input)

    model = pipeline("text-generation", model="gpt2")

    # generate a response
    output_text = model(input_text + model_output, max_length=50, do_sample=True, temperature=0.7)[0]["generated_text"]
    recommendation = decode_output(output_text)

    #list of required courses
    required_courses = course_catalog[user_input["major"]]["required_courses"]

    # remove courses the user has already completed
    for course in user_input["completed_courses"]:
        if course in required_courses:
            required_courses.remove(course)

    return recommendation, required_courses


def load_course_catalog():
    with open("course_catalog.json", "r") as f:
        course_catalog = json.load(f)
    return course_catalog


def get_user_input():
    # Prompt
    student_id = input("Enter your student ID: ")
    major = input("Enter your major: ")
    completed_courses_str = input("Enter the list of completed courses separated by commas: ")
    completed_courses = [c.strip() for c in completed_courses_str.split(",")]

    user_input = {
        "student_id": student_id,
        "major": major,
        "completed_courses": completed_courses
    }
    return user_input


if __name__ == "__main__":
    course_catalog = load_course_catalog()
    user_input = get_user_input()
    model_output = ""
    recommendation, required_courses = get_course_recommendation(user_input, course_catalog, model_output)
    print(recommendation)
    print(f"\nYou still need to complete the following required courses: {required_courses}")



'''
from transformers import pipeline
from utils import decode_output
from preprocessing import preprocess_text
import json

def get_course_recommendation(user_input, course_catalog, model_output):
    # Preprocess the user input
    input_text = preprocess_text(user_input)

    # Load the model pipeline
    model = pipeline("text-generation", model="gpt2")

    # Generate a response based on the user input and model output
    output_text = model(input_text + model_output, max_length=50, do_sample=True, temperature=0.7)[0]["generated_text"]

    # Decode the output text
    recommendation = decode_output(output_text)

    # Get the list of required courses based on the user's major
    required_courses = course_catalog[user_input["major"]]["required_courses"]

    # Remove any courses the user has already completed from the list of required courses
    for course in user_input["completed_courses"]:
        if course in required_courses:
            required_courses.remove(course)

    return recommendation, required_courses

# Load course catalog
import json

def load_course_catalog():
    with open("course_catalog.json", "r") as f:
        course_catalog = json.load(f)
    return course_catalog

# Load the course catalog
course_catalog = load_course_catalog()

# Prompt the user for input (you can replace this with your own input function)
user_input = {
    "student_id": "123456",
    "major": "computer science",
    "completed_courses": ["calculus i", "calculus ii", "intro to programming"]
}

# Call the function to generate course recommendation based on user input
recommendation, required_courses = get_course_recommendation(user_input, course_catalog)

# Print the recommendation
print(recommendation)
print(f"\nYou still need to complete the following required courses: {required_courses}")
'''

'''
from transformers import pipeline
from utils import decode_output
from preprocessing import preprocess_text
import json


def get_course_recommendation(user_input, course_catalog, model_output):
    # Preprocess the user input
    input_text = preprocess_text(user_input)

    # Load the model pipeline
    model = pipeline("text-generation", model="gpt2")

    # Generate a response based on the user input and model output
    output_text = model(input_text + model_output, max_length=50, do_sample=True, temperature=0.7)[0]["generated_text"]

    # Decode the output text
    recommendation = decode_output(output_text)

    # Get the list of required courses based on the user's major
    required_courses = course_catalog[user_input["major"]]["required_courses"]

    # Remove any courses the user has already completed from the list of required courses
    for course in user_input["completed_courses"]:
        if course in required_courses:
            required_courses.remove(course)

    return recommendation, required_courses


# Load the course catalog
course_catalog = load_course_catalog()

# Prompt the user for input (you can replace this with your own input function)
user_input = {
    "student_id": "123456",
    "major": "computer science",
    "completed_courses": ["calculus i", "calculus ii", "intro to programming"]
}

# Get the model output from the user input
model_output = ""

# Call the function to generate course recommendation based on user input
recommendation, required_courses = get_course_recommendation(user_input, course_catalog, model_output

# Print the recommendation
print(recommendation)
print(f"\nYou still need to complete the following required courses: {required_courses}")
'''