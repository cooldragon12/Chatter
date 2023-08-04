import React from "react"

const ChatLayout = ({children}:{children:React.ReactNode[]})=>{
    return (
        <div className="flex w-full h-full">
            <div className="flex w-1/4">
                {children[0]}
            </div>
            <div className="flex flex-1">
                {children[1]}
            </div>
            <div className="flex w-80">
                {children[2]}
            </div>
        </div>
    )
}

export default ChatLayout