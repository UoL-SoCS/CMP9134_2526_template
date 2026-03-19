"""
Ground Control Station — FastAPI application entry point.

This is a minimal scaffold. Students should implement full functionality:
"""

import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from robot_client import robot, RobotConnectionError

ROBOT_API_URL = os.getenv("ROBOT_API_URL", "http://localhost:5000")
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

logging.basicConfig(level=LOG_LEVEL.upper())
logger = logging.getLogger(__name__)


# ── App ────────────────────────────────────────────────────────────────────

app = FastAPI(
    title="Ground Control Station",
    description="CMP9134 — Robot Management System scaffold",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Health check ───────────────────────────────────────────────────────────


@app.get("/health", include_in_schema=False)
def health():
    return {"status": "ok"}


# ── Example: robot status ──────────────────────────────────────────────────
# TODO: add authentication, RBAC, and mission logging around these endpoints.


@app.get("/api/status")
async def get_status():
    """Proxy the robot status. Replace/extend with your own logic."""
    try:
        return await robot.get_status()
    except RobotConnectionError as exc:
        return {"error": str(exc)}


# ── TODO: add your routes below ────────────────────────────────────────────
# Example route skeletons:
#
# @app.post("/api/move")
# async def move(x: int, y: int):
#     ...
#
# @app.websocket("/ws/telemetry")
# async def ws_telemetry(websocket: WebSocket):
#     ...
