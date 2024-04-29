from datetime import datetime
from typing import Optional, Self
from pydantic import BaseModel, ConfigDict, model_validator

from src.exceptions.input_error import InputError

class TripSchema(BaseModel):
    destination:  Optional[str] = None
    departure_date:  Optional[str] = None
    return_date:  Optional[str] = None
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "destination": "France",
                "departure_date": "2025-04-26",
                "return_date": "2025-04-28",
            }
        },
    )

    @model_validator(mode='after')
    def check_valid_dates(self) -> Self:
        date1 = self.parse_date(self.departure_date)
        date2 = self.parse_date(self.return_date)
        if date1 > date2:
            raise InputError("Return date is before departure date")
        return self

    def parse_date(self, value):
        try:
            return datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Expected format: YYYY-MM-DD")