import { types} from './types-util';
export const initStateLogin = {
    user: "",
    access_token:"",
    refresh_token:"",
    error: null,
    
}
export const authReducer = (state, action) => {
    switch (action.type) {
        case types.LOGIN_REQUEST:
            return{
                ...state, 
                loading:true 
            }
        case types.LOGIN_SUCCESS:
            return{
                ...state,
                user: action.payload.username,
                access_token: action.payload.access,
                refresh_token:action.payload.refresh,
                loading:false,
            }
        case types.LOGIN_ERROR:
            return {
                    ...initialState,
                    loading: false,
                    error: action.error
                };
        
        case types.LOGOUT_REQUEST:
            return {
                ...state,
                loading:true,
            };
        case types.LOGOUT_SUCCESS:
                return {
                    ...state,
                    user: "",
                    access_token: "",
                    refresh_token:"",
                    loading:false,
                };
        case types.LOGOUT_ERROR:
            return {
                ...state,
                error:action.error,
            };
        default:
            return state;
    }
}