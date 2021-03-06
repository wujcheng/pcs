from __future__ import (
    absolute_import,
    division,
    print_function,
)

LOG_FILE = "/var/log/pcsd/pcs_snmp_agent.log"
ENTERPRISES_OID = "1.3.6.1.4.1"
PACEMAKER_OID = ENTERPRISES_OID + ".32723"
PCS_OID = PACEMAKER_OID + ".100"
DEFAULT_UPDATE_INTERVAL = 30
