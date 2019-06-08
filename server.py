import websockets
import asyncio
import json




@asyncio.coroutine
def get(websocket, path):
    recv = websocket.recv()
    jmessage = yield from recv
    message = recv
    print(message)
    msg = json.loads(jmessage)
    print(msg['id'], 'sendTO', msg['toId'], ':', msg['data'])
    server_data = "收到服务端的数据"
    yield from websocket.send(server_data)


@asyncio.coroutine
def send(msg, path):
    if(1):
        print('1')




def read_msg(data):
    msg_len = data[1] & 127 #数据长度
    if msg_len == 126:
        mask = data[4:8] #mask掩码
        content = data[8:]
    elif msg_len == 127:
        mask = data[10:14] #mask掩码
        content = data[14:]
    else:
        mask = data[2:6] #mask掩码
        content = data[6:]

    raw_str = ''
    for i,d in enumerate(content):
        raw_str += chr(d ^ mask[i % 4])
    return raw_str


start_server = websockets.serve(get, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

