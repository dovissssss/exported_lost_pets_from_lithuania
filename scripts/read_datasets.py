import pandas as pd
import config
from pandera.typing import DataFrame
from data_schemas import exported_lost_pets


def read_exported_pets_dataset() -> DataFrame[exported_lost_pets]:
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
    )
    return df  # type: ignore


def read_municipalities_population_dataset() -> pd.DataFrame:
    df_external = pd.read_excel(
        config.MUNICIPALITIES_POPULATION_DATA, index_col=0, skiprows=4
    )
    df_external.index.name = "year"
    return df_external
