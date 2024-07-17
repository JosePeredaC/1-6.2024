import asyncio
import websockets
import json
import requests
import time
import re
import base64
import random
import string


async def connect_to_websocket(pin, nickname, session_data):
    uri = f"wss://kahoot.it/cometd/{pin}/efa41d7bdadab3ea21ed2d1b57b9de77261f3dc146bc18844db60140606be64a3e9f9ebcdcd064146d3f65f778337888"

    async with websockets.connect(uri) as websocket:
        print("Conectado al WebSocket")

        handshake_message = [
            {
                # "id": "1",
                "channel": "/meta/handshake",
                "version": "1.0",
                "minimumVersion": "1.0",
                "supportedConnectionTypes": ["websocket", "long-polling", "callback-polling"],
                "advice": {"timeout": 60000, "interval": 0}
            }
        ]
        await websocket.send(json.dumps(handshake_message))
        response = await websocket.recv()
        print(f"Respuesta del servidor (handshake): {json.dumps(json.loads(response), indent=4)}")

        handshake_response = json.loads(response)[0]
        client_id = handshake_response['clientId']

        subscribe_message = [
            {
                # "id": "2",
                "channel": "/meta/connect",
                "clientId": client_id,
                "connectionType": "websocket"
            },
            {
                # "id": "3",
                "channel": "/service/controller",
                "content":"{\"device\":{\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36\",\"screen\":{\"width\":1920,\"height\":1080}}}",
                "clientId": client_id,
                "connectionType":"websocket"
            }
        ]
        await websocket.send(json.dumps(subscribe_message))
        response = await websocket.recv()
        print(f"Respuesta del servidor (subscripciones): {json.dumps(json.loads(response), indent=4)}")

        join_message = [
            {
                # "id": "4",
                "channel": "/service/controller",
                "clientId": client_id,
                "content":"{\"device\":{\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36\",\"screen\":{\"width\":1920,\"height\":1080}}}",
                "data": {
                	"content": "{\"device\":{\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36\",\"screen\":{\"width\":1920,\"height\":1080}}}",
                    "type": "login",
                    "gameid": pin,
                    "host": "kahoot.it",
                    "name": nickname
                }
            },
            {
                "channel": "/service/controller",
                "clientId": client_id,
                "content":"{\"device\":{\"userAgent\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36\",\"screen\":{\"width\":1920,\"height\":1080}}}",
                "data": {
                	"content": "{\"usingNamerator\":false}",
                    "type": "message",
                    "gameid": pin,
                    "host": "kahoot.it",
                    "id": 16
                }
            }
        ]
        await websocket.send(json.dumps(join_message))
        response = await websocket.recv()
        print(f"Respuesta del servidor (unirse al juego): {json.dumps(json.loads(response), indent=4)}")

        connect_continuous_message = [
            {
                # "id": "5",
                "channel": "/meta/connect",
                "clientId": client_id,
                "connectionType": "websocket"
            }
        ]
        await websocket.send(json.dumps(connect_continuous_message))

        try:
            while True:
                message = await websocket.recv()
                # print(f"Mensaje del servidor: {json.dumps(json.loads(message), indent=4)}")
                
                parsed_message = json.loads(message)
                for msg in parsed_message:
                    channel = msg.get("channel")
                    print(f"Mensaje del servidor en el canal {channel}: {json.dumps(msg, indent=4)}")
                    # if channel == "/meta/connect":
                    #     print("Conexión continua exitosa.")
                    #     await websocket.send(json.dumps(connect_continuous_message))
                    # elif channel == "/service/controller":
                    #     print(f"Mensaje del controlador: {json.dumps(msg, indent=4)}")
                    # elif channel == "/service/player":
                    #     print(f"Mensaje del jugador: {json.dumps(msg, indent=4)}")
                    # else:
                    #     print(f"Mensaje en el canal {channel}: {json.dumps(msg, indent=4)}")

        except websockets.exceptions.ConnectionClosedError as e:
            print(f"Error de conexión: {e}")

def fetch_session_data(pin):
    timestamp = int(time.time() * 1000)
    url = f"https://kahoot.it/reserve/session/{pin}/?{timestamp}"
    response = requests.get(url)
    return response.json()

# Decode challenge methods ------------------------------
def base64_decode(data):
    return base64.b64decode(data).decode('utf-8')

def xor_string(data, key):
    return ''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(data, key))

def reserve_challenge_to_answer(message, offset_equation):
    def decode(msg):
        return ''.join(chr((ord(char) * position + eval(offset_equation)) % 77 + 48) for position, char in enumerate(msg))
    return decode(message)

def decode_session_token(e, t, o):
    r = reserve_challenge_to_answer(t, o)
    n = base64_decode(e)
    return xor_string(n, r)

def connect_with_game_id_request(e, reserve_data, parse_response, extract_message_and_offset):
    t = reserve_data
    o = t.headers.get("x-kahoot-session-token")
    r = t.headers.get("x-kahoot-gameserver")
    n = parse_response(t)
    s, a = extract_message_and_offset(n["challenge"])
    i = decode_session_token(o, s, a)
    return {
        "gamePin": e,
        "sessionId": i,
        "reserve": n,
        "gameserver": r
    }

def extract_message_and_offset(script):
    pattern = re.compile(r"'(\d*[a-z][A-Z])\w+'")
    equals_index = script.find("=")
    offset_part = script[equals_index + 1:]
    semicolon_index = offset_part.find(";")
    offset_equation = offset_part[:max(0, semicolon_index)].strip()
    message_match = pattern.search(script)
    
    message = message_match.group(0)[1:-1] if message_match else ""
    
    return {
        "message": message,
        "offsetEquation": offset_equation
    }
# -------------------------------- end challenge decoding methods


def generate_random_string(length):
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


if __name__ == "__main__":
    try:
        pin = '7892778' # int(input("Introduce el pin de la sala: "))
        nickname = "Jose"+generate_random_string(2) # str(input("Introduce tu nombre: "))
        session_data = fetch_session_data(pin)
        print(f"Datos de la sesión: {json.dumps(session_data, indent=4)}")
        asyncio.run(connect_to_websocket(pin, nickname, session_data))
    except Exception as e:
        print(f"Ha ocurrido un error: generate_random_string{e}")