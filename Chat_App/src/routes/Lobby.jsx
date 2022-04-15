import React from 'react';
import { useAuthDispatch, useAuthState } from '../store/context';
import { logout } from '../store/dispatcher';




const Lobby =()=>{
    const userDetails = useAuthState();
    return(
        <div className="lobby">

        </div>
    )
}