import seaborn as sb
import matplotlib.pyplot as plt
import config
from read_datasets import read_exported_pets_dataset
from analysis_exported_pets import (
    count_exported_pets_sum_by_year,
    group_exported_pets_by_year,
    count_to_how_many_unique_countries_pets_r_exported,
)


df = read_exported_pets_dataset(config.EXPORTED_PETS_DATA)  # type: ignore


def plot_exported_pets_by_year_n_type():
    exported_pets_by_year_n_type = count_exported_pets_sum_by_year(df)
    # Plot Lost Pets sum by years, type
    sb.set(rc={"figure.figsize": (10, 5)})

    sb.barplot(
        x=exported_pets_by_year_n_type["year"],
        y=exported_pets_by_year_n_type["pet_count"],
        hue=exported_pets_by_year_n_type["pet_type"],
        palette="dark",
    )
    plt.title("Exported pets by year and type")
    plt.xlabel("year")
    plt.ylabel("pet_count")
    plt.savefig("./data/processed/exported_pets_by_year_n_type.png")


def plot_exported_pets_by_year():
    pets_by_year = group_exported_pets_by_year(df)
    # Pandas Plot()
    pets_by_year.plot(
        legend=False,
        figsize=(10, 5),
        c="green",
        marker="x",
        title="Exported Pets From Lithuania",
        xlabel="year",
        ylabel="pet_count",
    )
    plt.savefig("./data/processed/exported_pets_by_year.png")


def plot_unique_countries_count_by_year():
    unique_countries_by_year = count_to_how_many_unique_countries_pets_r_exported(df)
    # Plot count of unique countries by year
    unique_countries_by_year.plot(
        x="year",
        y="export_country",
        kind="bar",
        legend=False,
        figsize=(10, 6),
        title="Unique Export Countries Count By Year From Lithuania",
        xlabel="year",
        ylabel="countries_count",
    )
    plt.savefig("./data/processed/unique_countries_count_by_year.png")
