import seaborn as sb
import matplotlib.pyplot as plt
from read_datasets import read_exported_pets_dataset
import config


df = read_exported_pets_dataset(config.EXPORTED_PETS_DATA)  # type: ignore


def plot_exported_pets_by_year_n_type():
    # Plot Lost Pets sum by years, type
    dfr = (
        df[df["export_lost_types"] == "Išvežimas"]
        .groupby(
            ["year", "pet_type"],
            as_index=False,
        )["pet_count"]
        .sum()
    )

    sb.set(rc={"figure.figsize": (10, 5)})

    sb.barplot(
        x=dfr["year"],
        y=dfr["pet_count"],
        hue=dfr["pet_type"],
        palette="dark",
    )


plt.show()


def plot_exported_pets_by_year():
    # Pandas Plot()
    exported_pets_by_year = (
        df[df["export_lost_types"] == "Išvežimas"]
        .groupby("year", as_index=False)["pet_count"]
        .agg(["sum"])
    )
    exported_pets_by_year.plot(
        legend=False,
        figsize=(5, 3),
        c="green",
        marker="x",
        title="Exported Pets From Lithuania",
    )


def plot_unique_countries_count_by_year():
    unique_countries = (
        df[df["export_lost_types"] == "Išvežimas"]
        .groupby(["year"], as_index=True)["export_country"]
        .nunique()
    )
    unique_countries.plot.bar(legend=False, figsize=(5, 3))
