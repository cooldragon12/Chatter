class WebSocketProvider{

    constructor(roomUrl, socket_url){
        this.socket_url = socket_url
         // Default
        this.roomUrl= roomUrl;
    }
    changePath(newUrl){
        this.path = newUrl
    }
    // changeconnection(roomUrl){
    //     this.disconnect();
    //     // disconnect then reconnect new room
    //     this.path = `${this.socket_url}/ws/chat/${roomUrl}/`;
    //     this.socket = new WebSocket(this.path);
    //     this.socket.onopen = e =>{
    //         console.log(`Successfully Connected!! ${roomUrl}`);
    //     }
    //     this.socket.onerror = e =>{
    //         console.log('Error Connection')
    //     }
    //     this.socket.onclose = e =>{
    //         this.connect(roomUrl);
    //     }
    // }
    connect(){
        this.path = `${this.socket_url}/ws/chat/${this.roomUrl}/`;
        this.socket = new WebSocket(this.path);
        this.socket.onopen = e =>{
            console.log('Successfully Connected!!');
        }
        // The one who responsiible for recieving after handsshake
        this.socket.onmessage = e =>{
            this.receiveMessage(e.data);
        }
        this.socket.onclose = e =>{
            this.connect(roomUrl);
        }
    };
    disconnect(){
        this.socket.close();

    };
    // Method of Fetch and Send
    fetchMessage(roomId){
        return this.sendRequest({
            command:'fetch_messages',
            roomId:roomId
        })
    }
    sendMessage(message){
        return this.sendRequest({
            command:'new_message',
            from: message.user,
            content:message.content,
            room: message.roomId
        })
    }
    
    // Manage the request
    sendRequest(data){
        try{
            this.socket.send(JSON.stringify({...data}))
        }catch (err){
            console.log(err.message)
        }
    }
    receiveMessage(data){
        const dataJson = JSON.parse(data);
        const command = dataJson.command;

        return dataJson;
    }
}
export default WebSocketProvider;