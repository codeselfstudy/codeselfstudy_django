import json
import logging
from random import randint

logging.basicConfig(level=logging.DEBUG, filename="fixtures.log")
log = logging


def calculate_codewars_difficulty(rank):
    """
    One idea:

    kyu 8 -> level 1
    kyu 7 -> level 2
    kyu 6 -> level 3
    kyu 5 -> level 4
    kyu 4 -> level 5
    kyu 3 -> split between levels 6 and 7 (fewer people will reach this point than the lower levels)
    kyu 2 -> split between levels 8 and 9
    kyu 1 -> level 10
    """
    log.info(f"rank: {rank}")
    if rank:
        kyu = abs(rank)
    else:
        kyu = 0
    return {
        1: 10,
        2: randint(8, 9),
        3: randint(6, 7),
        4: 5,
        5: 4,
        6: 3,
        7: 2,
        8: 1,
        0: 0,
    }[kyu]


def create_codewars_obj(pk, puzzle):
    difficulty = calculate_codewars_difficulty(puzzle["rank"]["id"])
    return {
        "model": "puzzles.puzzle",
        "pk": pk,
        "fields": {
            "title": puzzle["name"],
            "is_active": True,
            "source": "Codewars",
            "difficulty": difficulty,
            "unsafe_description": puzzle["description"],
            "original_url": puzzle["url"],
            "original_raw_data": puzzle,
            "created_at": "2020-11-21T23:50:58.096Z",
            "updated_at": "2020-11-21T23:50:58.096Z",
        }
    }


def create_projecteuler_obj(pk, puzzle):
    difficulty = 0

    return {
        "model": "puzzles.puzzle",
        "pk": pk,
        "fields": {
            "title": puzzle["title"],
            "is_active": True,
            "source": "Project Euler",
            "difficulty": difficulty,
            "unsafe_description": puzzle["body"],
            "original_url": puzzle["url"],
            "original_raw_data": puzzle,
            "created_at": "2020-11-21T23:50:58.096Z",
            "updated_at": "2020-11-21T23:50:58.096Z",
        }
    }


if __name__ == "__main__":
    log.info("starting")
    with open("./full_mongo_dump_cw_and_pe.json", "r") as f:
        raw_contents = f.read()

    puzzles = json.loads(raw_contents)
    output = []
    failed = []
    for idx, p in enumerate(puzzles):
        log.info(f"processing puzzle #{idx}: {p['url']}")
        if p.get("source") == "codewars":
            fixture_data = create_codewars_obj(idx, p)
            output.append(fixture_data)
        elif p.get("source") == "projecteuler":
            fixture_data = create_projecteuler_obj(idx, p)
            output.append(fixture_data)
        else:
            failed.append({"idx": idx, "puzzle": p})

    with open("codewars_projecteuler_puzzles.json", "w") as f:
        f.write(json.dumps(output))

    with open("failed.json", "w") as f:
        f.write(json.dumps(failed))

