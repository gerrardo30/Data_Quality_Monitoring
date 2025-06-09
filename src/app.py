from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.sensor import Visitors

app = FastAPI()

@app.get("/")
def visit(date: str, store: str) -> JSONResponse:
    """
    Number of visitors for one day
    :param date: str
    :param store: str
    :return: JSONResponse
    """
    visitors = Visitors()
    try:
        nb_visit = 0
        for i_day in range(8, 20): # get number of visit hour by hour then add all to get nb visit for the day
            nb_visitors_hours = visitors.get_number_visitors(
                date, hour=i_day, store=store
            )
            if nb_visitors_hours != "null":
                nb_visit += int(nb_visitors_hours)

        return JSONResponse(content=nb_visit)

    except IndexError:
        return JSONResponse(
            content=f"Date invalide : {date}", status_code=400
        )

@app.get("/all_data_day_hour")
def visit(date: str) -> JSONResponse:
    """
    get all the data for a specific day and hour
    :param date: str
    :return: JSONResponse
    """
    visitors = Visitors()
    try:
        return JSONResponse(content=visitors.get_all_data_day(date))

    except IndexError:
        return JSONResponse(
            content=f"Date invalide : {date}", status_code=400
        )