import ChatRoom from './ChatRoom';
import Login from './Login';
import Lobby from './Lobby';
const routes = [
    {
        path:'/'| '/login',
        component:Login,
        isPrivate:false,
    },
    // {
    //     path:'/sign-up',
    //     component:Register,
    //     isPrivate:false,
    // },
    // {
    //     path:'/lobby',
    //     component:Lobby,
    //     isPrivate:true,
    // },
    // {
    //     path:'/room',
    //     component:ChatRoom,
    //     isPrivate:true,
    // },
    
]
export default routes;