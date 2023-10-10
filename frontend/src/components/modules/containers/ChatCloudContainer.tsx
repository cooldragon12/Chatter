import React from "react";
import { IMessage } from "../../../types/message";


const ChatCloudContainer = ({children, message, isSender}:{children:React.JSXElementConstructor<{message:IMessage}>, message:IMessage, isSender:boolean})=>{
    const Child = children;
    return(
        <div className="flex flex-col px-5">
            <div className={`flex justify-between p-2 rounded-md ${isSender? 'bg-white':''}`}>
                <Child message={message}  />
                {
                    
                }
            </div>
        </div>
    )
}
export default ChatCloudContainer;