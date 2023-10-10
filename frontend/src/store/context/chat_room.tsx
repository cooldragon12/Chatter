import {createContext, useReducer} from 'react';
import { messageReducer } from '../reducers';
import { roomReducer } from '../reducers/room';
import { IChatContext, initStateChat, initStateRoom } from '.';


export const ChatContext = createContext<IChatContext>(
    {
        messages:initStateChat,
        dispatch:()=>{},
        rooms:initStateRoom,
        dispatchRoom:()=>{}
    }
);

const ChatProvider = ({children}:{children:React.ReactNode})=>{
    const [messages, dispatch] = useReducer(messageReducer, initStateChat)
    const [rooms, dispatchRoom] = useReducer(roomReducer, initStateRoom)
    
    
    
    return(
        <ChatContext.Provider value={{
            messages, 
            dispatch,
            rooms,
            dispatchRoom
            }}>
            {children}
        </ChatContext.Provider>
    )
}
export default ChatProvider;