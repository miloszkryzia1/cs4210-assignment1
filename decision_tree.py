# -------------------------------------------------------------------------
# AUTHOR: Milosz Kryzia
# FILENAME: decision_tree.py
# SPECIFICATION: This program creates a decision tree classifier using the sklearn library and visualizes it.
# FOR: CS 4210- Assignment #1
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

# importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

# reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0:  # skipping the header
            db.append(row)
            print(row)

# transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# --> add your Python code here

"""
Age: 1-young, 2-presbyopic, 3-prepresbyopic
Spectacle: 1-myope, 2-hypermetrope
Astigmatism: 1-yes, 2-no
Tear: 1-normal, 2-reduced
"""

for row in db:
    #check Age
    if row[0] == 'Young':
        row[0] = 1
    elif row[0] == 'Presbyopic':
        row[0] = 2
    elif row[0] == 'Prepresbyopic':
        row[0] = 3
    #check Spectacle Prescription
    if row[1] == 'Myope':
        row[1] = 1
    else:
        row[1] = 2
    #check Astigmastism
    if row[2] == 'Yes':
        row[2] = 1
    else:
        row[2] = 2
    #check TPR
    if row[3] == 'Normal':
        row[3] = 1
    else:
        row[3] = 2
    

X = [row[:-1] for row in db]

# transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2
# --> addd your Python code here
Y = []
for row in db:
    if row[-1] == 'Yes':
        Y.append(1)
    else:
        Y.append(2)

# fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X, Y)

# plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=[
               'Yes', 'No'], filled=True, rounded=True)
plt.show()
