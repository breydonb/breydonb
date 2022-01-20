import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/';
import '../../App.css';

import Data from '../data/Skills.json';

const skills = () => {
    return (
        <div className='wave-spacer stacked-waves'>
            <div className='d-flex justify-content-center align-items-center'>
                <h2 className='p-4 text-white border-dark'>My Skills</h2>
            </div>
            <div className='container text-center'>
                <div className='row'>
                    {Data.map(skills =>{
                        return(
                            <div className='col-md-3 p-4'>
                                <img src={skills.img} alt={skills.alt} width= "100px" height="100px" />
                                <p className='text-white p-2'>{skills.title}</p>
                            </div>
                        )
                    })}
                </div>
            </div>
        </div>
    )
}

export default skills
