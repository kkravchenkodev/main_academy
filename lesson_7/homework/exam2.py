correct = 0
with open('questions', 'r', encoding='utf-8') as q_file:
    with open('answers2', 'w', encoding='utf-8') as answers2_file:
        for line in q_file:
            question = line.strip()
            print(f"\nquestion: {question}\n")
            answers2_file.write(question)
            for _ in range(3):
                print(f"options: {q_file.readline().strip()}")
            answer = int(q_file.readline().split(':')[1].strip())
            user_answer = input("\n>>")
            # while not isinstance(user_answer, int):
            #     user_answer = input("\n>>")
            try:
                user_answer = int(user_answer.strip())
            except ValueError as e:
                print(e)
                print(f'Answer {user_answer} is not integer')
            if user_answer == answer:
                correct += 1
                answers2_file.write(f"\nAnswer {user_answer} is CORRECT\n")
            else:
                answers2_file.write(f"\nAnswer {user_answer} is WRONG\n")
