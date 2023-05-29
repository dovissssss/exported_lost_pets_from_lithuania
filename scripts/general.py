import pandas as pd
import pandera as pa
import logging
from pandera.typing import DataFrame
from data_schemas import MunicipalitiesPopulation


def count_exported_pets_sum_by_year(df: pd.DataFrame) -> pd.DataFrame:
    """Function Returns From Lithuania Exported Pets Number by Type and Year"""
    logging.info("Started the count for exported pets from Lithuania by year...")
    exported_pets_by_year = (
        df[df["export_lost_types"] == "Išvežimas"]
        .groupby(["year", "pet_type"], as_index=False)["pet_count"]
        .sum()
    )
    logging.info(f"Exported Pets from Lithuania by Year: {exported_pets_by_year}")
    return exported_pets_by_year  # type: ignore


def count_lost_pets_sum_by_year(df: pd.DataFrame) -> pd.DataFrame:
    """Function Returns Lost Pets Number In Lithuania by Type and Year"""
    logging.info("Started the count for lost pets from Lithuania by year...")
    lost_pets_by_year = (
        df[df["export_lost_types"] == "Dingimas"]
        .groupby(["year", "pet_type"], as_index=False)["pet_count"]
        .sum()
    )
    logging.info(f"Lost Pets from Lithuania by Year: {lost_pets_by_year}")
    return lost_pets_by_year  # type: ignore


def count_total_exported_n_lost_pets_by_type(df: pd.DataFrame) -> pd.DataFrame:
    logging.info(
        "Started the count for exported and lost pets from Lithuania by type..."
    )
    lost_n_exported_pets = df.groupby(
        ["pet_type", "export_lost_types"], as_index=False
    )["pet_count"].sum()
    logging.info(f"Pets Count by Type: {lost_n_exported_pets}")
    return lost_n_exported_pets  # type: ignore


def count_exported_pets_by_export_countries(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Started the count for exported pets from Lithuania by country...")
    exported_pets_by_countries = (
        df[df["export_lost_types"] == "Išvežimas"]
        .groupby("export_country", as_index=False)["pet_count"]
        .sum()
        .sort_values("pet_count", ascending=False)
    )  # type: ignore
    logging.info(f"Exported Pets Count by Country: {exported_pets_by_countries}")
    return exported_pets_by_countries


def count_exported_pets_by_lt_municipalities(df: pd.DataFrame) -> pd.DataFrame:
    logging.info(
        "Started the count for exported pets from Lithuania by municipalities..."
    )
    exported_pets_by_lt_municipalities = (
        df[df["export_lost_types"] == "Išvežimas"]
        .groupby("municipality", as_index=False)["pet_count"]
        .sum()
        .sort_values("pet_count", ascending=False)
    )  # type: ignore
    logging.info(
        f"Exported Pets Count by Municipalities: {exported_pets_by_lt_municipalities}"
    )
    return exported_pets_by_lt_municipalities


def count_exported_pets_by_year_n_lt_municipalities(df: pd.DataFrame) -> pd.DataFrame:
    logging.info(
        "Started the count for exported pets from Lithuania by year and municipalities..."
    )
    exported_pets_by_year_n_lt_municipalities = (
        df[df["export_lost_types"] == "Išvežimas"]
        .groupby(["year", "municipality"], as_index=False)["pet_count"]
        .sum()
        .sort_values("pet_count", ascending=False)
    )  # type: ignore
    logging.info(
        f"Exported Pets Count by Year and Municipalities: {exported_pets_by_year_n_lt_municipalities}"
    )
    return exported_pets_by_year_n_lt_municipalities


def get_to_how_many_unique_countries_pets_r_exported(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Started the unique count for export countries...")
    export_countries_count = (
        df[df["export_lost_types"] == "Išvežimas"]
        .groupby("year", as_index=False)["export_country"]
        .nunique()
    )
    logging.info(f"Unique Countries Count: {export_countries_count}")
    return export_countries_count  # type: ignore


def get_exported_pets_sum_n_max_entries_by_year(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Started the sum, max and mean calculations for pets by year...")
    exported_pets_sum_n_max_entries = (
        df[df["export_lost_types"] == "Išvežimas"]
        .groupby("year", as_index=False)["pet_count"]
        .agg(["sum", "max", "mean"])
    )
    logging.info(f"Sum, Max, Mean by year: {exported_pets_sum_n_max_entries}")
    return exported_pets_sum_n_max_entries


def unpivot_municipalities_population_dataset(
    df_external: pd.DataFrame,
) -> pd.DataFrame:
    df_external_unpivoted = df_external.melt(
        ignore_index=False, var_name="municipality", value_name="population"
    )
    return df_external_unpivoted


@pa.check_types()
def merge_with_municipalities_population_dataset() -> (
    DataFrame[MunicipalitiesPopulation]
):
    logging.info(
        "Started the merge between exported pets dataset and municipalities population dataset..."
    )
    df_merged = count_exported_pets_by_year_n_lt_municipalities.merge(
        unpivot_municipalities_population_dataset,
        how="left",
        on=["year", "municipality"],
    )
    df_merged = df_merged.assign(
        pets_per_population=df_merged["pet_count"] / df_merged["population"]
    )
    return df_merged


# if __name__ == "__main__":
#     df = read_dataset()
#     df = count_exported_pets_sum_by_year(df)
#     df = count_lost_pets_sum_by_year(df)
#     df = count_total_exported_n_lost_pets_by_type(df)
#     df = count_exported_pets_by_lt_municipalities(df)
#     df = get_to_how_many_unique_countries_pets_r_exported(df)
#     df = get_exported_pets_sum_n_max_entries_by_year(df)
