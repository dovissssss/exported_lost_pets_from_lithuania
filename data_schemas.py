import pandera as pa
from pandera.typing import Series


class ExportedLostPets(pa.SchemaModel):
    export_lost_types: Series[str]
    export_country: Series[str] = pa.Field(nullable=True)
    municipality: Series[str]
    ward: Series[str] = pa.Field(nullable=True)
    area: Series[str]
    pet_type: Series[str]
    year: Series[int]
    pet_count: Series[int]


class MunicipalitiesPopulation(pa.SchemaModel):
    year: Series[int]
    municipality: Series[str]
    population: Series[int]
