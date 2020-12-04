""" AOC Day 4 """
from __future__ import annotations

import dataclasses
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

    def is_simple_valid(self) -> Optional[SimpleValidPassport]:
        """
        If the passport is "simply valid", return a SimpleValidPassport instance of it
        else return None
        """
        if not (
            self.birth_year is None
            or self.issue_year is None
            or self.expiration_year is None
            or self.height is None
            or self.hair_color is None
            or self.eye_color is None
            or self.passport_id is None
        ):
            return SimpleValidPassport(**dataclasses.asdict(self))
        return None


@dataclass(frozen=True, order=True)
class SimpleValidPassport:
    """
    A passport that at least is at most only missing its country code
    """
    birth_year: str
    issue_year: str
    expiration_year: str
    height: str
    hair_color: str
    eye_color: str
    passport_id: str
    country_id: Optional[str]

    def is_valid(self) -> bool:
        """
        Does this passport meet all the requirements?
        """
        if len(self.birth_year) != 4:
            return False
        if not 1920 <= int(self.birth_year) <= 2002:
            return False

        if len(self.issue_year) != 4:
            return False
        if not 2010 <= int(self.issue_year) <= 2020:
            return False

        if len(self.expiration_year) != 4:
            return False
        if not 2020 <= int(self.expiration_year) <= 2030:
            return False

        match = re.match(r"^(\d+)(cm|in)$", self.height)
        if not match:
            return False
        try:
            hgt = int(match.groups()[0])
        except ValueError:
            return False

        if match.groups()[1] == "cm":
            if not 150 <= hgt <= 193:
                return False
        elif match.groups()[1] == "in":
            if not 59 <= hgt <= 76:
                return False
        else:
            return False

        if not re.match(r"#[0-9a-f]{6}", self.hair_color):
            return False

        if self.eye_color not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False

        if not re.match(r"^[0-9]{9}$", self.passport_id):
            return False

        return True


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
    total_valid = sum(
        bool(passport.is_simple_valid()) for passport in parse_file(filename)
    )
    return total_valid


def second(filename: Union[str, Path]) -> int:
    """
    Count all passports that follow all the many validation rules
    """
    total_valid = 0
    for passport in parse_file(filename):
        if passport.is_simple_valid():
            if passport.is_simple_valid().is_valid():
                total_valid += 1
    return total_valid
