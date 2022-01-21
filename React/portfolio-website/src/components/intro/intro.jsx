import '../../App.css';
import 'bootstrap/dist/css/bootstrap.css';
import Typewriter from 'typewriter-effect';

// <div className='spacer layer-wave'></div>

function intro(){
    return (
        <>
            {/* <div className='d-flex justify-content-between align-items-center'>
                <div className='d-flex flex-column p-5'>
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
                    <p className='w-50'>
                        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam dictum suscipit risus, id egestas ex auctor at. Maecenas sagittis lectus felis, sed pretium neque euismod eget. Curabitur varius lobortis nunc, ut pharetra elit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam id urna varius, ullamcorper nunc id, tempus nunc. Phasellus congue velit libero. In hac habitasse platea dictumst.
                    </p>
                </div>
                
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
                <div className='col'>
                    <div className='d-inline-flex flex-column p-5'>
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
                        <p className='w-50'>
                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam dictum suscipit risus, id egestas ex auctor at. Maecenas sagittis lectus felis, sed pretium neque euismod eget. Curabitur varius lobortis nunc, ut pharetra elit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam id urna varius, ullamcorper nunc id, tempus nunc. Phasellus congue velit libero. In hac habitasse platea dictumst.
                        </p>
                    </div>
                    <div className='p-5'>
                        <div className='d-flex justify-content-center align-items-center'>
                            <div className='hexagon'>
                                <div className='hex-background'>
                                    <img src='img/me-full.jpg' alt='Breydon Brennan'/>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default intro