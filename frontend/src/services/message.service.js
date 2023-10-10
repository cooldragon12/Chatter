import { types } from "../reducer"

export const message_send = (dispatch, messagePayload,socket)=>{
    try{
        dispatch({type:types.MESSAGE_SENDING})
        socket.sendMessage(messagePayload)
        
    }catch (err){
        dispatch({type:types.MESSAGE_ERROR,error:err.message})
        console.log(err.message)
    }
}
export const message_retrieve = (dispatch, messagePayload,socket)=>{
    try{
        dispatch({type:types.FETCH_MESSAGES})
        socket.sendMessage(messagePayload)
    }catch (err){
        dispatch({type:types.FETCH_ERROR,error:err.message})
        console.log(err.message)
    }
}
export const add_message = (dispatch, message)=>{
    try{
        dispatch({type: types.MESSAGE_SENT,message:message})
    }catch (err){
        console.log(err.message)
    }
}
export const set_messages = (dispatch, messages)=>{
    try{
        dispatch({type: types.FETCH_SUCCESS, messages:messages})
        
    }catch (err){
        console.log(err.message)
        
    }
}