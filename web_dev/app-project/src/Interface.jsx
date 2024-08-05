import { ControlPanel } from './control.jsx'
import { StatusPanel } from './statusPanel.jsx'

export function Interface({MbAtrr}){
    return(
    <>
        <div className="Major-container">
            <h1>Interfaz de usuario</h1>
            <h2>Totorial 2</h2>
            <div className='Container panel'>
                <ControlPanel 
                    MbAtrr ={MbAtrr}
                />
                <StatusPanel 
                    MbAtrr = {MbAtrr}
                />
            </div>
            
        </div>  
    </>
    );
}