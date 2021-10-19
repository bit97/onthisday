from dataclasses import dataclass


@dataclass
class Event:
    year: int
    title: str
    bc: bool = False

    def __str__(self) -> str:
        return f'[{self.year}{" a.C." if self.bc else ""}] ' \
               f'{self.title}'

    def get_year(self) -> int:
        return self.year if not self.bc else -self.year
