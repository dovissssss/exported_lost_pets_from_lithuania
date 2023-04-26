import pandas as pd
from general import count_exported_pets_sum_by_year, count_lost_pets_sum_by_year, count_total_exported_n_lost_pets_by_type


def test_count_exported_pets_sum_by_year():
    df = pd.DataFrame(
        {
            "export_lost_types": ["Išvežimas", "Išvežimas", "Išvežimas"],
            "year": ["2022", "2022", "2023"],
            "pet_type": ["Šuo", "Šuo", "Katė"],
            "pet_count": [100, 150, 300],
        }
    )
    df_expected = pd.DataFrame(
        {
            "year": ["2022", "2023"],
            "pet_type": ["Šuo", "Katė"],
            "pet_count": [250, 300],
        }
    )
    result = count_exported_pets_sum_by_year(df)
    pd.testing.assert_frame_equal(result, df_expected, check_dtype=False)


def test_count_lost_pets_sum_by_year():
    df = pd.DataFrame(
        {
            "export_lost_types": ["Dingimas", "Dingimas", "Išvežimas"],
            "year": ["2022", "2023", "2023"],
            "pet_type": ["Šuo", "Katė", "Katė"],
            "pet_count": [10, 50, 3],
        }
    )
    df_expected = pd.DataFrame(
        {
            "year": ["2022", "2023"],
            "pet_type": ["Šuo", "Katė"],
            "pet_count": [10, 50],
        }
    )
    result = count_lost_pets_sum_by_year(df)
    pd.testing.assert_frame_equal(result, df_expected, check_dtype=False)


def test_count_total_exported_n_lost_pets_by_type():
    df = pd.DataFrame(
        {
            "export_lost_types": ["Išvežimas", "Dingimas", "Dingimas"],
            "pet_type": ["Šuo", "Katė", "Katė"],
            "pet_count": [10, 50, 3],
        }
    )
    df_expected = pd.DataFrame(
        {
            "pet_type": ["Katė", "Šuo"],
            "export_lost_types": ["Dingimas", "Išvežimas"],
            "pet_count": [53, 10],
        }
    )
    result = count_total_exported_n_lost_pets_by_type(df)
    pd.testing.assert_frame_equal(result, df_expected, check_dtype=False)
