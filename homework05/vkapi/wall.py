import textwrap
import time
import typing as tp
from string import Template
import math

import pandas as pd
from pandas import json_normalize

from vkapi import config, session
from vkapi.exceptions import APIError


def get_posts_2500(
    owner_id: str = "",
    domain: str = "",
    offset: int = 0,
    count: int = 10,
    max_count: int = 2500,
    filter: str = "owner",
    extended: int = 0,
    fields: tp.Optional[tp.List[str]] = None,
) -> tp.Dict[str, tp.Any]:

    # FMT off
    script = f"""
    var i = 0; 
    var result = [];
    while (i < {max_count}){{
        if ({offset}+i+100 > {count}){{
            result.push(API.wall.get({{
            "owner_id": "{owner_id}",
            "domain": "{domain}",
            "offset": "{offset} +i",
            "count": "{count}-(i+{offset})",
            "filter": "{filter}",
            "extended": "{extended}",
            "fields": "{fields}"
        }}));
    }} 
    result.push(API.wall.get({{
            "owner_id": "{owner_id}",
            "domain": "{domain}",
            "offset": "{offset} +i",
            "count": "{count}",
            "filter": "{filter}",
            "extended": "{extended}",
            "fields": "{fields}"
        }}));
        i = i + {max_count};
    }}
    return result;
    """

    # FMT: on
    info = {"code": script,"access_token": config.VK_CONFIG["access_token"],"v": config.VK_CONFIG["version"],}
    response_json = session.post("execute", data=info).json()
    if "error" in response_json or not session.post("execute", data=info).ok:
        raise APIError(response_json["error"]["error_msg"])
    return response_json["response"]["items"]


def get_wall_execute(
    owner_id: str = "",
    domain: str = "",
    offset: int = 0,
    count: int = 10,
    max_count: int = 2500,
    filter: str = "owner",
    extended: int = 0,
    fields: tp.Optional[tp.List[str]] = None,
    progress=None,
) -> pd.DataFrame:
    wall_execute = pd.DataFrame()
    if progress is None:
        progress = lambda x: x
    num=math.ceil(count / 2500)
    for i in progress(range(num)):
        wall_execute = wall_execute.append(json_normalize(get_posts_2500(owner_id, domain, offset, count, max_count, filter, extended, fields)))
        time.sleep(1)
    return wall_execute
