print('Welcome to 💜♠  Ŧ𝓗𝒆 山𝔬𝐫𝐋𝒹ⓢ  ｈ卂Ｒｄ€Ｓţ ⓠᑌ丨Ƶ  ♛♚ ')
answer=input('Are you ready to play the Quiz ? (y/n) :')
score=0
total_questions=3
 
 
if answer.lower()=='y':
    answer=input('Question 1: What is the doll, Barbie’s, full name?')
    if answer.lower()=="Barbara Millicent Roberts":
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 2: What year did the Titanic sink in the Atlantic Ocean on 15 April, on its maiden voyage from Southampton?')
    if answer.lower()=='1912':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: Who invented Cat’s Eyes in 1934 to improve road safety?')
    if answer.lower()=='Percy Shaw':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')