def minion_game(string):
    vowels = ["A","E","I","O","U"]
    v_count = 0
    c_count = 0
    up_string = string.upper()

    for i in range(0,len(up_string)):

        if up_string[i] in vowels:
            v_count += len(string) - i
        else:
            c_count += len(string) - i
    if v_count > c_count:
        print(f"Kevin {v_count}")
    elif v_count < c_count:
        print(f"Stuart {c_count}")
    else:
        print("Draw")


minion_game("Banana")