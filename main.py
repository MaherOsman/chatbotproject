
from flask import Flask, render_template, request
from model import get_course_recommendation
from preprocessing import preprocess_text
import json

app = Flask(__name__)

# Function to receive user input
def get_user_input():
    student_id = request.form.get("student_id")
    major = request.form.get("major")
    semester = request.form.get("semester")
    courses_taken = []
    for i in range(1, 5):
        course = request.form.get(f"course_{i}")
        if course:
            courses_taken.append(course)
    return {"student_id": student_id, "major": major, "semester": semester, "completed_courses": courses_taken}

# handling user input
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = get_user_input()
        with open("course_catalog.json", "r") as f:
            course_catalog = json.load(f)
        model_output = ""  # model output as empty string
        preprocessed_input = {k: preprocess_text(v) if k != "semester" else v for k, v in user_input.items()}
        recommendation, required_courses = get_course_recommendation(preprocessed_input, course_catalog, model_output)
        # Return the course recommendation as a response
        return render_template("recommendation.html", recommendation=recommendation, required_courses=required_courses)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

