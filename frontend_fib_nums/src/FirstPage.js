import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const FirstPage = () => {
    const defaultText = 'Enter a positive integer';
    const [input, setInput] = useState(defaultText);
    const [notValidInput, setNotValidInput] = useState(false);
    const navigation = useNavigate();
    const [isfetching, setIsFetching] = useState('false');

    const saveInput = (input) => {
        setInput(input.target.value);
    }
    
    const handleOnFocus = () => {
        setNotValidInput(false);
        if(input===defaultText) {
            setInput('');
        }
    }
    
    const handleOnBlur = () => {
        if(input==='') {
            setInput(defaultText);
        }
    }

    const handleOnClick = async () => {
        const num = parseInt(input);
        if(!isNaN(num) && num > 0) {
            //render the second page
            setIsFetching(true);
            try {
                const response = await axios.get('http://127.0.0.1:8000/fib_webapp/fib-num/', {
                    params: {
                    num: input
                    }
                })
                const data = await JSON.parse(response.data);
                setIsFetching(false);
                // console.log(input);
                navigation('/second-page', {state: { n_value: input, numbers : data }});
            } catch(error) {
                console.error('Error generating fibonacci numbers: ', error);
                setIsFetching(false);
            }
        }
        else {
            setInput(defaultText);
            console.log('not valid input');
            setNotValidInput(true);
        }
    }

    return (
    <div style={{display: 'flex', flexDirection: 'column'}}>
      <h1 style={{margin: '5%', alignSelf: 'center'}}>Fibonacci Numbers Generator</h1>
      <h2 style={{margin: '5%', alignSelf: 'center'}}>Enter a positive integer(n) for generating first n fibonacci numbers</h2>
      <input className='input' type="text" value={input} onChange={saveInput} 
      onFocus={handleOnFocus} onBlur={handleOnBlur}
      style={{marginLeft: '1%', marginRight: '1%',alignSelf: 'center'}}/>
      <button onClick={handleOnClick}
      style={{marginTop: '1%',marginLeft: '1%', marginRight: '1%',alignSelf: 'center'}}>Submit</button>
      {notValidInput ? <p style={{margin: '1%', alignSelf: 'center'}}>Enter valid input</p> : null}
    </div>
    )
}

export default FirstPage;