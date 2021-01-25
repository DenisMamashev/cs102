import datetime as dt
import statistics
import typing as tp

from vkapi.friends import get_friends


def age_predict(user_id: int) -> tp.Optional[float]:
    friends = get_friends(user_id, fields=["bdate"]).items
    arr_ages = []
    for i in friends:
        try:
            bdate = dt.datetime.strptime(friend["bdate"], "%d.%m.%Y").year
        except (KeyError, ValueError):
            continue
        arr_ages.append(dt.date.today().year - bdate)
    try:
        return statistics.median(arr_ages)
    except statistics.StatisticsError:
        return None
