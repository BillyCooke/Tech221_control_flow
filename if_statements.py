# if, elif and else

# age = 20
#
# if age >= 18:
#     print("You are the correct age to buy a ticket for this movie")
# elif age < 18:
#     print("Sorry you are not old enough for this movie")

film_rating = "hi"

if film_rating.lower() == "universal":
    print("All ages can watch this movie")
elif film_rating.lower() == "pg":
    print("parental guidance recommended")
elif film_rating.lower() == "12":
    print("You must be at least 12 years old to watch this")
elif film_rating.lower() == "15":
    print("You must be at least 15 years old to watch this")
elif film_rating.lower() == "18":
    print("You must be at least 18 to watch this")
else:
    print("This is not a correct rating, please use universal, pg, 12, 15, 18")

# There are no switch or case statements in python

