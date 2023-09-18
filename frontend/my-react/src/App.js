import React from "react"
import {BrowserRouter as Router, Link, Route, Switch} from 'react-router-dom'
import NavBar from './components/NavBar'
import './App.css'

function App() {
  return (
    <div>
        <Router>
          <Switch>
            <NavBar/>
          </Switch>
        </Router>
    </div>
  )
}

export default App;