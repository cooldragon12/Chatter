import {Link} from 'react-router-dom'
interface NavProps{
    isAuthUser:boolean,
    toLogout:()=>void
}
const NavBar = ({isAuthUser, toLogout}:NavProps)=>{
    
    return(
        <div className="nav background-eerie-black">
            {
                Boolean(isAuthUser) ? (
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
export default NavBar;