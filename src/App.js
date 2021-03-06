import React, { Fragment, useState, useEffect } from 'react';
import axios from 'axios';
import Example from './example/example.js';
import AddLink from './components/addlink.js';

function App() {
    const [data, setData] = useState([]);
    const [query, setQuery] = useState('redux');

    useEffect(() => {
        const fetchData = async () => {
            const result = await axios(
                'http://192.168.1.131:8000/items/',
            );

            console.log(result.data)
            setData(result.data);
            
        };

        fetchData().catch(()=>setData([{url:"error",title:"error",points: "0"}]));
    }, []);

    return (
        <Fragment>
            <input
                type="text"
                value={query}
                onChange={event => setQuery(event.target.value)}
            />
            <Example/>
            <ul>
                {data.map(item => (
                    <li key={item.url}>
                        <a href={item.url}>{item.title}</a>{item.points.toString()}
                    </li>
                ))}
            </ul>
            <AddLink/>
        </Fragment>
    );
}

export default App;
