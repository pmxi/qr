import json


def parse_qr_str(inp):
    out = inp.split(";")
    outd = {}
    for i in out:
        val = i.split("=")
        outd[val[0]] = val[1]
    return outd
