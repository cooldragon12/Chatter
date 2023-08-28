
import {createContext, useContext, useReducer} from 'react';
import { initStateChat, messageReducer } from '../reducer';

export type Message = {
    id: string;
    text: string;
    createdAt: Date;
    userId: string;
}

export const ChatContext = createContext();
const ChatProvider = ()=>{
    const [messages, dispatch] = useReducer(messageReducer, initStateChat)
    
    return(
        <ChatContext.Provider value={{messages, dispatch}}>
            {children}
        </ChatContext.Provider>
    )
}
export default ChatProvider;