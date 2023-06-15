# Isveztu/Dingusiu is Lietuvos gyvunu analize


```
project/
├── data/
│ ├── raw/
│ ├── processed/
│ └── interim/
├── notebooks/
├── scripts/
├── output/
├── README.md
└── requirements.txt
```


Source: https://data.gov.lt/dataset/293/download/13457/Prarasti_isvezti_augintiniai%202023-04-01%2008.00.00.csv

External Data Source:https://osp.stat.gov.lt/lt/statistiniu-rodikliu-analize?hash=a1f6bbd8-ce7e-4980-ba01-72567b3983d8

## Installation

First of all please install all required modules with:
```
pip install -r requirements.txt
```

with download_data function download the required data files for analysis:
```
python scripts/run.py --download_data
```

using visualize_all_charts function draw charts for the analysis:
```
python scripts/run.py ----visualize_all_charts
```

Questions:
* Exported Pets sum by years, type.
* Lost Pets sum by years, type.
* Exported/Lost Pets Total Sum throughout years.
* Total exported Pets by export countries.
* Lithuanian municipalities by total exported pets sum including all analysis period.
* To how many unique countries, each year pets are exported.
* Exported Pets sum, max entries and mean entries per year.
* Create logic to group data by counties (LT apskritys)
* Create time series forecating model for exported/lost pets
