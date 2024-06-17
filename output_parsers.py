from langchain.output_parsers import (
    PydanticOutputParser,
)  # external library to access Pydantic
from pydantic import BaseModel, Field
from typing import List


class PersonIntel(BaseModel):
    summary: str = Field("description on who this person is")
    facts: List[str] = Field("interesting facts on this person")
    topics_of_interest: List[str] = Field("topics this person is interested in")
    ice_breakers: List[str] = Field(
        "ice breakers to start a converstation with this person"
    )

    def to_dict(self):
        dict = {
            "summary": self.summary,
            "facts": self.facts,
            "topics_of_interest": self.topics_of_interest,
            "ice_breakers": self.ice_breakers,
        }
        return dict


person_intel_parser: PydanticOutputParser = PydanticOutputParser(
    pydantic_object=PersonIntel
)
