from pydantic import BaseModel, Field, computed_field
from typing import Annotated,List,Optional

CoordPair = Annotated[list[float],Field(
  ...,max_length=2,min_length=2
)]

class coords_val(BaseModel):
  coord_list: Annotated[List[CoordPair],Field(
    ..., min_length=3, 
    description="The coordinates of the vertices (in [[x,y]] format)",
    examples=[
      [[1,2],[4,5],[9,4]], [[5,4],[-4,-1],[4,-4],[7,1]]
    ]
  )]
  assume_unordered: Annotated[Optional[bool],Field(
    description="If `True`," \
    " it will use an experimental function to order the provided vertices of the polygon in CCW or CW orientation."
  )] = False

  @computed_field(return_type=int)
  @property
  def n_vertices(self) -> int:
    n_poly:int = len(self.coord_list)
    return n_poly