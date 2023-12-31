import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
df = pd.read_csv('tennis_stats.csv')
print(df.head())

# perform exploratory analysis here:
plt.scatter(df[['BreakPointsOpportunities']], df[['Wins']], alpha=0.4)

plt.show()
plt.clf()

## perform single feature linear regressions here:
features = df[['BreakPointsOpportunities']]
outcome = df[['Winnings']]

features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8, test_size = 0.2)

model = LinearRegression()
model.fit(features_train, outcome_train)

#print('Training accuracy:')
#print(model.score(features_train, outcome_train))
#print('Test accuracy:')
#print(model.score(features_test, outcome_test))

prediction = model.predict(features_test)
plt.scatter(outcome_test, prediction, alpha = 0.4)

plt.title('Predicted Winnings vs. Actual Winnings - 1 Feature')
plt.xlabel('Actual Winnings')
plt.ylabel('Predicted Winnings')
plt.show()
plt.clf()

## perform two feature linear regressions here:
features = df[['BreakPointsOpportunities', 'FirstServeReturnPointsWon']]
outcome = df[['Winnings']]

features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8, test_size = 0.2)

model = LinearRegression()
model.fit(features_train, outcome_train)

#print('Training accuracy:')
#print(model.score(features_train, outcome_train))
#print('Test accuracy:')
#print(model.score(features_test, outcome_test))

prediction = model.predict(features_test)
plt.scatter(outcome_test, prediction, alpha = 0.4)

plt.title('Predicted Winnings vs. Actual Winnings - 2 Features')
plt.xlabel('Actual Winnings')
plt.ylabel('Predicted Winnings')
plt.show()
plt.clf()

## perform multiple feature linear regressions here:
features = df[['Aces','FirstServe', 'FirstServePointsWon', 'BreakPointsFaced', 'BreakPointsSaved', 'ServiceGamesPlayed', 'TotalServicePointsWon', 'SecondServeReturnPointsWon', 'BreakPointsOpportunities','ReturnGamesPlayed', 'ReturnPointsWon', 'TotalPointsWon']]
outcome = df[['Winnings']]

features_train, features_test, outcome_train, outcome_test = train_test_split(features, outcome, train_size = 0.8, test_size = 0.2)

model = LinearRegression()
model.fit(features_train, outcome_train)

print('Training accuracy:')
print(model.score(features_train, outcome_train))
print('Test accuracy:')
print(model.score(features_test, outcome_test))

prediction = model.predict(features_test)
plt.scatter(outcome_test, prediction, alpha = 0.4)

plt.title('Predicted Winnings vs. Actual Winnings - Multiple Features')
plt.xlabel('Actual Winnings')
plt.ylabel('Predicted Winnings')
plt.show()
plt.clf()
