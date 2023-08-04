import ChatLayout from '../components/layout/ChatLayout';
import ChatTBox from '../components/modules/ChatTBox';
import ChatCloud from '../components/modules/containers/ChatCloud';

const Lobby =()=>{
    return(
        <div id="lobby" className='bg-background w-full h-whole'>
            {/* Chat Interface */}
            <ChatLayout>
                <div className="w-full h-full bg-primary-300 rounded-r-lg">
                    {/* Chats Selection */}
                </div>
                <div className="w-full h-full bg-background flex flex-col gap-4">
                    {/* Main Chat */}
                    <div className='flex flex-1 flex-col scroll-m-1 overflow-y-scroll justify-end gap-3'>
                        <ChatCloud message={{
                            time: "12:00",
                            text: "Hello World",
                        }}  sender={{
                            icon: "A",
                            name: "Ako",
                        }}/>
                        <ChatCloud message={{
                            time: "12:00",
                            text: "Hello Worldfsa sdjiajdiajidsjaijdijaijdsjaidji as ijdiaaj",
                        }}  sender={{
                            icon: "A",
                            name: "Ako",
                        }}/>
                    </div>
                    <ChatTBox onClick={()=>{}} name='lobby-chat-input'/>
                </div>
                <div className="w-full bg-accent-200 h-full">
                    {/* Chat Description */}
                </div>
            </ChatLayout>
            
        </div>
    )
}
export default Lobby;