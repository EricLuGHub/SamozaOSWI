from enum import IntFlag, auto

class CEIO(IntFlag):
    CREATE   = 1 << 0  # C -> 1
    EXECUTE  = 1 << 1  # E -> 2
    INGEST   = 1 << 2  # I -> 4
    OBSERVE  = 1 << 3  # O -> 8

class WisActions:
    AUTH_CONNECTOR               = CEIO.CREATE
    HANDLE_CONNECTOR_CALLBACK    = CEIO.CREATE | CEIO.INGEST
    CONNECTOR_EXECUTE            = CEIO.EXECUTE
    GRANT_CEIO_PERMISSIONS       = CEIO.CREATE