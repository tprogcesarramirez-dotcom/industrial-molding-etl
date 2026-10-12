from typing import List, Optional
from pydantic import BaseModel, Field

class MoldingReport(BaseModel):
    machine_id: Optional[str] = Field(
        default=None, 
        description="Identificador de la máquina (ej. M102)"
    )
    downtime_minutes: Optional[int] = Field(
        default=None, 
        ge=0, 
        description="Tiempo total de paro en minutos"
    )
    approved_parts: Optional[int] = Field(
        default=None, 
        ge=0, 
        description="Número de piezas aprobadas"
    )
    rejected_parts: Optional[int] = Field(
        default=None, 
        ge=0, 
        description="Número de piezas rechazadas"
    )
    reasons: List[str] = Field(
        default_factory=list, 
        description="Lista de razones de paro o rechazo"
    )
    shift_leader: Optional[str] = Field(
        default=None, 
        description="Nombre del líder de turno"
    )
