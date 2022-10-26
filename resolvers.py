from ariadne import QueryType, MutationType
from database import Hydro


query = QueryType()
mutation = MutationType()


@query.field("get_hydro")
def resolve_get_hydro(_, info, location):
    """Queries all hydroponics datapoints by location string"""
    return Hydro.query.filter_by(location=location).all()


@query.field("get_all_hydro")
def resolve_get_all_hydro(_, info):
    """Queries all hydroponics datapoints"""
    return Hydro.query.all()


@mutation.field("create_hydro")
def resolve_create_hydro(
    _, info, location, water_temp, air_temp, tds, humidity, **kwargs
):
    """Creates a new hydroponics datapoint in the database"""
    # TODO: Fix kwargs, use more proper optional resolver var
    ph = kwargs.get("ph", -20.0)
    hydro = Hydro.create(location, water_temp, air_temp, tds, humidity, ph)
    return hydro
