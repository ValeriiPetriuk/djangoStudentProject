import axios from 'axios';
import { GROUPS_LIST_FAIL, GROUPS_LIST_REQUEST, GROUPS_LIST_SUCCESS } from "../constants/groupsConstans"


export const listGroups = () => async (dispatch) => {
    try {
        dispatch({ type: GROUPS_LIST_REQUEST })

      
        const { data } = await axios.get(`http://127.0.0.1:8000/api/v1/groups/`)

        dispatch({
            type: GROUPS_LIST_SUCCESS,
            payload: data
        })

    } catch (error) {
        dispatch({
            type: GROUPS_LIST_FAIL,
            payload: error.response && error.response.data.detail
                ? error.response.data.detail
                : error.message,
        })
    }
}