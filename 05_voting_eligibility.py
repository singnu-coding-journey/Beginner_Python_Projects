def checking_voting_eligibility(ages):
    if ages >= 18:
        print("you are eligible for voting")
    else:
        print("you are not eligible for voting")   

age = int(input("Enter your age: "))
checking_voting_eligibility(age)
