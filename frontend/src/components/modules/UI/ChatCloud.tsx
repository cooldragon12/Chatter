import { IMessage } from "../../../types/message";



const ChatCloud = ({message}:{message:IMessage}) => {

    return (
        <>
            <div className="flex items-center gap-2">
                <div className="w-10 h-10 rounded-full bg-primary-100 flex justify-center items-center">
                    <p className="text-primary-600 text-sm">{message.user.icon}</p>
                </div>
                <div className="flex flex-col justify-center">
                    <p className="text-primary-600 text-xs">{message.user.username}</p>
                    <div className="flex flex-col gap-1">
                        <p className="text-primary-600 text-md">{message.text}</p>
                    </div>
                </div>
            </div>
            <div className="flex items-center">
                <p className="text-primary-300 text-sm">{message.timestamp}</p>
            </div>
        </>
    )
}
export default ChatCloud;