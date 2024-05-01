def utility(worksheet: str): 
    '''
    Evaluates the worksheet in terms of test performance. Returns final test score of the student.
    '''
    messages = [] 
    for j in range(len(posttest_problems)):
        test_problem = posttest_problems.iloc[j]['question']
        test_instruction = f'''Now the student is asked to work on the following problem on a test: {test_problem} Given the student's initial skill levels and the worksheet the student has received, what's the probability that the student can solve the problem correctly? Explain your reasoning and give a single number between 0 and 100 in square brackets.'''
        if j == 0:
            user_message = f"""{persona}
Here's a worksheet that the student receives:
{worksheet}

{test_instruction}
"""
        else:
            user_message = test_instruction
        messages.append({"role": "user", "content": user_message})
        chat_completion = openai.ChatCompletion.create(model=model_id, messages=messages, temperature=temperature)
        output = chat_completion.choices[0].message.content
        messages.append({"role": "assistant", "content":  output})   
    scores = re.findall(r'\[.*?\]', messages_string)
    sum_score = 0
    for s in scores:
        sum_score += try_convert_to_float(s)
    avg_score = sum_score / len(scores)

    return avg_score