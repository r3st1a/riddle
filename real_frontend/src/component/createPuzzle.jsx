import './createPuzzle.css';
import { useContent } from '../hooks/context';
import { FileUpload } from 'primereact/fileupload';
import { message } from "antd"
import { useAccount } from 'wagmi';
//上传图片的api还没有写    create按钮的上传函数没写

export function CreateGuess(){
    const {isCreate,setIsCreate,prizeInputValue,setPrizeInputvalue,CreateInputValue,setCreateInputValue,enterFeeInputValue,setEnterFeeInputValue,nameInputValue,setHardInputValue,setNameInputValue,answerInputValue,setAnswerInputValue,tipInputValue,setTipInputValue,setDscri,descri} = useContent()
    const {address} = useAccount() 
    async function handleClick(){
      console.log(address)
      if(!address) return alert(`你还没有登录！`)
      const data ={  
        title:nameInputValue,
        content:CreateInputValue,
        answer:answerInputValue,
        tip:tipInputValue,
        description:descri,
        prize:prizeInputValue,
        enterFee:enterFeeInputValue
      }
      message.success(`上传中`)
 try{
          const response = await fetch('/create_rid',{
              method:'post',
              headers:{'Content-Type':'application/json'},
              body:JSON.stringify(data)
            })
          const responseData = await response.json()
          message.success(`上传状态：`,responseData)
            }catch(error){message.error(`error:${error}`,2)}      
    }
  return (
    isCreate?
    <div className='modal-overlay'>
    <div className="modal-container">
      {/* Header */}
      <div className="modal-header">
        <span className="modal-title">create</span>
        <button className="close-btn" onClick={()=>{setIsCreate(0)}}>X</button>
      </div>

      {/* Main Content */}
      <div className="modal-content">
        
        <div className='input'>
          
          <p className='puzzle'>puzzle</p>
         <input type="text" value={CreateInputValue}  onChange={(e)=>{setCreateInputValue(e.target.value)}} className="placeholder-box1"/>
         <p className='answer'>answer</p>
         <input type="text" value={answerInputValue}  onChange={(e)=>{setAnswerInputValue(e.target.value)}} className="placeholder-box2"/>
         <p className='tip'>tip</p>
         <input type="text" value={tipInputValue}  onChange={(e)=>{setTipInputValue(e.target.value)}} className="placeholder-box3"/>
         <p className='des'>description</p>
         <input type="text" value={descri}  onChange={(e)=>{setDscri(e.target.value)}} className="placeholder-box4"/>
         <p className='puzzleName'>Puzzle-name</p>
         <input type="text" value={nameInputValue}  onChange={(e)=>{setNameInputValue(e.target.value)}} className="placeholder-box1"/>
         
         
        </div>
        {/* Controls Row */}
        <div className="controls-row">
          {/* Left: Prize Input */}
          <div className="prize-group">
            <div>
              <label>prize:<input type="text" value={prizeInputValue}  onChange={(e)=>{setPrizeInputvalue(e.target.value)}} className="prize-input" /> mon</label>
            </div>
            <div>
              <label>enter-fee:<input type="text" value={enterFeeInputValue} onChange={(e)=>{setEnterFeeInputValue(e.target.value)}} className="prize-input" /> mon</label>
            </div>
           
        </div>
        </div>
      </div>

      {/* Footer Button */}
      <div className="footer">
        <button className="create-btn" onClick={handleClick}>create</button>
      </div>
    </div>
    </div>
    :<></>
  );
};

