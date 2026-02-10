def game_score():
    player = input("Enter the Player Name : ")
    no_of_games = int(input("Enter the Number of Games : "))
    score = int(input("Enter the total Score achieved : "))   
    average_socre = score/no_of_games
    print(f"player: {player}\nGames Played: {no_of_games}\nTotal Score: {score}\nAverage Score: {average_socre}")

game_score()
