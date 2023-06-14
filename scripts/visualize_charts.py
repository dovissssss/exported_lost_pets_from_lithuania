import seaborn as sb
import matplotlib.pyplot as plt
from read_datasets import read_exported_pets_dataset
from analysis_exported_pets import (
    count_exported_pets_sum_by_year,
    group_exported_pets_by_year,
    count_to_how_many_unique_countries_pets_r_exported,
)
import config


df = read_exported_pets_dataset(config.EXPORTED_PETS_DATA)  # type: ignore

exported_pets_by_year_n_type = count_exported_pets_sum_by_year(df)


def plot_exported_pets_by_year_n_type(exported_pets_by_year_n_type):
    # Plot Lost Pets sum by years, type

    sb.set(rc={"figure.figsize": (10, 5)})

    sb.barplot(
        x=exported_pets_by_year_n_type["year"],
        y=exported_pets_by_year_n_type["pet_count"],
        hue=exported_pets_by_year_n_type["pet_type"],
        palette="dark",
    )


plt.savefig("exported_pets_by_year_n_type.png")

pets_by_year = group_exported_pets_by_year(df)


def plot_exported_pets_by_year(pets_by_year):
    # Pandas Plot()
    pets_by_year.plot(
        legend=False,
        figsize=(5, 3),
        c="green",
        marker="x",
        title="Exported Pets From Lithuania",
    )

    plt.savefig("exported_pets_by_year.png")


unique_coutries_by_year = count_to_how_many_unique_countries_pets_r_exported(df)


def plot_unique_countries_count_by_year(unique_coutries_by_year):
    # Plot count of unique countries by year
    unique_coutries_by_year.plot.bar(legend=False, figsize=(5, 3))

    plt.savefig("unique_countries_count_by_year.png")
