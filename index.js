var ws = new WebSocket("ws://localhost:8765/echo")
//建立成功后触发事件
var cmsg = JSON.stringify({id:123,data:"我是数据",toId:456});
ws.onopen = function () {
    ws.send(cmsg)
    console.log("sending ... ")
    alert(cmsg)
};
//when get server data do
ws.onmessage = function (evt) {
    var recevied_msg = evt.data
    console.log(recevied_msg)
    alert(recevied_msg)
};
//shutdown websocket so
ws.onclose = function () {
    console.log("shutdown ")
};