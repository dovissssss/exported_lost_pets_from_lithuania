import pandas as pd
import config


def read_exported_pets_dataset() -> pd.DataFrame:
    df = pd.read_csv(
        config.EXPORTED_PETS_DATA,
        delimiter=";",
        skiprows=1,
        names=[
            "export_lost_types",
            "export_country",
            "municipality",
            "ward",
            "area",
            "pet_type",
            "year",
            "pet_count",
        ],
        dtype={
            "export_lost_types": "string",
            "export_country": "string",
            "municipality": "string",
            "ward": "string",
            "area": "string",
            "pet_type": "string",
            "year": "int64",
            "pet_count": "int64",
        },
    )
    return df


def read_municipalities_population_dataset() -> pd.DataFrame:
    df_external = pd.read_excel(
        config.MUNICIPALITIES_POPULATION_DATA, index_col=0, skiprows=4
    )
    df_external.index.name = "year"
    return df_external
