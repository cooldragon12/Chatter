
import { FaHome, FaFileContract  } from 'react-icons/fa';

export type Route = {
    path:string,
    isPrivate:boolean,
    icon:any,
}

const routes:Route[] = [
    {
        path:'/',
        isPrivate:true,
        icon:FaHome,
    },
    {
        path:'/contact',
        isPrivate:true,
        icon:FaFileContract,
    }
    // {
    //     path:'/'| '/login',
    //     component:Login,
    //     isPrivate:false,
    // },
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