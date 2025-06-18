import easygui




def ask_question(the_question, the_image, the_correct_answer, the_score, the_app_name = "MyApp"):
    answer_01 = easygui.ynbox(msg=the_question,
                              title=the_app_name,
                              image=the_image)
    correct_answer = the_correct_answer.lower()
    if correct_answer != "yes":
        answer_01 = not answer_01  # Change True to False
    if answer_01:
        easygui.msgbox(msg="you are right", title=app_name, ok_button="continue")
        the_score += 1
    else:
        easygui.msgbox(msg="you are wrong", title=app_name, ok_button="continue")
    return the_score

# easygui.egdemo()
app_name = "MyApp"
score = 0

score = ask_question(the_question="Is the person in the image cooking",
                     the_image="cooking.gif",
                     the_correct_answer="yes",
                     the_score=score)

score = ask_question(the_question="Is the person in the image driving",
                     the_image="driving.png",
                     the_correct_answer="yes",
                     the_score=score)

easygui.msgbox(msg=f"your final score {score}", title=app_name, ok_button="close")
