import Intro from "./intro/intro";
import Projects from "./projects/Projects";
import Skills from './skills/skills';


function Home() {
    return (
        <div>
            <Intro />
            <Projects />
            <Skills />
        </div>
    )
}

export default Home