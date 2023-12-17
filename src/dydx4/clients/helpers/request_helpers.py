from typing import Optional, Any, Dict
import json
import random

from datetime import datetime

import dateutil.parser as dp


# def generate_query_path(url, params):
def generate_query_path(url: str, params: Dict) -> str:
    entries = params.items()
    if not entries:
        return url

    params_string = "&".join(
        f"{x[0]}={str(x[1]).lower() if isinstance(x[1], bool) else x[1]}"
        for x in entries
        if x[1] is not None
    )
    if params_string:
        return url + "?" + params_string

    return url


def json_stringify(data: Dict[str, Any]) -> str:
    return json.dumps(data, separators=(",", ":"))


def random_client_id() -> str:
    return str(int(float(str(random.random())[2:])))


def generate_now_iso() -> str:
    return (
        datetime.utcnow().strftime(
            "%Y-%m-%dT%H:%M:%S.%f",
        )[:-3]
        + "Z"
    )


def iso_to_epoch_seconds(iso: str) -> float:
    return dp.parse(iso).timestamp()


def epoch_seconds_to_iso(epoch: float) -> str:
    return (
        datetime.utcfromtimestamp(epoch).strftime(
            "%Y-%m-%dT%H:%M:%S.%f",
        )[:-3]
        + "Z"
    )


def remove_nones(original: Dict[str, Any]) -> Dict[str, Any]:
    return {k: v for k, v in original.items() if v is not None}
