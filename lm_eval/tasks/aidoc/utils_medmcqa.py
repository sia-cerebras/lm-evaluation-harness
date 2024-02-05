# Copied from Master
def doc_to_text(doc) -> str:
    """
    Question: <question>
    Options:
    A. <choice1>
    B. <choice2>
    C. <choice3>
    D. <choice4>
    Answer:
    """
    choices = [doc["opa"], doc["opb"], doc["opc"], doc["opd"]]
    option_choices = {'A': choices[0], 'B': choices[1], 'C': choices[2], 'D': choices[3]}

    prompt = "Question: " + doc["question"] + "\n\nOptions:\n"
    for choice, option in option_choices.items():
        prompt += f"{choice.upper()}. {option}\n"
    prompt += "The answer is:"
    return prompt

def doc_to_target(doc) -> str:
    return ['A', 'B', 'C', 'D'][int(doc['cop'])]
