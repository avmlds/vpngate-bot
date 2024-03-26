HOSTNAME = "HostName"
IP = "IP"
SCORE = "Score"
PING = "Ping"
SPEED = "Speed"
COUNTRYLONG = "CountryLong"
COUNTRYSHORT = "CountryShort"
NUMVPNSESSIONS = "NumVpnSessions"
UPTIME = "Uptime"
TOTALUSERS = "TotalUsers"
TOTALTRAFFIC = "TotalTraffic"
LOGTYPE = "LogType"
OPERATOR = "Operator"
MESSAGE = "Message"
OPENVPN_CONFIGDATA_BASE64 = "OpenVPN_ConfigData_Base64"

FIELDS = [
    HOSTNAME,
    IP,
    SCORE,
    PING,
    SPEED,
    COUNTRYLONG,
    COUNTRYSHORT,
    NUMVPNSESSIONS,
    UPTIME,
    TOTALUSERS,
    TOTALTRAFFIC,
    LOGTYPE,
    OPERATOR,
    MESSAGE,
    OPENVPN_CONFIGDATA_BASE64,
]

WELCOME_MESSAGE_TEMPLATE = """
vpngate.net Proxy

Use L2TP/IPsec to connect to a VPN server.
Login and password are: `vpn`
Data is updated every 2 hours.
Response contains 60 server addresses sorted by score.
To get servers use command /get
"""
