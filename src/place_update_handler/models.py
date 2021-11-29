from typing import Optional

from pydantic import BaseModel


class PlaceUpdateEvent(BaseModel):
    name: str
    address: str
    business_hours: dict[str, str]
    photo_link: Optional[str] = None
    rate: Optional[str] = None
    reviews: Optional[str] = None
    extra_attrs: dict[str, str]
    traits: dict[str, list[str]]
