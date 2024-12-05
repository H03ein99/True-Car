from sklearn import tree


def my_learner(my_list,year_miles):
    x = []
    y = []
    for year, miles, price in my_list:
        x.append([year, miles])
        y.append(price)
    clf = tree.DecisionTreeClassifier()
    clf.fit(x, y)
    answer = clf.predict(year_miles)
    return answer

