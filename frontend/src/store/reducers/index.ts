// Import Types
import { IMessage, MessageStatus } from '../../types/message';
import { IRoom } from '../../types/room';
import { UserCurrentInterface } from '../../types/user';
// Reducers Chat Related
import { messageReducer } from './messaging';
import { roomReducer } from './room';
/**
 * @description This is the type of the action that will be dispatched to the reducer, especially for `AuthReducer`
 */
export type AUTH_ACTIONTYPE =
// Authentication ACTIONTYPE
| {type:"LOGIN_REQUEST", payload?: UserCurrentInterface}
| {type:"LOGIN_SUCCESS", payload: UserCurrentInterface}
| {type:"LOGIN_ERROR", payload: {error:{}}}
| {type:"LOGOUT"}

export type MESSAGE_ACTIONTYPE =
| {type:"MESSAGE_SEND", payload:{message:IMessage}}
| {type:"MESSAGE_SENT", payload:{message:IMessage, status:MessageStatus}}
| {type:"MESSAGE_RECEIVE",payload:{message:IMessage, status:MessageStatus}}
| {type:"MESSAGE_ERROR", payload:{error:{},status:MessageStatus}}
| {type:"MESSAGES_FETCH", payload:{status:MessageStatus}}
| {type:"MESSAGES_FETCH_SCUCCESS", payload:{messages:IMessage[], status:MessageStatus}}
| {type:"MESSAGES_ERROR", payload:{error:{}, status:MessageStatus}}

export type ROOM_ACTIONTYPE = 
| {type: "CREATE_ROOM", payload:{loading:boolean}}
| {type: "CREATE_ROOM_ERROR", payload:{error:{}}}
| {type: "CREATE_ROOM_SUCCESS", payload:{newRoom:IRoom, loading:boolean}}
| {type: "JOIN_ROOM", payload:{loading:boolean}}
| {type: "JOIN_ROOM_ERROR", payload:{error:{}, loading:boolean}}
| {type: "JOIN_ROOM_SUCCESS", payload:{room:IRoom, loading:boolean}}
| {type: "FETCH_ROOMS", payload:{loading:boolean}}
| {type: "FETCH_ROOMS_ERROR", payload:{error:{}, loading:boolean}}
| {type: "FETCH_ROOMS_SUCCESS", payload:{rooms:IRoom[], loading:boolean}}


export {
    messageReducer,
    roomReducer,
}