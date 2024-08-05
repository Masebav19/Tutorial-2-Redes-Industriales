import { useEffect, useState } from "react";
import  axios  from 'axios'

export function  ControlPanel ({MbAtrr}){
    const [Start,setStart] = useState(false)
    const [Stop,setStop] =useState(false)
    useEffect(()=>{
        handleRequest(MbAtrr.DirIp,MbAtrr.MbAdd[0],Number(Start))
    },[Start])
    useEffect(()=>{
        handleRequest(MbAtrr.DirIp,MbAtrr.MbAdd[1],Number(Stop))
    },[Stop])
    function handleclick_Marcha_On(){
        setStart(true)
    }
    function handleclick_Marcha_Off(){
        setTimeout(()=>{
            setStart(false)
        },100)
        
    }

    function handleclick_Paro_On(){
        setStop(true)
    }
    function handleclick_Paro_Off(){
        setTimeout(()=>{
            setStop(false)
        },100)
        
    }

    const handleRequest=async (Ip,MbAdd,Value)=>{
        const result = await axios.post('http://172.31.36.35:3000/api/coil',{
            MbServer: Ip,
            MbAdd: MbAdd,
            Value: Value
        })
        console.log(result.data)
    }

    return(
    <span>
        <button className="Control-Button Marcha" onClick={handleclick_Marcha_On} onMouseUp={handleclick_Marcha_Off}>
            Marcha
        </button>
        <button className="Control-Button Paro" onClick={handleclick_Paro_On} onMouseUp={handleclick_Paro_Off}>
            Paro
        </button>
    </span>
    );
}