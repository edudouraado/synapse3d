"""Modelos compartilhados entre backend e frontend"""

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum


class EventType(str, Enum):
    HEATMAP = "heatmap"
    THEFT_ALERT = "theft_alert"
    CUSTOMER_ENTRY = "customer_entry"
    CUSTOMER_EXIT = "customer_exit"


class CameraBase(BaseModel):
    id: str
    name: str
    store_id: str
    rtsp_url: str
    position_x: float  # posição na planta 3D
    position_y: float
    position_z: float
    rotation_y: float  # rotação da câmera em graus


class CameraCreate(CameraBase):
    pass


class CameraResponse(CameraBase):
    class Config:
        from_attributes = True


class StoreBase(BaseModel):
    id: str
    name: str
    city: str
    address: str
    floor_plan_url: Optional[str] = None  # planta baixa da loja
    model_3d_url: Optional[str] = None    # modelo 3D da loja (GLTF/OBJ)


class StoreCreate(StoreBase):
    pass


class StoreResponse(StoreBase):
    class Config:
        from_attributes = True


class HeatmapPoint(BaseModel):
    x: float
    y: float
    intensity: float  # 0.0 a 1.0


class HeatmapData(BaseModel):
    store_id: str
    camera_id: str
    timestamp: datetime
    points: List[HeatmapPoint]


class TheftAlert(BaseModel):
    id: Optional[str] = None
    store_id: str
    camera_id: str
    timestamp: datetime
    confidence: float  # 0.0 a 1.0
    description: str
    image_url: Optional[str] = None


class CustomerEvent(BaseModel):
    store_id: str
    camera_id: str
    timestamp: datetime
    event_type: EventType
    count: int = 1
