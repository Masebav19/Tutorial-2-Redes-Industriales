import { useState, useEffect } from 'react';
import  axios  from 'axios'

function GreenIcon(){
    return(
        <svg width="100px" height="100px" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="green">
            <path d="M18,9.5V8H17V7a2,2,0,0,0-2-2H4A2,2,0,0,0,2,7v7a2,2,0,0,0,2,2H15a2,2,0,0,0,
            2-2V13h1V11.5h4v-2ZM14,14H5V13h9Zm0-2H5V11h9Zm0-2H5V9h9Zm0-2H5V7h9ZM3,17H16v2H3Z"/>
            <rect width="24" height="24" fill="none"/></svg>
        // <svg
        // version="1.1"
        // baseProfile="full"
        // width="100"
        // height="100"
        // xmlns="http://www.w3.org/2000/svg">
        // <circle cx="50" cy="50" r="30" fill = "Green"/>
        // </svg>
      
    );
}

function RedIcon(){
    return(
        <svg width="100px" height="100px" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fill="red">
            <path d="M18,9.5V8H17V7a2,2,0,0,0-2-2H4A2,2,0,0,0,2,7v7a2,2,0,0,0,2,2H15a2,2,0,0,0,
            2-2V13h1V11.5h4v-2ZM14,14H5V13h9Zm0-2H5V11h9Zm0-2H5V9h9Zm0-2H5V7h9ZM3,17H16v2H3Z"/>
            <rect width="24" height="24" fill="none"/></svg>
    //     <svg
    //     version="1.1"
    //     baseProfile="full"
    //     width="100"
    //     height="100"
    //     xmlns="http://www.w3.org/2000/svg">
    //     <circle cx="50" cy="50" r="30" fill = "Red"/>
    //   </svg>
      
    );
}



export function StatusPanel({MbAtrr}){
    const [State,setState] = useState(false)
    const [Value,setValue] = useState(false)
    useEffect(()=>{
        const interval = setInterval(async ()=>{
            const newState = await handleRequestContact();
            setState(newState)
        },200)
        return ()=> clearInterval(interval)
    },[State])
    
    useEffect(()=>{
        const interval = setInterval(async()=>{
            const newValue = await handleRequestInput();
            setValue(newValue)
        },300)
        return ()=> clearInterval(interval)
    },[Value])

    const handleRequestContact=async ()=>{
        const result = await axios.post('http://172.31.36.35:3000/api/contact',{
            MbServer: MbAtrr.DirIp,
            MbAdd: MbAtrr.MbAdd[2],
            Length: 1 
        })
        return result.data.Value[0] 
    }
    
    const handleRequestInput=async ()=>{
        const result = await axios.post('http://172.31.36.35:3000/api/input',{
            MbServer: MbAtrr.DirIp,
            MbAdd: MbAtrr.MbAdd[3],
            Length: 1 
        })
        return result.data.Value[0] 
    }

    return(
        <span className='container panel'>
            {State&&<GreenIcon />}
            {!State&&<RedIcon />}
            <p className='Value'>{Value}</p>
        </span>
    );
}