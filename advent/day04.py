""" AOC Day 4 """
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Union

RENAME_MAP = {
    "byr": "birth_year",
    "iyr": "issue_year",
    "eyr": "expiration_year",
    "hgt": "height",
    "hcl": "hair_color",
    "ecl": "eye_color",
    "pid": "passport_id",
    "cid": "country_id",
}


def _is_valid_year(year: str, left: int, right: int) -> bool:
    if not re.fullmatch(r"\d{4}", year):
        return False
    return left <= int(year) <= right


@dataclass(frozen=True, order=True)
class PotentialPassport:
    """
    A representation of the raw data
    """

    birth_year: Optional[int] = None
    issue_year: Optional[int] = None
    expiration_year: Optional[int] = None
    height: Optional[str] = None
    hair_color: Optional[str] = None
    eye_color: Optional[str] = None
    passport_id: Optional[int] = None
    country_id: Optional[int] = None

    @classmethod
    def parse(cls, datum: List[str]) -> PotentialPassport:
        """ Parse a passport from its raw representation """
        passport = {dat.split(":")[0]: dat.split(":")[1] for dat in datum}
        passport = {RENAME_MAP.get(key, key): val for key, val in passport.items()}
        return PotentialPassport(**passport)

    def is_simple_valid(self) -> bool:
        """
        If the passport is "simply valid" return True, else False
        """
        return not (
            self.birth_year is None
            or self.issue_year is None
            or self.expiration_year is None
            or self.height is None
            or self.hair_color is None
            or self.eye_color is None
            or self.passport_id is None
        )

    def is_valid(self) -> bool:
        """
        Does this passport meet all the requirements?
        """
        if not self.is_simple_valid():
            return False

        match = re.fullmatch(r"(\d+)(cm|in)", self.height)
        if not match:
            return False
        hgt = int(match.groups()[0])

        if match.groups()[1] == "cm":
            if not 150 <= hgt <= 193:
                return False
        else:
            if not 59 <= hgt <= 76:
                return False

        return bool(
            _is_valid_year(self.birth_year, 1920, 2002)
            and _is_valid_year(self.issue_year, 2010, 2020)
            and _is_valid_year(self.expiration_year, 2020, 2030)
            and re.fullmatch(r"#[0-9a-f]{6}", self.hair_color)
            and self.eye_color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            and re.fullmatch(r"[0-9]{9}$", self.passport_id)
        )


def parse_file(filename: Union[str, Path]) -> List[PotentialPassport]:
    """
    Parse a file into a list of potential passports
    """
    data = []
    datum = []
    with open(filename, "rt") as infile:
        for line in infile:
            line = re.sub(r"\s+", " ", line.strip())
            if not line:
                if datum:
                    data.append(datum)
                    datum = []
                    continue
            else:
                datum.extend(line.split(" "))
    if datum:
        data.append(datum)

    return [PotentialPassport.parse(datum) for datum in data]


def first(filename: Union[str, Path]) -> int:
    """
    Count all passports that are at most missing a country_id
    """
    total_valid = sum(passport.is_simple_valid() for passport in parse_file(filename))
    return total_valid


def second(filename: Union[str, Path]) -> int:
    """
    Count all passports that follow all the many validation rules
    """
    return sum(passport.is_valid() for passport in parse_file(filename))
