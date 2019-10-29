def is_league_united(hero1,hero2):
    if hero1 == "superman" and hero2 == "wonderwomen":
        return True 
    elif hero1 == "wonderwomen" and hero2 == "superman":
        return True
    else:
        return False

    def decide_plan(hero1,hero2):
        if is_league_united(hero1,hero2)==True:
            return "time to save the world!"
        else:
            return "we must unite the league!"

    def run():
        print ("enter name of first hero")
        hero1 = input()
        print ("enter name of second hero")
        hero2 = input()
        print("please enter league or plan")
        userChoice = input()
        if userChoice == "league":
            print (is_league_united(hero1,hero2))
        elif userChoice == "plan":
            print(decide_plan(hero1,hero2))
        else:
            print ("invalid command. Please try again")
            