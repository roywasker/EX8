def elect_next_budget_item(votes: list[set[str]], balances: list[float], costs: dict[str, float]):
    numOfVotes = {}
    # count how much vote each item get
    for vote in votes:
        for item in vote:
            numOfVotes[item] = numOfVotes.get(item, 0) + 1

    # calculate how much more is left to pay
    numOfMoneyForEachCitizen = {}
    newCosts = costs.copy()
    for i in range(len(balances)):
        for item in votes[i]:
            newCosts[item] -= balances[i]

    # calculate who is the next item
    for item in numOfVotes:
        numOfMoneyForEachCitizen[item] = newCosts[item] / numOfVotes[item]
    nextItem = min(numOfMoneyForEachCitizen.items(), key=lambda element: element[1])

    moneyAdded = 0
    totalMoneyForNextItem = 0.0

    # calculate how much money we get now
    for i in range(len(balances)):
        if nextItem[0] in votes[i]:
            totalMoneyForNextItem += balances[i]

    # add  0.1 until we can buy the next item
    while totalMoneyForNextItem < costs[nextItem[0]]:
        totalMoneyForNextItem = 0.0
        for i in range(len(balances)):
            balances[i] = round(balances[i] + 0.1, 2)
            if nextItem[0] in votes[i]:
                totalMoneyForNextItem += balances[i]
        moneyAdded = round(moneyAdded + 0.1, 2)

    # rest the money for the Citizen that buy the item
    for i in range(len(balances)):
        if nextItem[0] in votes[i]:
            balances[i] = 0

    # print the result
    print(f"After adding {moneyAdded} to each citizen, \"{nextItem[0]}\" is chosen.")
    for i in range(len(balances)):
        print(f"Citizen {i + 1} has {balances[i]:.2f} remaining balance.")


votes = [{"Park", "Trees"}, {"Trees"}, {"Park", "Lights"}, {"Lights"}, {"Park"}]
balances = [1.5, 2.4, 3.3, 4.2, 5.1]
costs = {"Park": 1000, "Trees": 2000, "Lights": 3000}

elect_next_budget_item(votes, balances, costs)
