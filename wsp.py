import asyncio
import websockets
import struct

async def handle_message(message):
    if isinstance(message, str):
        print('Mensaje de texto recibido:', message)
    elif isinstance(message, bytes):
        print('Mensaje binario recibido:', message)
        # Verificar si el mensaje es un frame de cierre
        if message[0] == 0x88:
            print('Frame de cierre recibido.')
            return True
        # Procesa los datos binarios según el protocolo específico
        # Ejemplo de interpretación de datos binarios:
        try:
            decoded_message = struct.unpack('!I', message[:4])  # Desempaquetar los primeros 4 bytes como un entero
            print('Mensaje decodificado:', decoded_message)
        except struct.error as e:
            print('Error al decodificar el mensaje binario:', e)
        return False

async def connect():
    uri = "wss://web.whatsapp.com/ws/chat?ED=CAIIDA"
    try:
        async with websockets.connect(uri) as websocket:
            while True:
                try:
                    message = await websocket.recv()
                    is_close_frame = await handle_message(message)
                    if is_close_frame:
                        break
                except websockets.ConnectionClosedError as e:
                    print("Conexión cerrada:", e)
                    break
                except websockets.IncompleteReadError as e:
                    print("Error de lectura incompleta:", e)
                    break
    except Exception as e:
        print("Error al conectar:", e)

if __name__ == "__main__":
    asyncio.run(connect())