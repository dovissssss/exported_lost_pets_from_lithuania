import pandas as pd

DIRECTORY = "../data/raw/Prarasti_isvezti_augintiniai.csv"


def read_dataset() -> pd.DataFrame:
    df = pd.read_csv(
        DIRECTORY,
        delimiter=";",
        dtype={" Išvežimo, praradimo pavadinimas": "string",
               " Šalies pavadinimas": "string",
               " Gyvūnų augintinio laikymo vietos savivaldybės pavadinimas": "string",
               " Gyvūnų augintinio laikymo vietos seniūnijos pavadinimas": "string",
               " Gyvūnų augintinio laikymo vietos vietovės pavadinimas": "string",
               " Gyvūno augintinio rūšies pavadinimas": "string",
               " Išvežimo praradimo metai": "int64",
               " Gyvūnų augintinių skaičius": "int64"
               })
    return df


def count_exported_pets_sum_by_year(df) -> pd.DataFrame:
    """Function Returns From Lithuania Exported Pets Number by Type and Year"""
    exported_pets_by_year = df[df["Išvežimo, praradimo pavadinimas"] == "Išvežimas"].groupby(
        [" Išvežimo praradimo metai", " Gyvūno augintinio rūšies pavadinimas"], as_index=False)[" Gyvūnų augintinių skaičius"].sum()
    return exported_pets_by_year


def count_lost_pets_sum_by_year(df) -> pd.DataFrame:
    """Function Returns Lost Pets Number In Lithuania by Type and Year"""
    lost_pets_by_year = df[df["Išvežimo, praradimo pavadinimas"] == "Dingimas"].groupby(
        [" Išvežimo praradimo metai", " Gyvūno augintinio rūšies pavadinimas"], as_index=False)[" Gyvūnų augintinių skaičius"].sum()
    return lost_pets_by_year


def count_total_exported_n_lost_pets_by_type(df) -> pd.DataFrame:
    lost_n_exported_pets = df.groupby(
        [" Gyvūno augintinio rūšies pavadinimas", "Išvežimo, praradimo pavadinimas"], as_index=False)[" Gyvūnų augintinių skaičius"].sum()
    return lost_n_exported_pets


def count_exported_pets_by_export_countries(df) -> pd.DataFrame:
    exported_pets_by_countries = df[df["Išvežimo, praradimo pavadinimas"] == "Išvežimas"].groupby(
        " Šalies pavadinimas", as_index=False)[" Gyvūnų augintinių skaičius"].sum().sort_values(' Gyvūnų augintinių skaičius', ascending=False)
    return exported_pets_by_countries


def count_exported_pets_by_lt_municipalities(df) -> pd.DataFrame:
    exported_pets_by_lt_municipalities = df[df["Išvežimo, praradimo pavadinimas"] == "Išvežimas"].groupby(
        " Gyvūnų augintinio laikymo vietos savivaldybės pavadinimas", as_index=False)[" Gyvūnų augintinių skaičius"].sum().sort_values(' Gyvūnų augintinių skaičius', ascending=False)
    return exported_pets_by_lt_municipalities


def get_to_how_many_unique_countries_pets_r_exported(df) -> pd.DataFrame:
    export_countries_count = df[df["Išvežimo, praradimo pavadinimas"] == "Išvežimas"].groupby(
        " Išvežimo praradimo metai", as_index=False)[" Šalies pavadinimas"].nunique()
    return export_countries_count


def get_exported_pets_sum_n_max_entries_by_year(df) -> pd.DataFrame:
    exported_pets_sum_n_max_entries = df[df["Išvežimo, praradimo pavadinimas"] == "Išvežimas"].groupby(
        " Išvežimo praradimo metai", as_index=False)[" Gyvūnų augintinių skaičius"].agg(['sum', 'max', 'mean'])
    return exported_pets_sum_n_max_entries


# if __name__ == "__main__":
#     df = read_dataset()
#     df = count_exported_pets_sum_by_year(df)
#     df = count_lost_pets_sum_by_year(df)
#     df = count_total_exported_n_lost_pets_by_type(df)
#     df = count_exported_pets_by_lt_municipalities(df)
#     df = get_to_how_many_unique_countries_pets_r_exported(df)
#     df = get_exported_pets_sum_n_max_entries_by_year(df)
