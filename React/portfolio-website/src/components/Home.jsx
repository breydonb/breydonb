import Intro from "./intro/intro";
import Projects from "./projects/Projects";
import Skills from './skills/skills';
import Footer from './Footer';

function Home() {
    return (
        <div>
            <Intro />
            <Projects />
            <Skills />
            <Footer />
        </div>
    )
}

export default Home