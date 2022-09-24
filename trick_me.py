'''clickbait generator by ajuba okwuchukwua anthony
A clickbait headline generator for your soulless content architectural website.
Tags: large, intermediate,humour,world.'''

import random

# Set up the constants
OBJECT_PRONOUNS = ['Her','Him','Them']
POSSESIVE_PRONOUNS = ['Her','His','Their']
PERSONAL_PRONOUNS = ['She','He','They']
STATES = ['New jessey','Caliornia','New York','Pennysylvania',
            'Ohio','North Carolina','Michigan','Illionis','Georgia']

NOUNS = ['Athlete','Clown','Shovel','Pale Diet', 'Doctor','Parent',
            'Cat','Dog','Chicken','Robot','Video Game','Avacado',
            'Plastic Straw','Serial Killer','Telephone Psychic']

PLACES = ['House','Attic','Bank Deposit Box','School','Basement',
            'Workplace','Donut Shop','Apocalypse Bunker']

WHEN = ['Soon','This year','Later today','RIGHT NOW','Next Week']

def main():
    print('Clickbait Headline Generator')
    print('By Ajuba Okwuchukwu Anthony')
    print()

    print('Our Website needs to trick people into looking at ads!')
    while 1:
        print('Enter the number of clickbait headlines to generate:')
        response = input('> ')
        if not response.isdecimal():
            print('Please enter a number.')
        else:
            number_of_headlines = int(response)
            break

    for j in range(number_of_headlines):
        click_bait_type = random.randint(1,8)

        if click_bait_type == 1:
            headline = generate_are_millennials_killing_headline()
        elif click_bait_type == 2:
            headline = generate_what_you_dont_know_headline()
        elif click_bait_type == 3:
            headline = generate_big_companies_hate_her_headline()
        elif click_bait_type == 4:
            headline = generate_you_wont_believe_headline()
        elif click_bait_type == 6:
            headline = generate_gift_idea_headline()
        elif click_bait_type == 7:
            headline = generate_reason_why_headline()
        elif click_bait_type ==8:
            headline = generate_job_automated_headline()

        print(headline)
    print() # Newline

    website = random.choice(['website','blag','Facebook','Googles',
                              'Tweedie','Pastgram'])
    
    when = random.choice(WHEN).lower()
    print('Post these to our', website,when,'or you/are fired!')

# Now lets go ahead and create the functions we have already placed in use.
# Each of these functions returns a different type of headline:

def generate_are_millennials_killing_headline():
    noun = random.choice(NOUNS)
    return 'Are Millenials Killing the {} Industry?'.format(noun)

def generate_what_you_dont_know_headline():
    noun = random.choice(NOUNS)
    plural_noun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return 'Without This {},{} Could Kill You {}.'.format(noun,plural_noun,when)

def generate_big_companies_hate_her_headline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return 'Big Companies Hate {}! See How This {} {} Invented a Cheaper {}'.format(pronoun,state,noun1,noun2)

def generate_you_wont_believe_headline():
    plural_noun1 = random.choice(NOUNS) + 's'
    plural_noun2 = random.choice(NOUNS) + 's'
    return ' What {} Dont Want to Know About {}'.format(plural_noun1,plural_noun2)

def generate_gift_idea_headline():
    number = random.randint(6,19)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return '{} Gift Ideas to Give Your {} From {}'.format(number,noun,state)

def generate_reason_why_headline():
    number1 = random.randint(4,17)
    plural_noun = random.choice(NOUNS) + 's'
    number2 = random.randint(1,number1) # number2 <= number1
    return '{} Reasons Why {} Are More Interesting Than You Think (Number {} Will Surprise You!)'.format(number1,plural_noun,number2)

def generate_job_automated_headline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0,2)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = POSSESIVE_PRONOUNS[i]
    if pronoun1 == 'Their':
        return 'This {} {} Didn\'t Robots Would Take {} Job. were Wrong.'.format(state,noun,pronoun1,pronoun2)
    else:
        return 'This {} {} Didn\'t Think RObots Would Take {} Job. {} was Wrong'.format(state,noun,pronoun1,pronoun2)


main()  


