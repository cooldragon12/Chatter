import { MESSAGE_ACTIONTYPE } from "."

import { IMessageState } from "../../types/message";

/**
 * 
 * @param state 
 * @param action 
 * @returns Reducer for message state and action
 */
export const messageReducer = (state:IMessageState, action:MESSAGE_ACTIONTYPE)=>{
    switch (action.type){
        case "MESSAGE_SEND":
            state.status = "SENDING";
            state.messages.push(action.payload.message);
            state.error = null;
            return state;
        case "MESSAGE_SENT":
            state.status = action.payload.status;
            return state;
        case "MESSAGE_ERROR":
            state.status = "ERROR";
            state.error = action.payload.error;
            return state;
        case "MESSAGE_RECEIVE":
            state.status = "RECIEVED";
            state.messages.push(action.payload.message);
            state.error = null;
            return state;
        case "MESSAGES_FETCH":
            state.status = "FETCHING"
            return state
        case "MESSAGES_FETCH_SCUCCESS":
            state.status = "FETCHED"
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