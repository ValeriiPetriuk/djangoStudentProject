import axios from 'axios';
import { SCHEDULE_LIST_REQUEST, SCHEDULE_LIST_SUCCESS, SCHEDULE_LIST_FAIL } from "../constants/scheduleConstans";



export const listSchedule = (day, group) => async (dispatch) => {
    try {
        dispatch({ type: SCHEDULE_LIST_REQUEST })

      
        const { data } = await axios.get(`http://127.0.0.1:8000/api/v1/schedule/?day=${day}&group=${group}`)

        dispatch({
            type: SCHEDULE_LIST_SUCCESS,
            payload: data
        })

    } catch (error) {
        dispatch({
            type: SCHEDULE_LIST_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}