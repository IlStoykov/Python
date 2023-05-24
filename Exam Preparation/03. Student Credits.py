def students_credits(*args):
    credit_score = 0
    course_dict = {}
    result = []
    for item in args:
        course_name, credits, t_point, d_points = item.split("-")
        credits, t_point, d_points = int(credits), int(t_point), int(d_points)
        d_credits = (d_points/t_point)*credits
        credit_score += d_credits
        course_dict[course_name] = (d_points/t_point)*credits
    if credit_score >= 240:
        result.append(f"Diyan gets a diploma with {credit_score:.1f} credits.")
    else:
        needed_score = 240 - credit_score
        result.append(f"Diyan needs {needed_score:.1f} credits more for a diploma.")
    dict_result = sorted(course_dict.items(), key=lambda x:-x[1])
    for k, v in dict_result:
        result.append(f"{k} - {float(v):.1f}")
    return "\n".join(result)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490",

    )
)

# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )
# print(
#     students_credits(
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Java Development-10-300-150"
#     )
# )
