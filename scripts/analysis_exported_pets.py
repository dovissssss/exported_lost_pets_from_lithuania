import pandas as pd
import logging


def group_exported_pets_by_year(df: pd.DataFrame) -> pd.DataFrame:
    # Group Lost Pets sum by year
    logging.info("Started the count for exported pets from Lithuania by year...")
    pets_by_year = (
        df[df["export_lost_types"] == "Išvežimas"]
        .groupby("year", as_index=False)["pet_count"]
        .agg(["sum"])
    )

    logging.info(f"Exported Pets from Lithuania by Year: {pets_by_year}")
    return pets_by_year


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


def count_to_how_many_unique_countries_pets_r_exported(
    df: pd.DataFrame,
) -> pd.DataFrame:
    logging.info("Started the unique count for export countries...")
    export_countries_count = (
        df[df["export_lost_types"] == "Išvežimas"]
        .groupby("year", as_index=False)["export_country"]
        .nunique()
    )
    logging.info(f"Unique Countries Count: {export_countries_count}")
    return export_countries_count  # type: ignore


def count_exported_pets_sum_n_max_entries_by_year(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Started the sum, max and mean calculations for pets by year...")
    exported_pets_sum_n_max_entries = (
        df[df["export_lost_types"] == "Išvežimas"]
        .groupby("year", as_index=False)["pet_count"]
        .agg(["sum", "max", "mean"])
    )
    logging.info(f"Sum, Max, Mean by year: {exported_pets_sum_n_max_entries}")
    return exported_pets_sum_n_max_entries
