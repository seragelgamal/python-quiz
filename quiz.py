# python quiz

print('\r\n')
print('Quiz')
print('\r\n')
print('This quiz has five questions. After answering all five questions, you will receive your mark at the end.')
print('\r\n')

# questions and corresponding answers
questions = ['What is the capital of Canada? ', 'What year is it? ', 'What programming language was this quiz written in? ',
             'Who is the president of the United States? ', 'What month is it? ']
answers = ['ottawa', '2020', 'python', 'donald trump', 'july']

# global score variable
score = 0

# loop through all the questions
for question in questions:
    print('Question ' + str(questions.index(question) + 1) + ':')
    answer = input(question).lower()
    if answer == answers[questions.index(question)]:
        score += 1

# print final score
print('Your score is ' + str(score) + '/5 (' + str(score/5*100) + '%)')
