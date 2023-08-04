import { types } from "./types-util";
export const initRoom = {
    groups:[],
    error:null,
}

export const roomReducer = (state, action)=>{
    switch (action.type){
        case types.FETCH_GROUPS:
            return{
                groups: [],
                error:null
            }
        case types.FETCH_GROUP_SUCCESS:
            return{
                groups: [action.payload.groups],
                error:null
            }
        case types.FETCH_GROUP_ERROR:
            return{
                groups: [state.groups],
                error:action.payload.error
            }
        case types.FETCH_GROUP_ERROR:
            return{
                groups: [state.groups],
                error:action.payload.error
            }
        case types.CREATE_GROUP:
            return {
                groups:[state.groups],
                error:null,
            }
        case types.CREATE_GROUP_ERROR:
            return {
                groups:[state.groups],
                error:action.payload.error
            }
        case types.CREATE_GROUP_SUCCESS:
            return {
                groups:[action.payload.newGroup,state.groups],
                error:null
            }
        case types.JOIN_GROUP:
            return {
                groups:[state.groups],
                error:null,
            }
        case types.JOIN_GROUP_ERROR:
            return {
                groups:[state.groups],
                error:action.payload.error,
            }
        case types.JOIN_GROUP_SUCCESS:
            return {
                groups:[action.payload.joinedGroup,state.groups ],
                error:null,
            }
    }
}