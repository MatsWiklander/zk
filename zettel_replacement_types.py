import re
from datetime import date

import click

from zettel_types import BaseZettel


def fetch_all_zettel_replacement_types():
    all_zettel_replacement_types = {zettel_replacement_class().snake_case(): zettel_replacement_class for
                                    zettel_replacement_class in
                                    BaseZettelReplacement.__subclasses__()}
    return all_zettel_replacement_types


class BaseZettelReplacement:
    def __init__(self):
        pass

    def snake_case(self):
        name = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', self.__class__.__name__[0:-17])
        return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name).lower()


class TodayZettelReplacement(BaseZettelReplacement):
    def __init__(self):
        super().__init__()

    def apply(self, zettel: BaseZettel):
        click.echo(zettel.raw)
        found = re.findall('.*today.*', zettel.raw)
        click.echo('---')
        click.echo(found)
        click.echo('---')
        zettel.raw = re.sub(r'{{.*?' + self.snake_case() + r'.*?}}', date.today().isoformat(), zettel.raw)
