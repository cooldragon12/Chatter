import { CircularProgress, Button } from "@material-ui/core"
const LoadingButton =(props)=>{
    const {loading, classes, children, ...other} =props;
    if (loading){
        retrun(
            <Button className={classess} {...other}>
                <CircularProgress />
                
            </Button>
        )
    }else{
        return(
            <Button className={classes} {...other}/>
                
        )
    }
}
export default LoadingButton;