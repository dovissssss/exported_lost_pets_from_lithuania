import pandas as pd

DIRECTORY = "../data/raw/Prarasti_isvezti_augintiniai.csv"

# prideti Pandera


def read_dataset() -> pd.DataFrame:
    df = pd.read_csv(
        DIRECTORY,
        delimiter=";",
        skiprows=1,
        names=["export_lost_types", "export_country", "municipality",
               "ward", "area", "pet_type", "year", "pet_count"],
        dtype={"export_lost_types": "string",
               "export_country": "string",
               "municipality": "string",
               "ward": "string",
               "area": "string",
               "pet_type": "string",
               "year": "int64",
               "pet_count": "int64"
               })
    return df


def count_exported_pets_sum_by_year(df: pd.DataFrame) -> pd.DataFrame:
    """Function Returns From Lithuania Exported Pets Number by Type and Year"""
    exported_pets_by_year = df[df["export_lost_types"] == "Išvežimas"].groupby(
        ["year", "pet_type"], as_index=False)["pet_count"].sum()
    return exported_pets_by_year  # type: ignore


def count_lost_pets_sum_by_year(df: pd.DataFrame) -> pd.DataFrame:
    """Function Returns Lost Pets Number In Lithuania by Type and Year"""
    lost_pets_by_year = df[df["export_lost_types"] == "Dingimas"].groupby(
        ["year", "pet_type"], as_index=False)["pet_count"].sum()
    return lost_pets_by_year  # type: ignore


def count_total_exported_n_lost_pets_by_type(df: pd.DataFrame) -> pd.DataFrame:
    lost_n_exported_pets = df.groupby(
        ["pet_type", "export_lost_types"], as_index=False)["pet_count"].sum()
    return lost_n_exported_pets  # type: ignore


def count_exported_pets_by_export_countries(df: pd.DataFrame) -> pd.DataFrame:
    exported_pets_by_countries = df[df["export_lost_types"] == "Išvežimas"].groupby(
        "export_country", as_index=False)["pet_count"].sum().sort_values('pet_count', ascending=False)  # type: ignore
    return exported_pets_by_countries


def count_exported_pets_by_lt_municipalities(df: pd.DataFrame) -> pd.DataFrame:
    exported_pets_by_lt_municipalities = df[df["export_lost_types"] == "Išvežimas"].groupby(
        "municipality", as_index=False)["pet_count"].sum().sort_values('pet_count', ascending=False)  # type: ignore
    return exported_pets_by_lt_municipalities


def get_to_how_many_unique_countries_pets_r_exported(df: pd.DataFrame) -> pd.DataFrame:
    export_countries_count = df[df["export_lost_types"] == "Išvežimas"].groupby(
        "year", as_index=False)["export_country"].nunique()
    return export_countries_count  # type: ignore


def get_exported_pets_sum_n_max_entries_by_year(df: pd.DataFrame) -> pd.DataFrame:
    exported_pets_sum_n_max_entries = df[df["export_lost_types"] == "Išvežimas"].groupby(
        "year", as_index=False)["pet_count"].agg(['sum', 'max', 'mean'])
    return exported_pets_sum_n_max_entries


# if __name__ == "__main__":
#     df = read_dataset()
#     df = count_exported_pets_sum_by_year(df)
#     df = count_lost_pets_sum_by_year(df)
#     df = count_total_exported_n_lost_pets_by_type(df)
#     df = count_exported_pets_by_lt_municipalities(df)
#     df = get_to_how_many_unique_countries_pets_r_exported(df)
#     df = get_exported_pets_sum_n_max_entries_by_year(df)
