def decision_tree(weather):
    if weather == "Sunny":
        return "No Play"
    elif weather == "Rainy":
        return "No Play"
    else:
        return "Play"


print("Decision Tree Algorithm")
weather = input("Enter weather (Sunny/Rainy/Cloudy): ")
print("Decision:", decision_tree(weather))
