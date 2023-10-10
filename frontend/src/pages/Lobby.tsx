import { useState } from 'react';
import ChatLayout from '../components/layout/ChatLayout';
import ChatTBox from '../components/modules/ChatTBox';
import ChatCloudContainer from '../components/modules/containers/ChatCloudContainer';
import ChatCloud from '../components/modules/UI/ChatCloud';
import { useWebSocket } from 'react-use-websocket/dist/lib/use-websocket';
import { ReadyState } from 'react-use-websocket';

const Lobby =()=>{
    const [socketUrl, setSocketUrl] = useState('wss://localhost:8000/chat');
    const {readyState, sendJsonMessage, lastJsonMessage, getWebSocket} = useWebSocket(socketUrl);
    const connectionStatus = {
        [ReadyState.CONNECTING]: 'Connecting',
        [ReadyState.OPEN]: 'Open',
        [ReadyState.CLOSING]: 'Closing',
        [ReadyState.CLOSED]: 'Closed',
        [ReadyState.UNINSTANTIATED]: 'Uninstantiated',
    }[readyState];
    return(
        <div id="lobby" className='bg-background w-full h-whole'>
            {/* Chat Interface */}
            <ChatLayout>
                <div className="w-full h-3/4 rounded-r-lg">
                    {/* Chats Selection */}
                    
                </div>
                <div className="w-full h-full bg-background/40 flex flex-col gap-4">
                    {/* Main Chat */}
                    <div className='flex flex-1 flex-col scroll-m-1 overflow-y-scroll justify-end gap-3'>
                        <ChatCloudContainer children={ChatCloud} message={{
                            id:"0",
                            timestamp:'12:00',
                            text:'Hello World',
                            user:{
                                id:"0",
                                status:'online',
                                username:'John Doe',
                                icon:'JD'
                            },
                            status:'SENT'
                        }} isSender={false}/>
                        <ChatCloudContainer children={ChatCloud} message={{
                            id:"0",
                            timestamp:'12:00',
                            text:'ds',
                            user:{
                                id:"0",
                                status:'online',
                                username:'John Doe',
                                icon:'We',
                            },
                            status:'SENT'
                        }} isSender={true}/>
                    </div>
                    <ChatTBox onClick={()=>{}} name='lobby-chat-input'/>
                </div>
                <div className="w-full h-3/4 bg-accent/40 rounded-md">
                    {/* Chat Description */}
                </div>
            </ChatLayout>
            
        </div>
    )
}
export default Lobby;