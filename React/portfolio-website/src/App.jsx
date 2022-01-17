import Intro from "./components/intro/intro";
import Projects from "./components/projects/Projects";
import React from 'react';
import Navigation from "./components/navigation/Navigation";
import Skills from './components/skills/skills';
import Footer from './components/Footer';


const App = () => {

  return (
    <div>
      <Navigation />
      <Intro />
      <Projects />
      <Skills />
      <Footer />
    </div>
  )
}

export default App
