import seaborn as sns
import matplotlib.pyplot as plt
genre = ["femme","femme","femme","femme",
"homme","homme","homme","homme","homme","homme"]
sns.countplot(x=genre)
plt.show()
