import React from "react";
export interface ItemListProps{
    datas: [],
    ItemComponent:React.FC<any>,
    name: string
}
const ItemListLayout:React.FC<ItemListProps> = (props)=>{
    const {datas, ItemComponent, name} = props;
    // Left the layout of this ItemList
    return(
        <>
            {
                datas.map((data, i)=><ItemComponent key={i} {...{[name]:data}}/>)
            }
        
        </>
    )

}

export default ItemListLayout;