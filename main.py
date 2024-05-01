def main():
    
    path = "input/input.txt"
    inputs = get_input(path)
    formatted_input = format_inputs_into_list(inputs)
   
def format_inputs_into_list(inputs):
    
    #split each game into a list, then append to a main list
    games = []
    input_list = [{"red": 12 }, {"green": 13},{"blue": 14}
    ]

    #get gameid and split cubesets from string.
    for line in inputs:
        l = line.strip().split(":", 1)
        cubesets = l[1].split(";")
        gameid = l[0] 
        # print(gameid)
        # print(f"Cubesets: {cubesets}")
        set_number = 0
        for cubeset in cubesets:
            sets= {}
            set_number += 1
            
            colors = cubeset.split(",")
            for each in colors:
                color = each.split()
                test = {color[1]: color[0]}
                
                   
    #print(games)         
 


def get_input(path):
    with open(path) as f:
        return f.readlines()




main()