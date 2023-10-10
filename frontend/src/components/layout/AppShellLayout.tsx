import { Link, Outlet } from "react-router-dom"
import { Route } from "../../pages"

export default function AppShellLayout({routes}:{ routes:Route[]}){
    return (
        <> 
            {/* Nav Sidebar */}
            <nav className=" w-16 h-screen top-0 z-20 left-0 bg-accent-300 text-primary-dark float-left flex justify-center items-center shadow-md">
                <div className="flex flex-col justify-center items-center bg-accent-100 py-9 rounded-full gap-3">
                    {
                        routes.map((route, index:number) => {
                            return (
                                <Link to={route.path} key={index} className="flex justify-center items-center w-full h-max p-5 rounded-full cursor-pointer group hover:bg-accent-200 transition-colors">
                                    <route.icon className="text-accent-300 w-6 h-6 group-hover:text-accent-500 transition-colors"/>
                                </Link>
                            )
                        })
                    }
                </div>
            </nav>
            {/* Header */}
            <div className="w-whole h-whole">
                <header className="pl-8  h-16 z-10 bg-accent-100 text-primary-700 shadow-sm">
                    <div className=" flex justify-between items-center h-full">
                        <div className="flex items-center">
                            <h1 className="font-semibold">Messages</h1>
                        </div>
                    </div>
                </header>
                {/* Main Content */}
                <Outlet/>
            </div>
        </>
    )
}