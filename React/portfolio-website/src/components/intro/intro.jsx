import '../../App.css';
import 'bootstrap/dist/css/bootstrap.css';
import Typewriter from 'typewriter-effect';

// <div className='spacer layer-wave'></div>

function intro(){
    return (
        <>
            {/*                
                <div className='p-5'>
                    <div className='d-flex justify-content-center'>
                        <div className='hexagon'>
                            <div className='hex-background'>
                                    <img src='img/me-full.jpg' alt='Breydon Brennan'/>
                            </div>
                        </div>
                    </div>
                </div>
            </div> */}
            <div className='container'>
                <div className='row justify-content-around'>
                    <div className='col'>
                        <div className='d-flex flex-column padding-text'>
                            <h2 id="i-intro">Hello, my name is </h2>
                            <h1 id="h-100">Breydon Brennan!</h1>
                            <div className='d-flex justify-content-left align-items-center'>
                                <h2>I am</h2>
                                <h2>
                                    <Typewriter
                                            options={{
                                                strings: ["a student", "an intern","a coding enthusiast"],
                                                autoStart: true,
                                                loop: true,
                                            }}
                                    />
                                </h2>
                            </div>
                            <p className='p-text'>
                                I am a current junior attending Eastern Illinois University, majoring in Computer Information Technology and minoring in Computer Science. I enjoy working on many programming projects, leading to the reason why I made this page. All my projects showcased on this page were exhilarating, challenging, and overall helpful to my learning experience. I have put in a great amount of time and love into these projects, so feel free to scroll down and check them out!
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default intro
