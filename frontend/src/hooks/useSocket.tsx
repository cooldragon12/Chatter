import { useEffect, useState } from "react";


// const useSocket = ()=>{
    
// }

const useSocket=({url=""})=>{
    const [room, setRoom] = useState("");
    const [socket, setSocket] = useState(new WebSocket);
    const path = `${url}/ws/chat/${room}/`;
    
    
    const connect =()=>{
        setSocket(new WebSocket(path))
        socket.onopen = e =>{
            console.log('Successfully Connected!!');
        }
    }
    const disconnect = () =>{
        return socket.close();
    }
    
    useEffect(()=>{
        if (socket.readyState === socket.OPEN)
            disconnect();
        if (room != "")
            connect();
    }, [room])
    return{setRoom, socket}
}
export default useSocket;