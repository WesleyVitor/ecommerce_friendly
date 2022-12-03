import React, {useState} from 'react'
import axios from 'axios'





export default function Login(){
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleChange = (e:React.FormEvent<HTMLInputElement>)=>{
        const name = e.currentTarget.name
        const value = e.currentTarget.value
        if( name == 'username'){
            setUsername(value)
        }else{
            setPassword(value)
        }
        

    }
    const handleSubmit = (e:React.SyntheticEvent)=>{
        const data = {
            'username':username,
            'password':password
        }
        axios({
        method: 'post',
        url: "http://localhost:8000/core/users/login",
        data: data
        
        })
        .then((response)=>{
            localStorage.setItem('Authorization', response.data.token);
            setUsername("");
            setPassword("");

        })
        .catch((error)=>{
            console.error('Error:', error);
        });
        

        
    }
    return (
        <form onSubmit={(e:React.SyntheticEvent)=>{
            e.preventDefault();
            handleSubmit(e);
        }}>
            <div>
                <h1>Fazer Login</h1>
            </div>
            <div className="form-outline mb-4">
                <input type="username" id="form2Example1" name='username' className="form-control" onChange={handleChange} />
                <label className="form-label" htmlFor="form2Example1">Username</label>
            </div>

           
            <div className="form-outline mb-4">
                <input type="password" id="form2Example2" name='password' className="form-control" onChange={handleChange}/>
                <label className="form-label" htmlFor="form2Example2">Password</label>
            </div>
            <div className="form-outline mb-4">
                <input type="submit" id="form2Example3" className="btn btn-primary btn-block mb-4" value="Sign In" />
            </div>
            

           
            <div className="text-center">
                <p>Not a member? <a href="/">Register</a></p>
            </div>
            </form>
    )
}