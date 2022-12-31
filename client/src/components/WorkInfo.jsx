import React from 'react';
import '../css/WorkInfo.css';
import { GiCook, GiPizzaSlice } from 'react-icons/gi';
import { FaAward } from 'react-icons/fa';
import { IoMdPeople } from 'react-icons/io';


const WorkInfo = () => {
  const info = [
    {'logo': GiPizzaSlice, "number": "100", "title": "Pizza Branches"},
    {"logo": FaAward, "number": "85", "title": "Number of Awards"},
    {"logo": IoMdPeople, "number": "10,567", "title": "Happy Customer"},
    {"logo": GiCook, "number": "900", "title": "Staff"}
  ];

  let items = [];

  const Icon = ({data}) => {
    return (
      <div className="icon_block">
        <div className="icon_image">
          {/* <div className='icon_image_layout'> */}
            <data.logo className='icon_image_img'/>
          {/* </div> */}
        </div>
        <div className="icon_info">
          <h2>{data.number}</h2>
          <p>{data.title}</p>
        </div>
      </div>
    )
  }

  info.forEach((el) => {
    items.push(<Icon data={el}/>);
  });

  const [scroll, setScroll] = React.useState(0);

  const handleScroll = () => {
    setScroll(window.scrollY);
  };

  React.useEffect(() => {
    window.addEventListener("scroll", handleScroll);
  }, []);
  
  return (
    <section className='workInfo' style={{backgroundPosition : `50% ${window.scrollY*0.65}px`}}>
        <div className="overlay">
            <div className="workInfo_content" >
              {items}
            </div>
        </div>
    </section>
  )
}

export default WorkInfo