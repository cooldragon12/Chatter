import React from 'react';
import { useEffect } from 'react';
import { useParams } from 'react-router';
import styled from 'styled-components';
import useAuth from '../hooks/useAuth';
import useRoom from '../hooks/useRoom';
import { ChatProvider } from '../store/context';
const MessagesContainer = styled.div`
    display:block;
`
const ChatRoom = ()=>{
    const {user} = useAuth();
    const {roomId} = useParams();
    const {messages, fetchMessage, sendMessage} = useRoom({roomId:roomId});
    const [message, setMessage] = useState("");
    const handleEnterButton = (e)=>{
        if (e.keyCode === 13){
            document.querySelector("chat-submit").click();
        }
    }
    const messageBoxHandler = (e) =>{
        setMessage(e.target.value)
    }
    const submitHandler = ()=>{
        sendMessage({
            user:user.user,
            content: message,
            room: roomId,
        })
    }
    
    useEffect(()=>{
        fetchMessage(roomId)
    }, [messages])
    
    return(
        <ChatProvider>
            <div className="main-cont">
                <MessagesContainer>
                    {
                        
                    }
                </MessagesContainer>
                <div className="cont">
                    <div className="field">
                        <input 
                            onChange={messageBoxHandler} 
                            value={message} 
                            onKeyUp={e =>handleEnterButton(e)} 
                            className="chat-input" 
                            type="text" name="chat-input" id="chat-input" 
                        />
                    </div>
                    <input type="button" onSubmit={submitHandler} value="submit" id="chat-submit" />
                </div>
            </div>
        </ChatProvider>
    )
}
export default ChatRoom;