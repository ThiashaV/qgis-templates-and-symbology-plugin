
import dataclasses
import datetime
import enum
import json
import typing

from uuid import UUID, uuid4

from qgis.PyQt import (
    QtCore
)

from qgis.core import QgsDateTimeRange, QgsRectangle


@dataclasses.dataclass
class SpatialExtent:
    coordinates: typing.List[int]
    crs: str


@dataclasses.dataclass
class TemporalExtent:
    """Temporal extent as defined by the STAC API"""
    interval: QgsDateTimeRange


@dataclasses.dataclass
class Properties:
    links: typing.List[str] = None
    thumbnail: str = None
    directory: str = None
    extension: str = None
    template_type: str = None
    spatial: SpatialExtent = None
    temporal: TemporalExtent = None


@dataclasses.dataclass
class Template:

    id: UUID
    name: str
    title: str = None
    description: str = None
    license: str = None
    properties: Properties = None
    downloaded: bool = False
    download_path = str = None


@dataclasses.dataclass
class Symbology:

    id: UUID
    name: str
    title: str = None
    description: str = None
    license: str = None
    properties: Properties = None
    downloaded: bool = False
    download_path = str = None

