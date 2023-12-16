import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
import math

df = pd.read_csv('diabetes.csv')

sns.countplot(x='Outcome', data=df)
print('Number of Outcome for each 0 and 1 are:\n',
      df['Outcome'].value_counts())


plt.subplots(figsize=(9, 9))
sns.heatmap(df.corr(), annot=True)


x = df.drop("Outcome", axis=1)
y = df.Outcome




from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)




model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid')) 
model.compile(loss='binary_crossentropy',
              optimizer='adam', metrics=['accuracy'])



model.fit(X_train, y_train, validation_data=(
    X_test, y_test), epochs=200, batch_size=10)



scores = model.evaluate(X_train, y_train)
print("Training Accuracy: %.2f%%\n" % (scores[1]*100))
scores = model.evaluate(X_test, y_test)
print("Testing Accuracy: %.2f%%\n" % (scores[1]*100))




man = np.array([[0, 350, 100, 50, 100, 32, 2, 56]])
out1 = model.predict(man)
print(out1)