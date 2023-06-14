import pandas as pd
import pandera as pa
import logging
from pandera.typing import DataFrame
from data_schemas import MunicipalitiesPopulation


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
