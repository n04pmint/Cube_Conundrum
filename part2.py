def main():
    
    path = "input/input.txt"
    inputs = get_input(path)
    formatted_input = format_inputs_into_list(inputs)
   
def format_inputs_into_list(inputs):
    
    #split each game into a list, then append to a main list
    games = []
    input_list = {"red": 12 }, {"green": 13},{"blue": 14}
    

    #get gameid and split cubesets from string.
    for line in inputs:
        # line: Game 2: 1 green, 17 red; 1 blue, 6 red, 7 green; 2 blue, 4 red, 7 green; 1 green, 6 red, 2 blue
        l = line.strip().split(":", 1)
        cubesets = l[1].split(";")
        gameid = l[0].split()
        gameid = gameid[1]
        set_number = 0
        # Game 1
        # cubesets
        # [' 1 green, 17 red', ' 1 blue, 6 red, 7 green', ' 2 blue, 4 red, 7 green', ' 1 green, 6 red, 2 blue']
        #print(f"GAME#{gameid}")
        #print(f"Cubeset: {cubesets}")
        for cubeset in cubesets:
            #cubeset 
            # 1 green, 17 red
            # 1 blue, 6 red, 7 green
            # 2 blue, 4 red, 7 green
            # 1 green, 6 red, 2 blue
            
            sets= {}
            set_number += 1
            setnumber = "set" + str(set_number)
            setnumber = {}
            colors = cubeset.split(",")
            
            for each in colors:
                #print(f"colors : {colors}")
                color = each.split()
                #print(f"color : {color}")
                sets[color[1]]= color[0]  
            
            for key, value in sets.items():
                
                for d in input_list:
                    if key in d and int(value) > d[key]:
                        print(f"IMPOSSIBble gameid: {gameid} -- {key} : {int(value)} {sets}")
                        games.append(gameid)
                        
                        break

                        
                
    #2278               

                   
    convert_list = set(games)
    games = list(convert_list)
    games.sort(key=int)
    
    print(games)              
    total = sum(int(item) for item in games)     
    total = 5050 - total 
    print(total)         

def get_input(path):
    with open(path) as f:
        return f.readlines()

def sum_of_100(n):
    n = 100
    sum_of_integers = (n / 2) * (1 + n)
    print(sum_of_integers)  # Output: 5050


main()