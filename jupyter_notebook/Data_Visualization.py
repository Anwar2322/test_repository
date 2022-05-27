# Steps Involved in Data Visualization
#1. Import Libraries

import seaborn as sns
import matplotlib.pyplot as plt

#2. Set Theme
sns.set_theme(style="ticks",color_codes=True)

#3. import Data Set (you can also import your data)
titanic= sns.load_dataset("titanic")
# print(titanic)

#4. plot basic graph with 1 variable
sns.countplot(x="sex", data=titanic)
plt.show()

# #5. plot basic graph with 2 variables 
sns.countplot(x="sex", hue="class", data=titanic)
plt.show()

# 6. plot basic graph with 2 variables with title 
p= sns.countplot(x="sex", hue="class", data=titanic)
p.set_title("My First Count Plot")
plt.show()
