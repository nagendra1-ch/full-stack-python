import React, { useState } from 'react'

const CricketScore= () => {
    const [wickets,setWickets]=useState(0)
    const [score,setScore]=useState(0)
    const [balls,setBalls]=useState(0)
    const [overs,setOvers]=useState(0)

    const handleRuns=(runs)=>{
        if(balls==6){
            setOvers(overs+1)
        }
        setBalls(balls  == 6 ? 0 : balls+1)
        setScore(score+runs)
    }
    const handleWicket=()=>{
        setWickets(wickets+1)
        if(balls==6){
            setBalls(0)
            setOvers(overs+1)
        }
        setBalls(balls  == 6 ? 0 : balls+1)
        

    }
    const reset=()=>{
        setBalls(0)
        setOvers(0)
        setScore(0)
        setWickets(0)
    }
    
    return (
        <>
           
        <h3 style={{
            textAlign:"center"
        }}>Score: {score}/{wickets}</h3>
        <p>overs:{overs}.{balls}</p>
        {
            wickets<10?
        <div style={{
            
            textAlign:'center'
        }}>

            <button style={{
                    backgroundColor:"teal",
                    margin:40,
                    padding:10,
                     borderRadius:5
                }} onClick={()=>handleRuns(6)}>6</button>
                <button style={{
                    backgroundColor:"teal",
                    padding:10,
                    margin:40,
                     borderRadius:5
                }} onClick={()=>handleRuns(4)}>4</button>
                <button style={{
                    padding:10,
                    backgroundColor:"teal",
                    margin:40,
                    padding:10,
                     borderRadius:5
                    
                }} onClick={()=>handleRuns(1)}>1</button>
                <button style={{
                    padding:10,
                    backgroundColor:"teal",
                    margin:40,
                    padding:10,
                    borderRadius:5
                    
                }} onClick={()=>handleRuns(2)}>2</button>
                <button style={{
                    padding:10,
                    backgroundColor:"teal",
                    margin:40,
                    padding:10, borderRadius:5
                    
                }} onClick={()=>handleRuns(0)}>Dot</button>
                
            <button style={{
                backgroundColor:"teal",
                    margin:40,
                    padding:10,
                     borderRadius:5
            }} onClick={handleWicket}>wicket</button>
            <button style={{
                backgroundColor:"red",
                    margin:40,
                    padding:10,
                     borderRadius:5
            }} onClick={reset}>Reset</button>
            
            

            
        </div>
        :
        <h2 style={{
            textAlign:"center"
        }}>GAMEOVER</h2>
}
            
        </>
    )
}

export default CricketScore
