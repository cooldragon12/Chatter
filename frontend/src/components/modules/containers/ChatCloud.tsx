

const ChatCloud = ({message, sender})=>{
    
    return(
        <div className="flex flex-col px-5">
            <div className="flex justify-between items-center">
                <div className="flex items-center gap-2">
                    <div className="w-10 h-10 rounded-full bg-primary-100 flex justify-center items-center">
                        <p className="text-primary-600 text-sm">{sender.icon}</p>
                    </div>
                    <div className="flex flex-col justify-center">
                            <p className="text-primary-600 text-xs">{sender.name}</p>
                        <div className="flex flex-col gap-1">
                            <p className="text-primary-600 text-md">{message.text}</p>
                        </div>
                    </div>
                </div>
                <p className="text-primary-300 text-sm">{message.time}</p>
            </div>
        </div>
    )
}
export default ChatCloud;