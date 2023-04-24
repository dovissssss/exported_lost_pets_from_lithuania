import pandas as pd
from general import count_exported_pets_sum_by_year, count_lost_pets_sum_by_year, count_total_exported_n_lost_pets_by_type


def test_count_exported_pets_sum_by_year():
    df = pd.DataFrame(
        {
            "Išvežimo, praradimo pavadinimas": ["Išvežimas", "Išvežimas", "Išvežimas"],
            " Išvežimo praradimo metai": ["2022", "2022", "2023"],
            " Gyvūno augintinio rūšies pavadinimas": ["Šuo", "Šuo", "Katė"],
            " Gyvūnų augintinių skaičius": [100, 150, 300],
        }
    )
    df_expected = pd.DataFrame(
        {
            " Išvežimo praradimo metai": ["2022", "2023"],
            " Gyvūno augintinio rūšies pavadinimas": ["Šuo", "Katė"],
            " Gyvūnų augintinių skaičius": [250, 300],
        }
    )
    result = count_exported_pets_sum_by_year(df)
    pd.testing.assert_frame_equal(result, df_expected, check_dtype=False)


def test_count_lost_pets_sum_by_year():
    df = pd.DataFrame(
        {
            "Išvežimo, praradimo pavadinimas": ["Dingimas", "Dingimas", "Išvežimas"],
            " Išvežimo praradimo metai": ["2022", "2023", "2023"],
            " Gyvūno augintinio rūšies pavadinimas": ["Šuo", "Katė", "Katė"],
            " Gyvūnų augintinių skaičius": [10, 50, 3],
        }
    )
    df_expected = pd.DataFrame(
        {
            " Išvežimo praradimo metai": ["2022", "2023"],
            " Gyvūno augintinio rūšies pavadinimas": ["Šuo", "Katė"],
            " Gyvūnų augintinių skaičius": [10, 50],
        }
    )
    result = count_lost_pets_sum_by_year(df)
    pd.testing.assert_frame_equal(result, df_expected, check_dtype=False)


def test_count_total_exported_n_lost_pets_by_type():
    df = pd.DataFrame(
        {
            "Išvežimo, praradimo pavadinimas": ["Išvežimas", "Dingimas", "Dingimas"],
            " Gyvūno augintinio rūšies pavadinimas": ["Šuo", "Katė", "Katė"],
            " Gyvūnų augintinių skaičius": [10, 50, 3],
        }
    )
    df_expected = pd.DataFrame(
        {
            " Gyvūno augintinio rūšies pavadinimas": ["Katė", "Šuo"],
            "Išvežimo, praradimo pavadinimas": ["Dingimas", "Išvežimas"],
            " Gyvūnų augintinių skaičius": [53, 10],
        }
    )
    result = count_total_exported_n_lost_pets_by_type(df)
    pd.testing.assert_frame_equal(result, df_expected, check_dtype=False)
