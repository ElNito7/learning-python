def computegrade() :
    score = input("Enter your score: ")
    try :
        if float(score) >= 0.9 :
            result = "A"
        elif float(score) >= 0.8 :
            result = "B"
        elif float(score) >= 0.7 :
            result = "C"
        elif float(score) >= 0.6 :
            result = "D"
        elif float(score) < 0.6 :
            result = "F"
    except :
        result = "Bad Score"
    print(result)
computegrade() 