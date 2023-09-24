import json


def make_example(question, i, k, name):

    return {"image_index": i,
           "split": "test",
           "image_filename": f"{name}.png",
           "question_index": k, 
           "question": question}

def make_dataset(questions):

    return {"info": {"split": "test", "license": "-", "version": "1.0", "date": "09/15/2023"},
           "questions": questions}


template_1 = lambda obj_0, obj_3, obj_4: f"""There is an object to the left of the {obj_0['color']} {obj_0['shape']} to the left of the {obj_3['color']} {obj_3['shape']} in front of the {obj_4['color']} {obj_4['shape']}; what color is it?"""
template_2 = lambda obj_0, obj_3, obj_4: f"""There is an object to the left of the {obj_0['color']} {obj_0['shape']} to the left of the {obj_3['color']} {obj_3['shape']} behind the {obj_4['color']} {obj_4['shape']}; what color is it?"""
template_3 = lambda obj_0, obj_3, obj_4: f"""There is an object to the left of the {obj_0['color']} {obj_0['shape']} to the left of the {obj_3['color']} {obj_3['shape']} in front of the {obj_4['color']} {obj_4['shape']}; what shape is it?"""
template_4 = lambda obj_0, obj_3, obj_4: f"""There is an object to the left of the {obj_0['color']} {obj_0['shape']} to the left of the {obj_3['color']} {obj_3['shape']} behind the {obj_4['color']} {obj_4['shape']}; what shape is it?"""

path_to_folder = ""


with open(path_to_folder + "info.json") as f:
    info = json.load(f)

k = 0
questions = []
question_type = ""
correct_answer = ""
for i in range(len(info)):
    obj_3 = info[i][1]['3']
    obj_0 = info[i][1]['0']
    obj_4 = info[i][1]['4']
    name = info[i][0]
    questions.append(make_example(template_1(obj_0, obj_3, obj_4), i, k, name))
    correct_answer += info[i][1]['7']['color'] + "\n" # In front of
    question_type += 'color_name' + '\n'
    k += 1
    questions.append(make_example(template_2(obj_0, obj_3, obj_4), i, k, name))
    correct_answer += info[i][1]['6']['color'] + "\n" # Behind
    question_type += 'color_name' + '\n'
    k += 1
    questions.append(make_example(template_3(obj_0, obj_3, obj_4), i, k, name))
    correct_answer += info[i][1]['7']['shape'] + "\n"
    question_type += 'shape_name' + '\n'
    k += 1
    questions.append(make_example(template_4(obj_0, obj_3, obj_4), i, k, name))
    correct_answer += info[i][1]['6']['shape'] + "\n"
    question_type += 'shape_name' + '\n'
    k += 1

answer = make_dataset(questions)

with open(path_to_folder + 'Reason_test_questions.json', 'w', encoding='utf-8') as json_file:
        json.dump(answer, json_file)

with open(path_to_folder + 'correct_answ.txt', 'w', encoding='utf-8') as f:
        f.write(correct_answer)

with open(path_to_folder + 'question_type.txt', 'w', encoding='utf-8') as f:
        f.write(question_type)

