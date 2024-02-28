#Code solves Advent Of Code 2023 Day 2 parts 1 and 2.
# TODO: Code repeats itself and can be simplified further. DRY principle. 

import re
max_red=12 
max_green=13
max_blue=14

def file_to_list():
    with open ('games.txt', 'r') as file:
        stripped_list=[]
        for line in file:
            stripped_list.append(line.strip())
    #print(stripped_list)
    return(stripped_list)



def red():
    red_list=[]
    red_rounds=[]
    for index, line in enumerate(file_to_list()):
        get_red = re.findall("\d+\sred", line)
        game_number=index+1
        red_rounds=[int(item.split()[0]) for item in get_red]
        possible_red=["fail" for x in red_rounds if x > 12]
        for i in possible_red:
            if i == "fail":
                red_list.append(game_number)
        print(game_number, possible_red)
    print(red_list)
    return(red_list)

def green():
    green_list=[]
    green_rounds = []
    for index, line in enumerate(file_to_list()):
        get_green = re.findall("\d+\sgreen", line)
        game_number=index+1
        green_rounds=[int(item.split()[0]) for item in get_green]
        possible_green=["fail" for x in green_rounds if x > 13]
        for i in possible_green:
            if i == "fail":
                green_list.append(game_number)
        print(game_number, possible_green)
    print(green_list)
    return(green_list)
          
def blue():
    blue_list= []
    blue_rounds = []
    for index, line in enumerate(file_to_list()):
        get_blue = re.findall("\d+\sblue", line)
        game_number=index+1
        blue_rounds=[int(item.split()[0]) for item in get_blue]
        possible_blue=["fail" for x in blue_rounds if x > 14]
        for i in possible_blue:
            if i == "fail":
                blue_list.append(game_number)
            print(game_number, possible_blue)
    print(blue_list)
    return(blue_list)

def possible_games():
    games=[]
    game_number=0
    for index, line in enumerate(file_to_list()):
        game_number+=1
        games.append(game_number)
    games_possible=[i for i in games if i not in red() and i not in blue() and i not in green()]
    games_possible = list(set(games_possible))
    print(games_possible)
    return games_possible

def sum_games():
    total=0
    for i in possible_games():
        total+=i
    print(total)

def cube_power():
    sum_power=0
    for index, line in enumerate(file_to_list()):
        get_red = re.findall("\d+\sred", line)
        get_blue = re.findall("\d+\sblue", line)
        get_green = re.findall("\d+\sgreen", line)
        game_number=index+1
        red_rounds=[int(item.split()[0]) for item in get_red]
        blue_rounds=[int(item.split()[0]) for item in get_blue]
        green_rounds=[int(item.split()[0]) for item in get_green]
        power=max(red_rounds) * max(blue_rounds) * max(green_rounds)
        sum_power+=power
        print(game_number," : ", power)
        print(sum_power)
    return (sum_power)

        

        
if __name__ == "__main__":
    #file_to_list()
    red()
    green()
    blue()
    possible_games()
    sum_games()
    cube_power()
    

       
    


        




    
