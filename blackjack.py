import random
import os


#Read data, numbers from 1 to 10.
def read_data():
    numbers = []
    with open('./numbers.txt', 'r', encoding='utf-8') as n:
        for line in n:
            numbers.append(line.strip())
    return numbers


#Hands, cards
def run():
    data = read_data()

    dealer_card1 = random.choice(data)
    dealer_cards = [dealer_card1]
    dealer_hand = dealer_card1

    user_card1 = random.choice(data)
    user_card2 = random.choice(data)
    user_cards = [user_card1 , user_card2]
    user_hand = int(user_card1) + int(user_card2)
    user_money = 1
    win_number = 21
    w = """ 
____    ____  ______    __    __     ____    __    ____  __  .__   __. 
\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  | 
 \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  | 
  \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  | 
    |  |    |  `--'  | |  `--'  |       \    /\    /    |  | |  |\   | 
    |__|     \______/   \______/         \__/  \__/     |__| |__| \__| 
                                                                       
                                                                       """

    l = """
____    ____  ______    __    __      __        ______        _______. _______ 
\   \  /   / /  __  \  |  |  |  |    |  |      /  __  \      /       ||   ____|
 \   \/   / |  |  |  | |  |  |  |    |  |     |  |  |  |    |   (----`|  |__   
  \_    _/  |  |  |  | |  |  |  |    |  |     |  |  |  |     \   \    |   __|  
    |  |    |  `--'  | |  `--'  |    |  `----.|  `--'  | .----)   |   |  |____ 
    |__|     \______/   \______/     |_______| \______/  |_______/    |_______|
                                                                               
            """

    while user_money == 1:
    
        #First screen and game
        os.system('cls')
        print("""
 ___                                                    ___ 
|A  |                                                  |A  |
| ♥ |Welcome to Las Vegas Blackjack, type your decision| ♥ |
|__A|                                                  |__A|

        """)
        print('Dealer cards: ')
        print(dealer_cards)
        print('Dealer hand: ' + str(dealer_hand))
        print(' ')
        print('Your cards: ')
        print(user_cards)
        print('Your hand: ' + str(user_hand))
        print(' ')
        user_decision = input('You wanna HIT? (type: Y or N): ')
        print(' ')

        if user_decision.isalpha():

            #User want one more card
            if user_decision == 'Y':

                user_card3 = random.choice(data)
                user_hand = int(user_hand) + int(user_card3)
                user_cards.append(user_card3)

                if int(user_hand) == int(win_number):
                    user_money = int(user_money) - int(1)
                    print(w)
                    print('You win, luckily')
                    print('Used cards: ' + str(user_cards))
                    print('Your hand: ' + str(user_hand))

                if int(user_hand) > int(win_number):
                    user_money = int(user_money) - int(1)
                    print(l)
                    print('You lose, the house always wins')
                    print('Used cards: ' + str(user_cards))
                    print('Your hand: ' + str(user_hand))

            #Stand
            if user_decision == 'N':

                while int(dealer_hand) <= int(user_hand):
                    dealer_card2 = random.choice(data)
                    dealer_hand = int(dealer_hand) + int(dealer_card2)
                    dealer_cards.append(dealer_card2)

                if int(dealer_hand) == int(win_number):
                    user_money = int(user_money) - int(1)
                    print(l)
                    print('The dealer have 21, you lose.')
                    print('Dealer cards: ' + str(dealer_cards))
                    print('Dealer hand: ' + str(dealer_hand))
                    
                if int(dealer_hand) > int(win_number):
                    user_money = int(user_money) - int(1)
                    print(w)
                    print('The dealer start to fly, you win.')
                    print('Dealer cards: ' + str(dealer_cards))
                    print('Dealer hand: ' + str(dealer_hand))

                if int(dealer_hand) > int(user_hand) and int(dealer_hand) < int(win_number):
                    user_money = int(user_money) - int(1)
                    print(l)
                    print('The dealer have a better hand, you lose.')
                    print('Dealer cards: ' + str(dealer_cards))
                    print('Dealer hand: ' + str(dealer_hand))



if __name__ == '__main__':
    run()