import React from 'react';
import { useLocation } from 'react-router-dom';

const Display = () => {
    const location = useLocation();
    const data = location.state ? location.state.numbers : undefined;
    const n = location.state.n_value;
    const values = [];
    var stringList = '';

    data.forEach((item) => {
        values.push(item.value);
    })

    stringList = values.join(', ');

    // if(data) {
    //     console.log(data);
    //     console.log(stringList);
    //     console.log(n);
    // }
    return (
        <div style={{display: 'flex', flexDirection: 'column'}}>
            { data ? 
            //     <table style={{alignSelf: 'center', margin: '20%', borderCollapse: 'collapse'}}>
            //     <thead>
            //       <tr>
            //         <th style={{border: '1px solid black', padding: 8, textAlign: 'center', wordWrap:'break-word'}}>Fibonacci Number</th>
            //         <th style={{border: '1px solid black', padding: 8, textAlign: 'center', wordWrap:'break-word'}}>Value</th>
            //       </tr>
            //     </thead>
            //     <tbody>
            //       {data.map((item) => (
            //         <tr key={item.fib_no}>
            //           <td style={{border: '1px solid black', padding: 1, textAlign: 'center', wordWrap:'break-word'}}>{item.fib_no}</td>
            //           <td style={{border: '1px solid black', padding: 1, textAlign: 'center', wordWrap:'break-word'}}>{item.value}</td>
            //         </tr>
            //       ))}
            //     </tbody>
            //   </table>
            <div style={{alignSelf: 'center', margin: '15%'}}>
                <p>The first {n} Fibonacci numbers are: </p>
                {stringList}
            </div>
                : 
                <p>Generating numbers....</p>}
        </div>
    )
}

export default Display;