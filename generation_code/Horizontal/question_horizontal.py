import json


def make_example(question, i, q, name):
    return {"image_index": i,
           "split": "test",
           "image_filename": f"{name}.png",
           "question_index": q, 
           "question": question}

def make_dataset(questions):
    return {"info": {"split": "test", "license": "-", "version": "1.0", "date": "09/15/2023"},
           "questions": questions}


template_1 = lambda obj_1, obj_2: f"There is an object to the left of a {obj_1['shape']} to the right of a {obj_2['shape']}, what color is it?" # 2nd
template_2 = lambda obj_1, obj_2: f"There is an object to the left of a {obj_1['shape']} to the right of a {obj_2['shape']}, what shape is it?" # 2nd
template_3 = lambda obj_1, obj_2: f"There is an object to the left of a {obj_1['shape']} to the right of a {obj_2['shape']}, what color is it?" # 3rd
template_4 = lambda obj_1, obj_2: f"There is an object to the left of a {obj_1['shape']} to the right of a {obj_2['shape']}, what shape is it?" # 3rd



temp_list = [template_1, template_2, template_3, template_4]
path_to_folder = ""


with open(path_to_folder + "info.json") as f:
    info = json.load(f)

questions = []
question_type = ""
correct_answer = ""
k = 0 # number of question
for img in range(len(info)):
    obj_0 = info[img][1]['0']
    obj_1 = info[img][1]['1']
    obj_2 = info[img][1]['2']
    obj_3 = info[img][1]['3']
    obj_4 = info[img][1]['4']

    name = info[img][0]
    for j in range(len(temp_list)):
        
        if j == 0:
            questions.append(make_example(temp_list[j](obj_2, obj_0), img, k, name))
            correct_answer += str(obj_1['color']) + '\n'
            question_type += 'color_name' + '\n'
        elif j == 1:
            questions.append(make_example(temp_list[j](obj_2, obj_0), img, k, name))
            correct_answer += str(obj_1['shape']) + '\n'
            question_type += 'shape_name' + '\n'
        elif j == 2:
            questions.append(make_example(temp_list[j](obj_1, obj_3), img, k, name))
            correct_answer += str(obj_2['color']) + '\n'
            question_type += 'color_name' + '\n'
        elif j == 3:
            questions.append(make_example(temp_list[j](obj_1, obj_3), img, k, name))
            correct_answer += str(obj_2['shape']) + '\n'
            question_type += 'shape_name' + '\n'
        
        k += 1

answer = make_dataset(questions)

with open('C:\\tmp\\Reason_test_questions.json', 'w', encoding='utf-8') as json_file:
        json.dump(answer, json_file)

with open('C:\\tmp\\correct_answ.txt', 'w', encoding='utf-8') as f:
        f.write(correct_answer)

with open('C:\\tmp\\question_type.txt', 'w', encoding='utf-8') as f:
        f.write(question_type)
