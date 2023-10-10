import React from "react";
export interface GroupTabProps {
    name:string,
    overview:string,
    image:string
}
const GroupTab:React.FC<GroupTabProps> = (props)=>{
    const {name, overview} = props;
    return (
        <div className="w-0.9 bg-white flex">
            <div className="w-[52px] flex items-center justify-center padd">
                {/* <img src={image} alt={name+"-profile"} /> */}
            </div>
            <div className="w-4/5">
                <h3>{name}</h3>
                <p>{overview}</p>
            </div>
        </div>
    )
}
export default GroupTab;