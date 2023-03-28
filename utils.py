
#extra additional utility functions. converting data types, generating random data
import json

def decode_output(output_text):
    decoded_output = json.loads(output_text)
    required_courses = decoded_output["required_courses"]
    optional_courses = decoded_output["optional_courses"]
    num_required_courses = len(required_courses)
    num_optional_courses = len(optional_courses)

    output_str = "Based on your declared major and completed courses, here is our recommendation for your remaining coursework:\n\n"

    if num_required_courses == 0:
        output_str += "Congratulations, you have completed all required coursework for your major!"
    else:
        output_str += f"You need to take {num_required_courses} required course(s):\n"
        for course in required_courses:
            output_str += f"- {course}\n"

        if num_optional_courses > 0:
            output_str += "\nYou may also take these optional course(s):\n"
            for course in optional_courses:
                output_str += f"- {course}\n"

    return output_str

