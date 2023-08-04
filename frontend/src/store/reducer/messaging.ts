import { MESSAGE_ACTIONTYPE } from "."
import { MessageInterface, MessageStatus } from "../context"


export const initStateChat = {
    messages: [],
    status:"",
    error: null,
}

export const messageReducer = (state:{messages:MessageInterface[], status:MessageStatus, error?:{}}, action:MESSAGE_ACTIONTYPE)=>{
    switch (action.type){
        case "MESSAGE_SENDING":
            state.status = "SENDING";
            state.messages.push(action.payload.message);
            return state;
        case "MESSAGE_SEND":
            state.status = "SENT";
            return state;
        case "MESSAGE_ERROR":
            state.status = "ERROR";
            state.error = action.payload.error;
            return state;
        case "MESSAGE_RECEIVE":
            state.status = "RECIEVED";
            state.messages.push(action.payload.message);
            return state;
        case "MESSAGES_GET":
            state.status = "RECIEVED"
            state.messages.concat(action.payload.messages)
            return state
        case "MESSAGES_ERROR":
            state.status = "ERROR"
            state.error = action.payload.error
            return state
        default:
            return state
    }
}