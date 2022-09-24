import random,sys
from turtle import penup

QUESTIONS = [
    {
        'question':'How many times can you take 2 apples from a pile of 10 apples?',
        'answer':'Once. Then you have a pile of 8 apples.',
        'accept': ['once','one','1'],
    },
    {
        'question':'what begins with "e" and ends with "e" but only has one letter in it?',
        'answer':'An envelope',
        'accept':['envelope'],
    },
    {
        'question':'Is it possible to draw a square with three sides?',
        'answer':'Yes. All squares have three sides.They also have four sides',
        'accept':['yes'],
    },
    {
        'question':'what does a towel get as it dries?',
        'answer':'wet',
        'accept':['wet'],
    },
    {
        'question':'Imagine you are in a haunted house full of evil ghosts. What do you have to do to stay safe?',
        'answer':'Nothing! I will just have to stop imagining.',
        'accept':['nothing','stop imagining'],
    },
    {
        'question':'A taxi driver is going the wrong way down a one-way street. she passes ten cops but does not get a ticket. why not?',
        'answer':'she was just walking',
        'accept':['whe was just walking','walking'],
    },
    {
        'question':'What is the only world the rhymes with orange?',
        'answer':'Orange',
        'accept':['orange'],
    },
    {
        'question':'What is the largest number in the world?',
        'answer':'one',
        'accept':['one','1'],
    },

]

CORRECT_TEXT = ['correct!','That is right.',"You're right.", 'You got it','Rightoh!']
INCORRECT_TEXT = ['Incorrect!','Nope!','You missed it',"That isn't right."]

print('''Trick brainy Questions by Ajuba okwuchukwu Anthony
Can you figure out the answers to these trick questions?
Enter QUIT to quit''')

input('Press Enter to begin...')
random.shuffle(QUESTIONS)

score = 0

for question_number,qa in enumerate(QUESTIONS): # Main program loop
    #as question_number is looping through the QUESTION, qa is keeping track of the "accept"
    print('\n'*30) # Clear screen
    print('Question:',question_number + 1)
    print('score:',score, '/',len(QUESTIONS))
    print('QUESTION:',qa['question'])

    response = input(' ANSWER: ').lower()

    if response == 'quit':
        print('Thanks for Playing!')
        sys.exit()

    correct = False
    for acceptance_word in qa['accept']:
        #looping through the accept held by qa while looping through QUESTIONS WITH question_number
        if acceptance_word in response:
            #checking if acceptance_word is in the users response
            correct = True

    if correct:
        text = random.choice(CORRECT_TEXT)
        print(text, qa['answer'])
        score += 1
    else:
        text = random.choice(INCORRECT_TEXT)
        print(text, 'The answer is:',qa['answer'])

    response = input('Press enter for the next question...').lower()

    if response == "quit":
        print('Thanks for playing')
        sys.exit()

print("That's all the questions. Thanks for playing!")
