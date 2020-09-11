import React, { useState } from 'react';
import axios from "axios";

function AddLink() {
    const [linkdata, setLinkdata] = useState({"url": "http://www.example.com", "title": "Example", "points": 0})


    const handleSubmit = (e) => {
        e.preventDefault()
        axios.post('http://192.168.1.131:8000/items/', linkdata)
            .then(function (response) {
                console.log(response)
            })
            .catch(function (error) {
                console.log(error)
            })
    };

        const handleChange = (event) => {
        setLinkdata({...linkdata, [event.target.name]: event.target.value})
        console.log(`${event.target.name} -> ${event.target.value}`)
    };

    return (
        <fragment>
            <form onSubmit={handleSubmit}>
                <input type="text" name="url" onChange={handleChange} value={linkdata.url}/>
                <input type="text" name="title" onChange={handleChange} value={linkdata.title}/>
                <button type="submit">Add</button>
            </form>
        </fragment>
    );
};

export default AddLink;
