def minion_game(string):
    player1 = "Kevin"
    player2 = "Stuart"
    vowels = ["A","E","I","O","U"]
    v_count = 0
    c_count = 0
    for i in range(0,len(string)):
        sub_str= string[i:]
        
        if string[i] in vowels:
            v_count += 1
        else:
            c_count += 1
    print(v_count, c_count)


minion_game("Banana")