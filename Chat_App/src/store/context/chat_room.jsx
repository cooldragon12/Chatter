
import {createContext, useContext, useReducer} from 'react';
import { initStateChat, messageReducer } from '../reducer';
export const ChatContext = createContext();
 const ChatProvider = ({children})=>{
    const [messages, dispatch] = useReducer(messageReducer, initStateChat)
    
    return(
        <ChatContext.Provider value={{messages, dispatch}}>
            
                {children}

        </ChatContext.Provider>
    )
}
export default ChatProvider;