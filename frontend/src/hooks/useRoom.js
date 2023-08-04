import { createRef, useContext, useEffect } from "react"
import { URLS } from "../config";
import { ChatContext } from "../store/context/chat_room"
import { add_message, message_retrieve, set_messages } from "../store/dispatcher/message";
import useSocket from "./useSocket";

const useRoom = ({roomId=""})=>{
    const {messages, dispatch} = useContext(ChatContext);
    const {socket, setRoom} = useSocket({url:URLS})
    socket.onmessage = e =>{
        receiveMessage(e.data);
    }
    const sendRequest=(data)=>{
        try{
            socket.send(JSON.stringify({...data}))
        }catch (err){
            console.log(err.message)
        }
    }
    const receiveMessage = (data)=>{
        const dataJson = JSON.parse(data);
        if (dataJson.command === 'messages')
            set_messages(dispatch, dataJson.messages)
        if (dataJson.command === 'new_message')
            add_message(dispatch,dataJson.message)
    }
    const fetchMessage = (roomId)=>{
        return sendRequest({
            command:'fetch_messages',
            roomId:roomId
        })
    }
    const sendMessage= (message)=>{
        return sendRequest({
            command:'new_message',
            from: message.user,
            content:message.content,
            room: message.roomId
        })
    }
    useEffect(()=>{
        setRoom(roomId);
        fetchMessage(roomId);
        return socket.close()
    }, [roomId])
    return{messages, sendMessage, fetchMessage}
}
export default useRoom;