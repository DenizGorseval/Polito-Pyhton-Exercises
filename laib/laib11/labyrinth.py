def maze_form(filename):
    try: 
        maze = []
        with open(filename) as file:
            for line in file:
                row = []
                for value in line.strip():
                    row.append(value)
                maze.append(row)
    except FileNotFoundError:
        return("The file can not be found")
    return maze

def corridors_formed(maze):
    corridors = {}
    for r,row in enumerate(maze):
        for c,value in enumerate(row):
            if (r == 0 and value == " "):
                coord = (r,c)
                corridors[coord] = []
                if maze[r+1][c] == " ":
                    corridors[coord].append((r+1,c))
                if (c-1) >= 0 and c < (len(row)-1):
                    if maze[r][c+1] == " ":
                        corridors[coord].append((r,c+1))
                    if maze[r][c-1] == " ":
                        corridors[coord].append((r,c-1))
                    break
            elif value != " ":
                continue
            coord = (r,c)
            corridors[coord] = []

            if r != len(maze) - 1:
                if maze [r-1][c] == " ":
                    corridors[coord].append((r-1,c))

                if maze[r+1][c] == " " and r < len(maze)-1:
                    corridors[coord].append((r+1,c))

                if maze[r][c+1] == " " and c < len(row)-1:
                    corridors[coord].append((r,c+1))

                if maze[r][c-1] == " " and c != 0:
                    corridors[coord].append((r,c-1))
            else:
                if maze [r-1][c] == " ":
                    corridors[coord].append((r-1,c))

                if maze[r][c+1] == " " and c < len(row)-1:
                    corridors[coord].append((r,c+1))

                if maze[r][c-1] == " " and c != 0:
                    corridors[coord].append((r,c-1))
        
    return corridors

def paths_formed(corridors,maze):
    paths = {}
    for key in corridors:
        paths[key] = "?"
    

    for key in corridors:
        r,c = key
        counter = 0
        if r == 0:
            paths[key] = "N"
            counter += 1
        elif r == len(maze)-1:
            paths[key] = "S"
            counter += 1
        if counter == 2:
            break
    
    for key,direction in paths.items():
        if direction != "?":
            r_key, c_key = key
            for value in corridors[key]:
                r_val,c_val = value
                if r_val - 1 == r_key:
                    paths[value] = direction
                elif c_val - 1 == c_key:
                    paths[value] = "W"
                elif c_val + 1 == c_key:
                    paths[value] = "E"
        
    return paths
               


                

        
    
    







def main():
    filename = "maze.txt"
    maze = maze_form(filename)
    corridor_dict = corridors_formed(maze)
    paths = paths_formed(corridor_dict, maze)
    print()

main()