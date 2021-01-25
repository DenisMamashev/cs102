import dataclasses
import math
import time
import typing as tp

from vkapi import config, session
from vkapi.exceptions import APIError

QueryParams = tp.Optional[tp.Dict[str, tp.Union[str, int]]]


@dataclasses.dataclass(frozen=True)
class FriendsResponse:
    count: int
    items: tp.Union[tp.List[int], tp.List[tp.Dict[str, tp.Any]]]


def get_friends(
    user_id: int,count: int = 5000,offset: int = 0,fields: tp.Optional[tp.List[str]] = None
) -> FriendsResponse:
    info = {
        "access_token": config.VK_CONFIG["access_token"],
        "v": config.VK_CONFIG["version"],
        "count": count,
        "user_id": user_id if user_id is not None else "",
        "fields": ",".join(fields) if fields is not None else "",
        "offset": offset,
    }
    response = session.get("friends.get", params=info)
    if "error" in response.json() or not response.ok:
        raise APIError(response.json()["error"]["error_msg"])
    else:
        return FriendsResponse(count=response.json()["response"]["count"],items=response.json()["response"]["items"],)


class MutualFriends(tp.TypedDict):
    id: int
    common_friends: tp.List[int]
    common_count: int


def get_mutual(
    source_uid: tp.Optional[int] = None,
    target_uid: tp.Optional[int] = None,
    target_uids: tp.Optional[tp.List[int]] = None,
    order: str = "",
    count: tp.Optional[int] = None,
    offset: int = 0,
    progress=None,
) -> tp.Union[tp.List[int], tp.List[MutualFriends]]:
    if target_uids is None:
        info = {
            "access_token": config.VK_CONFIG["access_token"],
            "v": config.VK_CONFIG["version"],
            "source_uid": source_uid if source_uid is not None else "",
            "target_uid": target_uid,
            "order": order,
        })
        response_json = session.get(f"friends.getMutual", params=info).json()
        if not session.get(f"friends.getMutual", params=info).ok or "error" in response_json:
            raise APIError(response_json["error"]["error_msg"])
        return response_json["response"]
    arr_mutual = []
    if progress is None:
        progress = lambda x: x
    for _ in progress(range(math.ceil(len(target_uids) / 100))):
        info = {
            "access_token": config.VK_CONFIG["access_token"],
            "v": config.VK_CONFIG["version"],
            "target_uids": ",".join(map(str, target_uids)),
            "order": order,
            "count": count if count is not None else "",
            "offset": offset + _ * 100,
        }
        response_file = session.get(f"friends.getMutual", params=info).json()
        if not session.get(f"friends.getMutual", params=info).ok or "error" in response_file:
            raise APIError(response_file["error"]["error_msg"])
        for temp in response_file["response"]:
            arr_mutual.append(MutualFriends(id=temp["id"],common_friends=temp["common_friends"],common_count=temp["common_count"],))
        if _ % 3 == 2:
            time.sleep(1)
    return arr_mutual
