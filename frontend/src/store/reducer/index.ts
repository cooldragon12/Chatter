import { MessageInterface, RoomInterface, UserCurrentInterface } from '../context';

export {authReducer} from './auth';
export {initStateChat, messageReducer} from './messaging'


export type AUTH_ACTIONTYPE =
// Authentication ACTIONTYPE
| {type:"LOGIN_REQUEST", payload?: UserCurrentInterface}
| {type:"LOGIN_SUCCESS", payload: UserCurrentInterface}
| {type:"LOGIN_ERROR", payload: {error:{}}}
| {type:"LOOUT", payload:{}}

export type MESSAGE_ACTIONTYPE =
| {type:"MESSAGE_SEND"}
| {type:"MESSAGE_SENDING", payload:{message:MessageInterface}}
| {type:"MESSAGE_RECEIVE",payload:{message:MessageInterface}}
| {type:"MESSAGE_ERROR", payload:{error:{}}}
| {type:"MESSAGES_GET", payload:{messages:MessageInterface[]}}
| {type:"MESSAGES_ERROR",payload:{error:{}}}

export type ROOM_ACTIONTYPE = 
| {type: "CREATE_ROOM", payload:RoomInterface}
| {type: "JOIN_ROOM", payload:RoomInterface}
| {type: "FETCH_ROOMS", payload:RoomInterface[]}