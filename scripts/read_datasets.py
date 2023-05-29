import pandas as pd
import pandera as pa
import config
from pandera.typing import DataFrame
from data_schemas import ExportedLostPets


@pa.check_types()
def read_exported_pets_dataset() -> DataFrame[ExportedLostPets]:
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
