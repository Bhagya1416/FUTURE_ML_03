import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "outputs/ranked_candidates.csv"
)

plt.figure(figsize=(10,5))

plt.bar(
    df["Candidate"],
    df["Final Score"]
)

plt.xticks(rotation=45)

plt.title(
    "Candidate Ranking"
)

plt.tight_layout()

plt.show()