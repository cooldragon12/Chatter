/**
 * Message types
 * 
 * This is the type od the state or data that the application will be using
 */
import { IUser } from "./user";
/**
 * Message interface
 * This is the interface for the message object
 */
export type IMessage = {
    id: string;
    text: string;
    timestamp: string;
    user: IUser;
    status:MessageStatus;
}

export type IMessageState = {
    messages:IMessage[];
    status:MessageStatus;
    error?:{};
}

/**
 * Message status
 * This is the status of the message
 */
export type MessageStatus=
| "SENT"
| "RECIEVED"
| "SENDING"
| "ERROR"
| "FETCHING"
| "FETCHED"

