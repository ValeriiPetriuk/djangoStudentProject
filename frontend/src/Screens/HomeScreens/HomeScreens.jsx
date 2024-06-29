import { Grid, Box, Paper } from "@mui/material";
import { useDispatch, useSelector } from 'react-redux';
import SheduleTable from "../../Components/SheduleTable";
import SelectDay from "../../Components/SelectDay";
import SelectGroup from "../../Components/SelectGroup";
import { useEffect, useState } from "react";
import { listSchedule } from "../../actions/scheduleActions";
import { listGroups } from "../../actions/groupsActions";


const HomeScreens = () => {

    const dispatch = useDispatch()
    const scheduleList = useSelector(state => state.scheduleList)
    const {schedule, loading: loadingSchedule} = scheduleList

    const groupsList = useSelector(state => state.groupsList)
    const {groups} = groupsList

    const [day, setDay] = useState('Понеділок');
    const [group, setGroup] = useState('');

    useEffect(()=> {
      dispatch(listSchedule(day, group))
      dispatch(listGroups())
    }, [dispatch, day, group])

    
    const handleChangeDay = (event) => {
        setDay(event.target.value);
    };
  
    const handleChangeGroup = (event) => {
        setGroup(event.target.value);
    }
    return(
        <Box sx={{flexGrow: 1, marginTop: 2}}>
            <Grid container spacing={2}>
                <Grid item xs={12}>
                <Paper sx={{ padding: 2 }}>
                        <Grid container spacing={2}>
                            <Grid item xs={6}>
                                <SelectDay day={day} handleChange={handleChangeDay}/>
                            </Grid>
                            <Grid item xs={6}>
                                <SelectGroup  group={group} handleChangeGroup={handleChangeGroup} groups={groups}/>
                            </Grid>
                        </Grid>
                    </Paper>
                    
                </Grid>
                <Grid item xs={12} >
                    <Paper>
                        <SheduleTable schedule={schedule} loading={loadingSchedule}/>
                    </Paper>
                </Grid>
             
            </Grid>
        </Box>

     
    )
}

export default HomeScreens;