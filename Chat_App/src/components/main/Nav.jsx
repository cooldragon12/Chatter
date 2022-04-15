import React from 'react';
import {Link} from 'react-router-dom'

const Nav = ({isAuthUser, toLogout})=>{
    
    return(
        <div className="nav">
            {
                Boolean(isAuthUser.token) ? (
                <>
                    <Link to="/">
                        <span>Home</span>
                    </Link>
                    <Link to="/logout">
                        <span onClick={toLogout}>Logout</span>
                    </Link>
                </>
                ): (
                    <>
                        <Link to="/login">
                            <span>Login</span>
                        </Link>
                        <Link to="/signup">
                            <span>Sign up</span>
                        </Link>
                    </>
                )
            }
        </div>
    )
}
export default Nav;