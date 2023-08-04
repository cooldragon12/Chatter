export {AuthProvider} from './auth';
// export {useChatDispatch, useChatState,ChatProvider} from './chat_room';
export {default as ChatProvider, ChatContext} from './chat_room';

export interface RoomInterface{
    search_id:string,
    name: string,
    max_users: number,
    host: number | UserInterface
    code: string,
    created_on:string,
    members?:number[] | UserInterface[] |null,
    messages?: [] | MessageInterface[]
}

export interface MessageInterface{
    content:string,
    user: number | UserInterface
    timestamp: string
}
export type MessageStatus=
| "SENT"
| "RECIEVED"
| "SENDING"
| "ERROR"
export interface UserInterface{
    id:string,
    username:string,
    status:string
}
export interface UserCurrentInterface{
    user:UserInterface,
    rooms_list: RoomInterface[] | []
    access_token: string
}
interface Provider{
    current_user:UserCurrentInterface,
    // dispatch: React.Dispatch<>
}

