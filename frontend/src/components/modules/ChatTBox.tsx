import React, { useState } from 'react';
import {BiSend} from "react-icons/bi"

const ChatTBox = (props: { onClick: () => void, name: string }) => {

    const { onClick, name, } = props
    const [text, setText] = useState('');

    const handleEnter = (e: React.KeyboardEvent) => {
        if (e.key !== '13')
            return;
        onClick()
    }
    return (
        <div className=" p-4">
            <div className="  flex justify-center items-center gap-3">
                <div className="flex bg-primary-100 rounded-full p-2">
                    <input
                        onChange={e => setText(e.target.value)}
                        value={text}
                        onKeyUp={handleEnter}
                        
                        className="outline-none w-[50vw] px-4 bg-transparent rounded-full"
                        type="text" name={name ? name : "chat-input"} id="chat-input"
                    />
                </div>
                <button type="button" onClick={onClick} id="chat-submit">
                    <BiSend className="text-primary-200 w-8 h-8 "/>
                </button>
            </div>
        </div>

    )
}
export default ChatTBox;