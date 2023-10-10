import { IMessageState } from "../../types/message"
import { IRoomState } from "../../types/room"


export const initStateChat = {} as IMessageState
export const initStateRoom = {} as IRoomState

export interface IChatContext{
    messages:IMessageState,
    dispatch:React.Dispatch<any>
    rooms:IRoomState,
    dispatchRoom:React.Dispatch<any>
}