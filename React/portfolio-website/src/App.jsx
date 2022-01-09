import Intro from "./components/intro/intro";
import Projects from "./components/projects/Projects";
import React from 'react';
import Navigation from "./components/navigation";


const App = () => {

  return (
    <div>
      <Navigation />
      <Intro />
      <Projects />
    </div>
  )
}

export default App
