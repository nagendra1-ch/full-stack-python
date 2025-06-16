import logo from './logo.svg';
import './App.css';
import AppHeader from "./CricketScore";
import CricketScore from './CricketScore';

function App() {
  return (
    <>
       <div style={{
            backgroundColor:"teal",
            color:"white",
            textAlign:"center",
            padding:20
        }}>
            <h1>Cricket Score</h1>

        </div>

    <div style={{
      display:'flex',
      justifyContent:'space-between'
    }}>
      <div>
        <h3 style={{textAlign:'center'}}>Team-A</h3>
      <CricketScore/></div>
      <div>
        <h3 style={{textAlign:'center'}}>Team-B</h3>
      <CricketScore/></div>
    </div>
    </>
  );
}

export default App;
