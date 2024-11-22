# Questions for MBTI test
questions = [
    {"question": "Do you feel more energized around people or alone?", "choices": ["E", "I"]},
    {"question": "Do you focus on facts and details or big-picture ideas?", "choices": ["S", "N"]},
    {"question": "Do you make decisions based on logic or emotions?", "choices": ["T", "F"]},
    {"question": "Do you prefer a structured schedule or go with the flow?", "choices": ["J", "P"]}
]

# Scoring dictionary
scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}

# Ask each question and update scores
for q in questions:
    print(q["question"])
    print(f"Choices: {q['choices'][0]} (1) / {q['choices'][1]} (2)")
    answer = input("Enter 1 or 2: ")
    if answer == "1":
        scores[q["choices"][0]] += 1
    elif answer == "2":
        scores[q["choices"][1]] += 1

# Determine MBTI type
mbti_type = ""
mbti_type += "E" if scores["E"] > scores["I"] else "I"
mbti_type += "S" if scores["S"] > scores["N"] else "N"
mbti_type += "T" if scores["T"] > scores["F"] else "F"
mbti_type += "J" if scores["J"] > scores["P"] else "P"

print(f"Your MBTI type is: {mbti_type}")
