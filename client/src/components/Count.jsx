import React, { useState, useEffect } from 'react'

const Count = props => {
  
    const {num, duration} = props.data
    const [count, setCount] = useState('0');

    useEffect(() => {
        let start = 0;

        const end = parseInt(num.sustring(0,3));

        if (start === end) return;

        let totalMilSecDur = parseInt(duration);
        let incrementTime = (totalMilSecDur / end) * 1000;  
        let timer = setInterval(() => {
            start++;
            setCount(String(start) + num.substring(3));
            if (start === end) clearInterval(timer);
        }, incrementTime); 
    })

    return (
        <i>{count}</i>
    )
}

export default Count