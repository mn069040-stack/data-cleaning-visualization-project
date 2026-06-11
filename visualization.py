import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


# ==========================
# Average Cutoff Comparison
# ==========================
def plot_category_comparison(df):

    categories = ["GEN", "OBC", "SC/ST"]

    values = [
        df["GEN"].mean(),
        df["OBC"].mean(),
        df["SC/ST"].mean()
    ]

    plt.figure(figsize=(8, 5))

    sns.barplot(
        x=categories,
        y=values
    )

    plt.title("Average GATE Cutoff by Category")
    plt.ylabel("Average Cutoff")

    plt.tight_layout()

    plt.savefig("category_comparison.png")

    plt.show()


# ==========================
# Year-wise Trend
# ==========================
def plot_yearly_trend(df):

    yearly = df.groupby("Year")[["GEN", "OBC", "SC/ST"]].mean()

    plt.figure(figsize=(10, 6))

    plt.plot(
        yearly.index,
        yearly["GEN"],
        marker="o",
        label="GEN"
    )

    plt.plot(
        yearly.index,
        yearly["OBC"],
        marker="o",
        label="OBC"
    )

    plt.plot(
        yearly.index,
        yearly["SC/ST"],
        marker="o",
        label="SC/ST"
    )

    plt.title("Year-wise GATE Cutoff Trend")

    plt.xlabel("Year")
    plt.ylabel("Average Cutoff")

    plt.legend()

    plt.tight_layout()

    plt.savefig("yearly_trend.png")

    plt.show()


# ==========================
# Top 10 Papers
# ==========================
def plot_top_papers(df):

    top = df.sort_values(
        by="GEN",
        ascending=False
    ).head(10)

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=top,
        x="GEN",
        y="Paper Name"
    )

    plt.title("Top 10 Papers by GEN Cutoff")

    plt.xlabel("GEN Cutoff")
    plt.ylabel("Paper Name")

    plt.tight_layout()

    plt.savefig("top_papers.png")

    plt.show()