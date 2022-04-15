import { types } from "./types-util"

export const initStateChat = {
    messages: [],
    sending:false,
    errorMessage: null,
}

export const messageReducer = (state, action)=>{
    switch (action.type){
        case types.MESSAGE_SENDING:
            return{
                ...state,
                sending:true,
            }
        case types.MESSAGE_SENT:
            return{
                messages:[
                    ...state.message,
                    action.message,
                ],
                sending:false,
                
            }
        case types.MESSAGE_ERROR:
            return{
                ...state,
                error:action.error,
                sending: false,
            }
        case types.FETCH_MESSAGES:
            return{
                ...state.message,
                sending:true,
                
            }
        case types.types.FETCH_SUCCESS:
            return{
                
                messages:[
                    ...state.message,
                    action.messages],
                sending:false,
            }
        case types.FETCH_ERROR:
            return{
                ...state,
                error:action.error,
                sending:false,
            }
        default:
            return state
    }
}