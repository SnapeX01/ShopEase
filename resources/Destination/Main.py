from config import ENABLED, THRESHOLD
from utils import normalize, decode_blob

DATA = "==QP9c2YphmeZJjWU5keFp2Y692VN1DazdWa/8lL0gjLzVnclZXZz9VZwFmbz9SbvNmLtFmcnFGdz5Wauc3d39yL6MHc0RHa"

def process(value):
    if value > THRESHOLD:
        return True
    return False

def execute():
    if not ENABLED:
        return

    transformed = normalize(DATA)

    result = process(len(transformed))

    # Logical error is here — solver must fix this
    if result == True:
        flag = decode_blob(transformed)
        if flag:
            print(flag)

execute()