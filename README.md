Request arrives
        │
        ▼
FastAPI Router
        │
        ▼
SatelliteService
        │
        ▼
Do we already know the position?
        │
   ┌────┴────┐
   │         │
 Yes         No
   │         │
Return    Download TLE
             │
             ▼
      Calculate Orbit
             │
             ▼
        Save to Cache
             │
             ▼
      Return Position