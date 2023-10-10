import { ROOM_ACTIONTYPE } from "."
import { IRoomState } from "../../types/room"
/**
 * 
 * @param state ``IRoomState``
 * @param action ``ROOM_ACTIONTYPE``
 * @returns state
 * @description Reducer for room state and action  
 */
export const roomReducer = (state:IRoomState, action:ROOM_ACTIONTYPE)=>{
    switch (action.type){
        case 'CREATE_ROOM':
            state.loading = true
            return state
        case 'CREATE_ROOM_SUCCESS':
            state.rooms.push(action.payload.newRoom)
            state.loading = false
            return state
        case 'CREATE_ROOM_ERROR':
            state.error = action.payload.error
            state.loading = false
            return state
        case 'FETCH_ROOMS':
            state.loading = true
            return state
        case 'FETCH_ROOMS_SUCCESS':
            state.rooms = action.payload.rooms
            state.loading = false
            return state
        case 'FETCH_ROOMS_ERROR':
            state.error = action.payload.error
            state.loading = false
            return state
        case 'JOIN_ROOM':
            state.loading = true
            return state
        case 'JOIN_ROOM_ERROR':
            state.error = action.payload.error
            state.loading = false
            return state
        case 'JOIN_ROOM_SUCCESS':
            state.rooms.push(action.payload.room)
            state.loading = false
            return state
    }
}