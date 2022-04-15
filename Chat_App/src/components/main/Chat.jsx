import React,{useEffect, useState} from 'react';
import styled from 'styled-components';

const Container = styled.div`
display:flex;
width:100%;
height:fit-content;
flex-wrap:wrap;
justify-content:${({sender}) => sender? "right" : "left" };
align-items:center;
`
const MessageContainer = styled.div`
    display:flex;
    flex-wrap:wrap;

    flex-direction:vertical;
    justify-content:${({sender}) => sender? "right" : "left" };
    align-items:center;
`
const MessageCont= styled.div`
    padding:10%;
    display:flex;
    flex-wrap:wrap;
`
const DateContainer= styled.div`
    color:#457b9d;
    font-style:italic;
`
const AuthorCont = styled.div`
color:#457b9d;
`
const Chat = ({message, sender})=>{
    
    return(
        <Container sender={sender}>
            <MessageContainer sender={sender}>
                <AuthorCont>
                    {message.user}
                </AuthorCont>
                <MessageCont>
                    <p>{message.content}</p>
                </MessageCont>
                <DateContainer>
                    {message.timestamp}
                </DateContainer>
            </MessageContainer>
        </Container>
    )
}
export default Chat;