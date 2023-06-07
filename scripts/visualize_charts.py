import seaborn as sb
import matplotlib.pyplot as plt
from read_datasets import read_exported_pets_dataset
import config


df = read_exported_pets_dataset(config.EXPORTED_PETS_DATA)  # type: ignore


def count_exported_pets_by_year_n_type(df):
    dfr = (
        df[df["export_lost_types"] == "Išvežimas"]
        .groupby(
            ["year", "pet_type"],
            as_index=False,
        )["pet_count"]
        .sum()
    )
    return dfr


def plot_exported_pets_by_year_n_type(dfr):
    # Plot Lost Pets sum by years, type

    sb.set(rc={"figure.figsize": (10, 5)})

    sb.barplot(
        x=dfr["year"],
        y=dfr["pet_count"],
        hue=dfr["pet_type"],
        palette="dark",
    )


plt.savefig("exported_pets_by_year_n_type.png")


def group_exported_pets_by_year(df):
    # Group Lost Pets sum by year
    exported_pets_by_year = (
        df[df["export_lost_types"] == "Išvežimas"]
        .groupby("year", as_index=False)["pet_count"]
        .agg(["sum"])
    )

    return exported_pets_by_year


def plot_exported_pets_by_year(exported_pets_by_year):
    # Pandas Plot()
    exported_pets_by_year.plot(
        legend=False,
        figsize=(5, 3),
        c="green",
        marker="x",
        title="Exported Pets From Lithuania",
    )

    plt.savefig("exported_pets_by_year.png")


def count_unique_countries_by_year(df):
    # Calculate count of unique countries by year
    unique_countries = (
        df[df["export_lost_types"] == "Išvežimas"]
        .groupby(["year"], as_index=True)["export_country"]
        .nunique()
    )

    return unique_countries


def plot_unique_countries_count_by_year(unique_countries):
    # Plot count of unique countries by year
    unique_countries.plot.bar(legend=False, figsize=(5, 3))

    plt.savefig("unique_countries_count_by_year.png")
