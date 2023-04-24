import pandas as pd
from general import count_exported_pets_sum_by_year


def test_count_exported_pets_sum_by_year():
    df = pd.DataFrame(
        {
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
