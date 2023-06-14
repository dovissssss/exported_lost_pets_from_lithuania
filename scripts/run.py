from read_datasets import download_data_files
from visualize_charts import (
    plot_exported_pets_by_year_n_type,
    plot_exported_pets_by_year,
    plot_unique_countries_count_by_year,
)


def visualize_charts():
    plot_exported_pets_by_year_n_type()
    plot_exported_pets_by_year()
    plot_unique_countries_count_by_year()


if __name__ == "__main__":
    download_data = download_data_files()
    visualize_all_charts = visualize_charts()
