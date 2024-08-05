import { Interface } from './Interface'
import { useState } from 'react'
import cors from 'cors'

cors();
class MbServerAtrr{
    constructor(DirIp,MbAdd){
        this.DirIp = DirIp,
        this.MbAdd = MbAdd
    }
  }


function InputForm({UpdateAtrr}){ 
    
    function HandleReadInputs(e){
        e.preventDefault()
        const form = e.target;
        const formData = new FormData(form)
        const Formdata = Object.fromEntries(formData.entries())
        const MbServer = new MbServerAtrr(Formdata.IpAdd,[
            Formdata.StartAdd, Formdata.StopAdd, Formdata.StatusAdd, Formdata.LevelAdd
        ])
        UpdateAtrr(MbServer)  
    
    }
    return(
        <>
            <h1>Laboratorio de redes Industriales</h1>
            <p>Ingrese los campos necesario para inciar la interfaz de usuario</p>
            <span>
                <form method="POST" onSubmit={HandleReadInputs}>
  
                    <label htmlFor="IpAdd">Direccion Ip del servidor</label>
                    <input name= "IpAdd" type="text" className="IpAdd" />
  
                    <label htmlFor="StartAdd">Direccion modbus para Marcha</label>
                    <input name= "StartAdd" type="number" className="StartAdd" />
  
                    <label htmlFor="StopAdd">Direccion modbus para Paro</label>
                    <input name= "StopAdd" type="number" className="StopAdd" />
  
                    <label htmlFor="StatusAdd">Direccion modbus para Status</label>
                    <input name= "StatusAdd" type="number" className="StatusAdd" />
  
                    <label htmlFor="LevelAdd">Direccion modbus para Nivel</label>
                    <input name= "LevelAdd" type="number" className="LevelAdd" />
  
                    <button className="Submit" >Iniciar</button>
                </form>
                
            </span>
        
        </>
    );
}

export function App(){
    const [MbAtrr,setMbAtrr] = useState({})

    const UpdateAtrr = (MbServer = {})=>{
        setMbAtrr(MbServer)
    }
    return(
        <>
            <div className="Container">
                <div className='Major-container'>
                    <InputForm
                        UpdateAtrr = {UpdateAtrr}
                    /> 
                </div>
                    {typeof(MbAtrr?.DirIp) === "string" && <Interface
                        MbAtrr = {MbAtrr}
                    />}
            </div>
                        
        </>
    )
}